# Phase 5 — Data gate and evaluation attempt

- **Date:** 2026-10-18 (Asia/Calcutta)
- **Decision:** **Blocked before outcome analysis.** No selected-arm episode outcomes, detector metrics, or experimental findings were computed.
- **Protocol:** Internal v1.0 with pre-outcome amendments A1 (data integrity, 2026-10-18) and A2 (classifier failure handling, 2026-10-25); not externally registered.

## Checks completed

- **[Verified fact — metadata]** The datasets-server `/size` endpoint reports the `episodes` Parquet config at 15,976,423 bytes, 27,100 rows, and 43 columns. The dataset page separately lists 8.12 GB total file size; the scopes are not reconciled.
- **[Verified fact — global schema only]** `/rows?config=episodes&split=test&offset=0&length=5` returned the first five rows from an unrelated `communication` condition. Its feature schema includes the fields needed by the pipeline, including `run_id`, `condition_id`, `sequence_id`, `evaluation_episode`, `is_warmup`, task IDs, verdicts, `bob_task_correct`, peer-script settings, `agreement`, and nested `communication` events. This confirms global field names and representation only; it does not validate the selected arms or their values.
- **[Pre-outcome design amendment A1]** The global schema also includes `controlled_message_generation_failed`. The frozen pipeline now requires this field to be false on every selected episode; any true value stops analysis rather than silently excluding rows. The addition is recorded in `research/experimental_design.md` and in the config; it does not use selected-arm outcomes.
- **[Test result]** After adding A1 and episode-index descriptive summaries, all **12 synthetic tests passed**. This remains software validation, not a dataset result.

## Retrieval/filter failures

- Exact-condition requests to the datasets-server `/filter` endpoint returned `Parameter 'where' contains errors or invalid symbols` for both frozen condition IDs.
- A numeric `sequence_id=1` filter attempt returned **502 Bad Gateway**.
- The remote `/rows` endpoint was accessible for a tiny unrelated sample, but returns full verbose communication content; no selected-arm rows were successfully filtered and saved locally.
- The `/parquet` endpoint exposes shard URLs and metadata, but the binary Parquet shards were not obtained in this workspace. No local `data/episodes/` input exists.

These failures block row-level validation. Dataset metadata and an unrelated schema sample are not substitutes for the selected trace records.

## Frozen gate status

| Gate | Status | Evidence |
|---|---|---|
| Obtain only the `episodes` Parquet config | **Blocked** | No local file; metadata endpoints only |
| Confirm global required column names | **Partially passed** | Schema from five unrelated rows |
| Validate selected-arm required values and A1 generation-failure flag | **Not checked** | No selected episode rows |
| Validate 10 ordered episodes/run and one run per sequence/arm | **Not checked** | No local selected rows |
| Verify matching task signatures and at least 40 complete sequence blocks | **Not checked** | No local selected rows |
| Compute paired outcomes or grouped classifier metrics | **Not run** | Pre-analysis gates not passed |

## Remaining / next action

Provide the `episodes` Parquet shard files (the metadata-only total is about 15.98 MB) in the ignored local directory `data/episodes/`, or make a permitted retrieval route available. Do **not** fetch the full 8.12 GB release. Once the file is present, run the pre-analysis validation first:

```bash
.venv/bin/python -m analysis.peer_intervention_audit \
  --input data/episodes \
  --config configs/controlled_peer_audit.json \
  --output-dir outputs/controlled-peer-audit
```

The current analysis entry point stops on an integrity failure or fewer than 40 complete sequence pairs before producing outcome summaries. If a gate fails, retain the validation report and document the failure; do not tune, substitute conditions, or proceed to outcome comparisons.

## Sources

- [Dataset-server size metadata](https://datasets-server.huggingface.co/size?dataset=SALT-NLP%2Fagent-collusion)
- [Dataset-server Parquet shard metadata](https://datasets-server.huggingface.co/parquet?dataset=SALT-NLP%2Fagent-collusion)
- [Dataset-server episode rows (unrelated sample, offsets 0–4)](https://datasets-server.huggingface.co/rows?dataset=SALT-NLP%2Fagent-collusion&config=episodes&split=test&offset=0&length=5)
- [Dataset viewer filter documentation](https://huggingface.co/docs/dataset-viewer/filter)

## Code-review follow-up — 2026-10-25

- **[Test result]** Recreated the locked Python environment and ran `python -m unittest discover -s tests -v`: **16 synthetic tests passed**. `ruff check analysis tests`, compilation, and config JSON validation also pass after cleanup.
- **[Code correction]** A text-classifier view that cannot be fitted (for example, an empty Alice-message vocabulary) is now recorded as `not_run` without suppressing the primary outcome or other classifier views. Pre-analysis validation stops now write a diagnostic `validation_report.json` and `run.log`, including row context where available.
- These changes are software-only; the selected SALT data gate remains blocked and no empirical result has been computed.

## Data-gate update — 2026-10-26

- **[Verified fact — local data]** The `episodes` Parquet config was downloaded locally into ignored `data/episodes/`: 53 shards, 15,976,423 bytes total, 27,100 rows, 43 columns — exactly matching the Oct 18 metadata above. The obtain-only-`episodes` gate is now **passed**. The full 8.12 GB release was not fetched.
- **[Gate result]** The first run with the frozen v1.0 config stopped under A1: violating arm, sequence 22, episode 7 has `controlled_message_generation_failed = true` and contains no Bob messages (intervention not delivered). Stopped-run artifacts (`validation_report.json`, `run.log`, protocol config, input manifest with SHA-256 hashes) are retained. No outcome summaries were produced.
- **[Metadata-only census]** Reading only ID/integrity columns for the 1,000 selected rows: compliant 500 rows / 0 generation failures; violating 500 rows / 1 failure (sequence 22, episode 7, run `controlled_peer__gemini-3-7-flash__summary--accept--full-feedback__rep022`); 49 sequences have 10 rows per arm with zero failures (upper bound on complete pairs before task-signature pairing).
- **[Amendment A3]** Recorded in `research/experimental_design.md` before any outcome summaries, contrasts, or classifiers: under the separate config `configs/controlled_peer_audit_a3.json`, a generation-failed run is invalid and its whole sequence pair is excluded, enumerated in `validation.generation_failure_exclusions`; the frozen minimum of 40 complete pairs still applies. The diagnostic-viewing disclosure for the sequence-22 run is recorded in A3.
- **[Not yet verified]** Selected-arm field values beyond the gate stop, task-signature matching, the final complete-pair count, paired outcomes, and classifiers all await the single amended run. If complete pairs fall below 40, the audit stops again with no outcome summaries. Do not re-run with further changes without a new dated amendment.
