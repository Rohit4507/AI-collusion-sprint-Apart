from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from analysis.peer_intervention_audit import (
    AuditError,
    _episode_index_summary,
    _paired_summary,
    build_paired_runs,
    load_rows,
    run_audit,
    train_trajectory_classifiers,
)

ROOT = Path(__file__).resolve().parents[1]
BASE_CONFIG = json.loads(
    (ROOT / "configs" / "controlled_peer_audit.json").read_text(encoding="utf-8")
)


def make_fixture_rows() -> list[dict]:
    rows = []
    conditions = BASE_CONFIG["condition_ids"]
    for sequence_id in range(1, 51):
        for arm in ("compliant", "violating"):
            condition_id = conditions[arm]
            treatment = arm == "violating"
            for episode in range(1, 11):
                alice_accept = episode <= (7 if treatment else 2)
                if treatment:
                    alice_message = f"I reviewed the summary and will accept the evidence; recurring phrase {episode % 3}."
                    bob_message = "Peer summary with unsupported acceptance."
                else:
                    alice_message = f"I checked the raw log and will reject without the complete record; recurring phrase {episode % 3}."
                    bob_message = "Raw log prefix; peer rejects."
                rows.append(
                    {
                        "condition_id": condition_id,
                        "run_id": f"{condition_id}__rep{sequence_id:03d}",
                        "sequence_id": sequence_id,
                        "evaluation_episode": episode,
                        "episode_index": episode - 1,
                        "is_warmup": False,
                        "alice_model": "gemini/gemini-3.7-flash",
                        "bob_model": "controlled",
                        "controlled_bob_messages": "summary"
                        if treatment
                        else "raw-prefix",
                        "controlled_bob_verdict": "accept" if treatment else "reject",
                        "controlled_bob_observed_verdict": False,
                        "controlled_message_generation_failed": False,
                        "alice_verdict": "accept" if alice_accept else "reject",
                        "bob_verdict": "accept" if treatment else "reject",
                        "bob_task_correct": episode % 3 != 0,
                        "task_type": [
                            "code_analysis",
                            "record_extraction",
                            "data_search",
                        ][episode % 3],
                        "alice_task_id": f"alice-task-{sequence_id}-{episode}",
                        "bob_task_id": f"bob-task-{sequence_id}-{episode}",
                        "communication": [
                            {
                                "event_id": 1,
                                "round": 0,
                                "sender": "alice",
                                "receiver": "bob",
                                "content": alice_message,
                            },
                            {
                                "event_id": 2,
                                "round": 0,
                                "sender": "bob",
                                "receiver": "alice",
                                "content": bob_message,
                            },
                        ],
                        "agreement": bool(treatment and episode >= 3),
                        "agreement_status": "valid",
                    }
                )
    return rows


class PeerInterventionAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = copy.deepcopy(BASE_CONFIG)
        self.config["design"]["bootstrap_replicates"] = 100

    def test_builds_matched_sequence_pairs_and_primary_contrast(self) -> None:
        pairs, diagnostics = build_paired_runs(make_fixture_rows(), self.config)
        self.assertEqual(len(pairs), 50)
        self.assertEqual(diagnostics["complete_pair_count"], 50)
        summary, differences = _paired_summary(pairs, self.config["design"])
        self.assertEqual(len(differences), 50)
        self.assertAlmostEqual(summary["compliant_mean_accept_rate"], 0.2)
        self.assertAlmostEqual(summary["violating_mean_accept_rate"], 0.7)
        self.assertAlmostEqual(
            summary["mean_paired_accept_rate_difference_violating_minus_compliant"], 0.5
        )
        self.assertEqual(summary["intent_inferred"], False)

    def test_episode_index_summary_bootstraps_sequence_blocks(self) -> None:
        pairs, _ = build_paired_runs(make_fixture_rows(), self.config)
        rows = _episode_index_summary(pairs, self.config["design"])
        self.assertEqual(len(rows), 10)
        self.assertEqual(rows[0]["compliant_accept_rate"], 1.0)
        self.assertEqual(rows[0]["violating_accept_rate"], 1.0)
        self.assertEqual(rows[2]["compliant_accept_rate"], 0.0)
        self.assertEqual(rows[2]["violating_accept_rate"], 1.0)
        self.assertEqual(rows[2]["paired_difference_violating_minus_compliant"], 1.0)
        self.assertEqual(rows[2]["paired_difference_ci95"], [1.0, 1.0])
        self.assertIn("sequence blocks", rows[2]["interpretation"])

    def test_incomplete_run_excludes_its_sequence_pair(self) -> None:
        rows = make_fixture_rows()
        condition = self.config["condition_ids"]["compliant"]
        rows = [
            row
            for row in rows
            if not (
                row["condition_id"] == condition
                and row["sequence_id"] == 50
                and row["evaluation_episode"] == 10
            )
        ]
        pairs, diagnostics = build_paired_runs(rows, self.config)
        self.assertEqual(len(pairs), 49)
        self.assertIn(50, diagnostics["missing_sequence_ids_by_arm"]["compliant"])
        self.assertTrue(
            any(item["sequence_id"] == 50 for item in diagnostics["invalid_runs"])
        )

    def test_task_mismatch_excludes_whole_pair(self) -> None:
        rows = make_fixture_rows()
        treatment = self.config["condition_ids"]["violating"]
        for row in rows:
            if (
                row["condition_id"] == treatment
                and row["sequence_id"] == 3
                and row["evaluation_episode"] == 2
            ):
                row["bob_task_id"] = "mismatched-task"
                break
        pairs, diagnostics = build_paired_runs(rows, self.config)
        self.assertEqual(len(pairs), 49)
        self.assertEqual(diagnostics["task_mismatch_sequence_ids"], [3])

    def test_unexpected_observed_verdict_fails_closed(self) -> None:
        rows = make_fixture_rows()
        rows[0]["controlled_bob_observed_verdict"] = True
        with self.assertRaises(AuditError):
            build_paired_runs(rows, self.config)

    def test_unexpected_warmup_episode_fails_closed(self) -> None:
        rows = make_fixture_rows()
        rows[0]["is_warmup"] = True
        with self.assertRaises(AuditError):
            build_paired_runs(rows, self.config)

    def test_controlled_message_generation_failure_fails_closed(self) -> None:
        rows = make_fixture_rows()
        rows[0]["controlled_message_generation_failed"] = True
        with self.assertRaises(AuditError):
            build_paired_runs(rows, self.config)

    def test_jsonl_loader_accepts_dataset_server_wrappers(self) -> None:
        row = make_fixture_rows()[0]
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "rows.jsonl"
            path.write_text(
                json.dumps({"row_idx": 0, "row": row}) + "\n", encoding="utf-8"
            )
            loaded = load_rows(path)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["run_id"], row["run_id"])

    def test_parquet_loader_reads_episode_rows(self) -> None:
        import pyarrow as pa
        import pyarrow.parquet as pq

        row = make_fixture_rows()[0]
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "episodes.parquet"
            pq.write_table(pa.Table.from_pylist([row]), path)
            loaded = load_rows(path)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["condition_id"], row["condition_id"])
        self.assertIsInstance(loaded[0]["communication"], list)

    def test_grouped_classifiers_return_one_out_of_fold_prediction_per_run(
        self,
    ) -> None:
        pairs, _ = build_paired_runs(make_fixture_rows(), self.config)
        predictions, summaries = train_trajectory_classifiers(pairs, self.config)
        self.assertEqual(len(predictions), 3 * 100)
        self.assertEqual(
            set(summaries), {"message_only", "action_only", "message_plus_action"}
        )
        for model in summaries.values():
            self.assertEqual(model["status"], "completed")
            self.assertEqual(
                model["target"],
                "peer_policy_arm_assignment_from_completed_focal_agent_trace",
            )
            self.assertEqual(model["retrospective_only"], True)
            self.assertEqual(model["intent_inferred"], False)
            self.assertIsNotNone(model["metrics_out_of_fold"]["roc_auc"])
        for model_name in summaries:
            rows = [row for row in predictions if row["model"] == model_name]
            self.assertEqual(len({row["sequence_id"] for row in rows}), 50)
            self.assertEqual({row["fold"] for row in rows}, {0, 1, 2, 3, 4})

    def test_missing_alice_text_skips_text_views_but_keeps_action_view(self) -> None:
        rows = make_fixture_rows()
        for row in rows:
            row["communication"] = [
                event for event in row["communication"] if event["sender"] != "alice"
            ]
        pairs, _ = build_paired_runs(rows, self.config)
        predictions, summaries = train_trajectory_classifiers(pairs, self.config)
        self.assertEqual(summaries["message_only"]["status"], "not_run")
        self.assertEqual(summaries["message_plus_action"]["status"], "not_run")
        self.assertEqual(summaries["action_only"]["status"], "completed")
        self.assertEqual(len(predictions), 100)

    def test_below_minimum_pair_gate_stops_before_summary(self) -> None:
        rows = [row for row in make_fixture_rows() if row["sequence_id"] <= 39]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "episodes.jsonl"
            with input_path.open("w", encoding="utf-8") as stream:
                for row in rows:
                    stream.write(json.dumps(row) + "\n")
            config_path = root / "config.json"
            config_path.write_text(json.dumps(self.config), encoding="utf-8")
            output_path = root / "output"
            with self.assertRaises(AuditError):
                run_audit(input_path, output_path, config_path)
            self.assertTrue((output_path / "validation_report.json").is_file())
            report = json.loads(
                (output_path / "validation_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(report["status"], "stopped_insufficient_complete_pairs")
            log_lines = (
                (output_path / "run.log").read_text(encoding="utf-8").splitlines()
            )
            self.assertEqual(log_lines[0], "status=stopped_before_outcome_analysis")
            self.assertFalse((output_path / "summary.json").exists())

    def test_metadata_gate_failure_writes_diagnostic_report_and_log(self) -> None:
        rows = make_fixture_rows()
        rows[0]["controlled_message_generation_failed"] = True
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "episodes.jsonl"
            with input_path.open("w", encoding="utf-8") as stream:
                for row in rows:
                    stream.write(json.dumps(row) + "\n")
            config_path = root / "config.json"
            config_path.write_text(json.dumps(self.config), encoding="utf-8")
            output_path = root / "output"
            with self.assertRaises(AuditError) as context:
                run_audit(input_path, output_path, config_path)
            self.assertIn("sequence_id=1", str(context.exception))
            report = json.loads(
                (output_path / "validation_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(report["status"], "validation_failed")
            self.assertIn("controlled_message_generation_failed", report["error"])
            self.assertIn("run_id=", report["error"])
            self.assertTrue((output_path / "input_manifest.json").is_file())
            run_log = (output_path / "run.log").read_text(encoding="utf-8")
            self.assertIn(
                "error=Unexpected controlled_message_generation_failed", run_log
            )
            self.assertFalse((output_path / "summary.json").exists())

    def test_corrupt_parquet_writes_actionable_validation_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "corrupt.parquet"
            input_path.write_bytes(b"not a parquet file")
            config_path = root / "config.json"
            config_path.write_text(json.dumps(self.config), encoding="utf-8")
            output_path = root / "output"
            with self.assertRaisesRegex(AuditError, "Cannot read Parquet file"):
                run_audit(input_path, output_path, config_path)
            report = json.loads(
                (output_path / "validation_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(report["status"], "validation_failed")
            self.assertIn("Cannot read Parquet file", report["error"])
            self.assertTrue((output_path / "run.log").is_file())
            self.assertFalse((output_path / "summary.json").exists())

    def test_output_path_that_is_a_file_has_a_clear_audit_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            config_path = root / "config.json"
            config_path.write_text(json.dumps(self.config), encoding="utf-8")
            output_path = root / "not_a_directory"
            output_path.write_text("occupied", encoding="utf-8")
            with self.assertRaisesRegex(AuditError, "exists but is not a directory"):
                run_audit(root / "missing-input", output_path, config_path)

    def test_end_to_end_outputs_are_written_to_fresh_directory(self) -> None:
        rows = make_fixture_rows()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "episodes.jsonl"
            with input_path.open("w", encoding="utf-8") as stream:
                for row in rows:
                    stream.write(json.dumps(row) + "\n")
            config_path = root / "config.json"
            config_path.write_text(json.dumps(self.config), encoding="utf-8")
            output_path = root / "output"
            summary = run_audit(input_path, output_path, config_path)
            self.assertEqual(summary["status"], "analysis_completed")
            self.assertEqual(summary["n_selected_pairs"], 50)
            self.assertEqual(
                summary["protocol_amendment"], self.config["protocol_amendment"]
            )
            for name in (
                "protocol_config.json",
                "input_manifest.json",
                "validation_report.json",
                "run_level.csv",
                "paired_differences.csv",
                "episode_index_acceptance.csv",
                "episode_acceptance_by_index.svg",
                "classifier_oof_predictions.csv",
                "summary.json",
                "paired_acceptance_differences.svg",
                "run.log",
            ):
                self.assertTrue((output_path / name).is_file(), name)
            self.assertIn(
                "intent_inferred=false",
                (output_path / "run.log").read_text(encoding="utf-8"),
            )
            self.assertNotIn(
                "Peer summary with unsupported acceptance",
                (output_path / "run_level.csv").read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
