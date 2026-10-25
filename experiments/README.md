# Vendored upstream `controlled.py` — fenced-JSON fix

`controlled.py` in this directory is a **vendored snapshot** of
[`experiments/controlled.py`](https://github.com/SALT-NLP/agent-collusion/blob/main/experiments/controlled.py)
from SALT-NLP/agent-collusion (MIT; see `UPSTREAM_LICENSE`), upstream blob
`b7863603560a736403cf1337aa5909de6e377458`, fetched 2026-10-25. It did not
previously exist in this repository.

## The bug and the fix

Upstream `save_bob()` parses the model response with

```python
outgoing = validate_messages(json.loads(result["content"]))
```

A model that wraps an otherwise valid JSON array in an outer Markdown code
fence (`` ```json ... ``` ``) makes `json.loads()` fail. The existing code
then retries and, after 3 attempts, records `generation_failed=True`. In
the released episode table that surfaces as
`controlled_message_generation_failed`, which this repository's frozen
audit (amendment A1) correctly fails closed on.

The only local change vs upstream is `_unwrap_json_code_fence()` and its
single use before `json.loads()` in `save_bob()`:

- It removes the fence **only** when the stripped response consists solely
  of an opening `` ``` ``/`` ```json `` line, the JSON text, and a closing
  `` ``` `` line.
- Plain JSON, prose around a fence, other language tags, a missing closing
  fence, nested/multiple fences, and non-string content are returned
  unchanged, so `json.loads()` and the existing `except (ValueError,
  TypeError)` retry behaviour are preserved.
- `validate_messages()` is untouched: exactly 5 strings, each at most 200
  characters. A fenced response that violates the count/length rules is
  still rejected, still retries, and still ends as
  `generation_failed=True` — failure flags are never suppressed.

Verify that this is the only change by diffing against upstream:

```bash
gh api repos/SALT-NLP/agent-collusion/contents/experiments/controlled.py \
  -H "Accept: application/vnd.github.raw+json" > /tmp/upstream_controlled.py
diff -u /tmp/upstream_controlled.py experiments/controlled.py
```

The intended upstream contribution is exactly that diff (excluding the
vendoring header comment). Fixing generation does **not** repair any
already-written dataset rows or cache files, and none are modified here.

## Scope in this repository

- The offline audit in `analysis/` does **not** import this module, does
  not call models, and is unchanged — including the A1 fail-closed gate on
  `controlled_message_generation_failed` in
  `analysis/peer_intervention_audit.py` and
  `configs/controlled_peer_audit.json`.
- The upstream-only `experiments.*` imports (`agents`, `memory`,
  `protocol`, `usage`) are **not** vendored, so do not import this file
  directly here. `tests/test_controlled.py` loads it by file path with
  those imports stubbed; no model, network, dataset, or cache file is used.
- The real-data audit remains gated on obtaining the local `episodes`
  Parquet export (see `research/phase5_data_gate.md`). This fix plus
  synthetic tests are not a real-data result.
