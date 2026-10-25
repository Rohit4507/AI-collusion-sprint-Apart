"""Regression tests for the vendored upstream ``experiments/controlled.py``.

Covered behaviour: only a valid outer Markdown JSON code fence is unwrapped
before ``json.loads()``; the upstream 5-string / 200-character validation,
the 3-attempt retry loop, and the ``generation_failed`` flag are preserved.
The upstream-only ``experiments.*`` imports are stubbed below; these tests
use no model, network, dataset, or cache file (``save_bob`` writes only to a
temporary directory).
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import types
import unittest
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
CONTROLLED_PATH = ROOT / "experiments" / "controlled.py"
CONFIG_PATH = ROOT / "configs" / "controlled_peer_audit.json"

VALID_MESSAGES = [f"evidence message {index}" for index in range(1, 6)]


class _FakeLLMRetryLimitExceededError(Exception):
    """Stand-in for the upstream exception type imported by controlled.py."""


def _load_controlled():
    """Load experiments/controlled.py by path with upstream imports stubbed."""

    def _unpatched_run_reflection_turn(**kwargs):
        raise AssertionError("run_reflection_turn stub must be patched per-test")

    def _is_internal_marker(message):
        return False

    def _format_private_raw_log(slot):
        return slot.get("formatted_raw_log", "x" * 1200)

    def _agent_state(state, actor):
        return state["agents"][actor]

    def _make_llm_usage_recorder(**kwargs):
        def _recorder(*args, **recorder_kwargs):
            return None

        return _recorder

    agents = types.ModuleType("experiments.agents")
    agents.LLMRetryLimitExceededError = _FakeLLMRetryLimitExceededError
    agents.run_reflection_turn = _unpatched_run_reflection_turn
    memory_messages = types.ModuleType("experiments.memory.messages")
    memory_messages.is_internal_marker = _is_internal_marker
    messaging = types.ModuleType("experiments.protocol.messaging")
    messaging._format_private_raw_log = _format_private_raw_log
    state_module = types.ModuleType("experiments.protocol.state")
    state_module.agent_state = _agent_state
    usage = types.ModuleType("experiments.usage")
    usage.make_llm_usage_recorder = _make_llm_usage_recorder

    stubs = {
        "experiments": types.ModuleType("experiments"),
        "experiments.agents": agents,
        "experiments.memory": types.ModuleType("experiments.memory"),
        "experiments.memory.messages": memory_messages,
        "experiments.protocol": types.ModuleType("experiments.protocol"),
        "experiments.protocol.messaging": messaging,
        "experiments.protocol.state": state_module,
        "experiments.usage": usage,
    }
    missing = object()
    saved = {name: sys.modules.get(name, missing) for name in stubs}
    sys.modules.update(stubs)
    try:
        spec = importlib.util.spec_from_file_location(
            "controlled_under_test", CONTROLLED_PATH
        )
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Cannot load controlled.py from {CONTROLLED_PATH}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
    finally:
        for name, original in saved.items():
            if original is missing:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = original
    return module


controlled = _load_controlled()


def fenced(payload: str, tag: str = "json") -> str:
    opening = f"```{tag}" if tag else "```"
    return f"{opening}\n{payload}\n```"


def parse(content):
    """Mirror the single parsing call site inside save_bob()."""
    return controlled.validate_messages(
        json.loads(controlled._unwrap_json_code_fence(content))
    )


@dataclass
class _FakeModelConfig:
    model: str = "fake-model"


class UnwrapAndValidationTests(unittest.TestCase):
    def test_plain_json_still_parses(self) -> None:
        self.assertEqual(parse(json.dumps(VALID_MESSAGES)), VALID_MESSAGES)

    def test_fenced_json_parses(self) -> None:
        payload = json.dumps(VALID_MESSAGES, indent=2)
        self.assertEqual(parse(fenced(payload)), VALID_MESSAGES)

    def test_bare_and_uppercase_fences_parse(self) -> None:
        payload = json.dumps(VALID_MESSAGES)
        self.assertEqual(parse(fenced(payload, tag="")), VALID_MESSAGES)
        self.assertEqual(parse(fenced(payload, tag="JSON")), VALID_MESSAGES)

    def test_fenced_json_with_surrounding_whitespace_or_crlf_parses(self) -> None:
        payload = json.dumps(VALID_MESSAGES)
        self.assertEqual(parse(f"\n\n  {fenced(payload)}  \n"), VALID_MESSAGES)
        self.assertEqual(parse(f"```json\r\n{payload}\r\n```\r\n"), VALID_MESSAGES)

    def test_malformed_json_is_rejected_plain_and_fenced(self) -> None:
        cases = (
            "not json at all",
            "{not json",
            fenced('["a",]'),
            fenced(""),
            "",
        )
        for content in cases:
            with self.subTest(content=content[:24]), self.assertRaises(ValueError):
                parse(content)

    def test_wrong_item_count_is_rejected_plain_and_fenced(self) -> None:
        for messages in (VALID_MESSAGES[:4], VALID_MESSAGES + ["extra"]):
            payload = json.dumps(messages)
            for content in (payload, fenced(payload)):
                with (
                    self.subTest(count=len(messages), fenced="```" in content),
                    self.assertRaises(ValueError),
                ):
                    parse(content)

    def test_overlength_message_is_rejected_plain_and_fenced(self) -> None:
        at_limit = ["x" * controlled.MESSAGE_CHARS] * controlled.MESSAGE_COUNT
        self.assertEqual(parse(fenced(json.dumps(at_limit))), at_limit)
        over_limit = ["x" * (controlled.MESSAGE_CHARS + 1)] + VALID_MESSAGES[1:]
        payload = json.dumps(over_limit)
        for content in (payload, fenced(payload)):
            with self.subTest(fenced="```" in content), self.assertRaises(ValueError):
                parse(content)

    def test_non_string_items_and_non_arrays_are_rejected(self) -> None:
        for payload in (json.dumps([1, 2, 3, 4, 5]), json.dumps({"a": 1})):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                parse(fenced(payload))

    def test_only_a_valid_outer_fence_is_unwrapped(self) -> None:
        payload = json.dumps(VALID_MESSAGES)
        good_fence = fenced(payload)
        cases = {
            "prose_before_fence": f"Here you go:\n{good_fence}",
            "prose_after_fence": f"{good_fence}\nDone.",
            "missing_closing_fence": f"```json\n{payload}",
            "missing_opening_fence": f"{payload}\n```",
            "wrong_language_tag": fenced(payload, tag="python"),
            "multiple_fences": f"{good_fence}\n{good_fence}",
            "nested_fence": f"```json\n{good_fence}\n```",
        }
        for name, content in cases.items():
            with self.subTest(case=name):
                self.assertEqual(controlled._unwrap_json_code_fence(content), content)
                with self.assertRaises(ValueError):
                    parse(content)

    def test_non_string_content_preserves_type_error(self) -> None:
        self.assertIsNone(controlled._unwrap_json_code_fence(None))
        already_parsed = list(VALID_MESSAGES)
        self.assertIs(
            controlled._unwrap_json_code_fence(already_parsed), already_parsed
        )
        with self.assertRaises(TypeError):
            parse(None)

    def test_validation_limits_are_unchanged(self) -> None:
        self.assertEqual(controlled.MESSAGE_COUNT, 5)
        self.assertEqual(controlled.MESSAGE_CHARS, 200)
        self.assertEqual(controlled.validate_messages(VALID_MESSAGES), VALID_MESSAGES)
        with self.assertRaises(ValueError):
            controlled.validate_messages(VALID_MESSAGES[:4])
        with self.assertRaises(ValueError):
            controlled.validate_messages(["x" * 201] + VALID_MESSAGES[1:])


class SaveBobRetryTests(unittest.TestCase):
    """Exercise save_bob()'s preserved retry loop with a fake model turn."""

    def _save_bob_with_contents(self, contents: list):
        remaining = list(contents)
        calls = []

        def fake_run_reflection_turn(**kwargs):
            calls.append(kwargs)
            return {"content": remaining.pop(0), "reasoning_trace": None}

        slot = {
            "private_raw_log": ["log entry"],
            "task_tmp_dir": "/tmp/fake-task-dir",
            "formatted_raw_log": "x" * 1200,
        }
        prepared = SimpleNamespace(
            agents={
                "bob": SimpleNamespace(
                    task="fake-task",
                    code_path=None,
                    source_path=None,
                    database_path=None,
                )
            },
            state={
                "episode_id": "episode-1",
                "events": [],
                "agents": {"bob": slot},
            },
        )
        runtime = SimpleNamespace(
            config=_FakeModelConfig(),
            messages=[{"role": "user", "content": "task transcript"}],
        )
        reasoning_traces: list = []
        with tempfile.TemporaryDirectory() as temp_dir:
            config = SimpleNamespace(
                episode_index=0,
                controlled_bob_cache=str(Path(temp_dir) / "cache"),
                usage_journal_path=None,
                usage_invocation_id="invocation-1",
            )
            with mock.patch.object(
                controlled, "run_reflection_turn", fake_run_reflection_turn
            ):
                path = controlled.save_bob(
                    prepared, runtime, config, [], reasoning_traces
                )
            data = json.loads(Path(path).read_text(encoding="utf-8"))
        return data["payload"], calls, reasoning_traces

    def test_save_bob_accepts_fenced_json_on_first_attempt(self) -> None:
        payload, calls, _ = self._save_bob_with_contents(
            [fenced(json.dumps(VALID_MESSAGES, indent=2))]
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(payload["messages"], VALID_MESSAGES)
        self.assertIs(payload["generation_failed"], False)
        self.assertEqual(payload["generation_error"], "")

    def test_save_bob_still_accepts_plain_json_on_first_attempt(self) -> None:
        payload, calls, _ = self._save_bob_with_contents([json.dumps(VALID_MESSAGES)])
        self.assertEqual(len(calls), 1)
        self.assertEqual(payload["messages"], VALID_MESSAGES)
        self.assertIs(payload["generation_failed"], False)

    def test_save_bob_retries_after_malformed_then_accepts_fenced(self) -> None:
        payload, calls, traces = self._save_bob_with_contents(
            ["not json", fenced(json.dumps(VALID_MESSAGES))]
        )
        self.assertEqual(len(calls), 2)
        self.assertEqual([trace["attempt_idx"] for trace in traces], [0, 1])
        self.assertEqual(payload["messages"], VALID_MESSAGES)
        self.assertIs(payload["generation_failed"], False)

    def test_save_bob_retries_after_invalid_outer_fence_then_accepts_plain(
        self,
    ) -> None:
        prose_wrapped = f"Here you go:\n{fenced(json.dumps(VALID_MESSAGES))}"
        payload, calls, _ = self._save_bob_with_contents(
            [prose_wrapped, json.dumps(VALID_MESSAGES)]
        )
        self.assertEqual(len(calls), 2)
        self.assertEqual(payload["messages"], VALID_MESSAGES)
        self.assertIs(payload["generation_failed"], False)

    def test_save_bob_persistent_malformed_fails_closed_not_suppressed(
        self,
    ) -> None:
        payload, calls, traces = self._save_bob_with_contents(
            ["not json", fenced('["a",]'), "{broken"]
        )
        self.assertEqual(len(calls), 3)
        self.assertEqual([trace["attempt_idx"] for trace in traces], [0, 1, 2])
        self.assertIsNone(payload["messages"])
        self.assertIs(payload["generation_failed"], True)

    def test_save_bob_validation_failures_exhaust_retries_and_fail_closed(
        self,
    ) -> None:
        wrong_count = fenced(json.dumps(VALID_MESSAGES[:4]))
        overlength = fenced(json.dumps(["x" * 201] + VALID_MESSAGES[1:]))
        payload, calls, _ = self._save_bob_with_contents(
            [wrong_count, overlength, wrong_count]
        )
        self.assertEqual(len(calls), 3)
        self.assertIsNone(payload["messages"])
        self.assertIs(payload["generation_failed"], True)


class FrozenAuditGateTests(unittest.TestCase):
    def test_a1_generation_failure_gate_is_not_relaxed(self) -> None:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        self.assertIs(
            config["expected_fields"]["controlled_message_generation_failed"],
            False,
        )


if __name__ == "__main__":
    unittest.main()
