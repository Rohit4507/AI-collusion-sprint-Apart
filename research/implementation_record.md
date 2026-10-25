# Phase 4 — Offline analysis implementation record

- **Date:** 2026-10-18 (Asia/Calcutta)
- **Scope:** Implementation against the frozen Phase 3 protocol. This phase builds and tests the pipeline; it does not report empirical results.

## Implemented

- `analysis/peer_intervention_audit.py` — local-only loader for Parquet shards or JSON/JSONL; exact-condition filtering; metadata/schema checks; sequence/task matching; run-, paired-sequence, and episode-index outcome summaries; deterministic sequence-block bootstrap intervals; grouped five-fold logistic-regression arm classifiers; SHA-256 input manifest; CSV/JSON/SVG outputs.
- `configs/controlled_peer_audit.json` — machine-readable condition IDs, expected fields, sequence IDs, sample gates, classifier parameters, bootstrap settings, outcome wording, and pre-outcome amendments A1 (no controlled-message-generation failures) and A2 (unusable classifier views are recorded as `not_run`).
- `tests/test_peer_intervention_audit.py` — synthetic unit and end-to-end tests for pairing, missing/mismatched sequences, metadata failure, Parquet/JSONL loading, classifiers, output files, and the minimum-pair stopping gate.
- `analysis/README.md`, `requirements-analysis.txt`, `requirements-analysis.lock`, `requirements-dev.txt`, `.github/workflows/analysis-checks.yml`, and `.gitignore` — run instructions, pinned dependencies, CI lint/test checks, and rules to keep downloaded data/output files out of Git.

The pipeline reports **constrained-evidence ACCEPT**, false approvals, and scripted-peer verdict agreement separately. It does not infer intent. Synchronization is descriptive; action MI/CMI is not reported as a causal detector score for these constant-script arms.

## Validation performed

- **[Test result]** `python -m unittest discover -s tests -v` — **12 tests passed** on synthetic fixtures using Python 3.11.2, PyArrow 21.0.0, and scikit-learn 1.7.2. Tests include sequence-block episode-index summaries and a fail-closed generation-failure gate.
- **[Test result]** The tests verify deterministic grouped processing and output generation, but use no SALT-NLP episode outcomes. They are software tests, not experimental observations.
- **[Not performed]** No SALT-NLP file was downloaded; the real Parquet parser/condition-pair validation has not been run on the release. No benchmark, detector evaluation, model/API call, or experiment has been run.

## Data-access note

**[Verified fact — metadata/schema only]** Hugging Face datasets-server metadata lists the `episodes` Parquet config at 15,976,423 bytes (27,100 rows, 43 columns); the dataset page lists 8.12 GB total file size. These figures cover different scopes and are not reconciled. A remote five-row sample confirms global column names and that `communication` is a list of event records, but those rows are from an unrelated condition and do not verify selected-arm values. It also exposes `controlled_message_generation_failed`, which is now covered by the pre-outcome A1 fail-closed gate. Exact selected-condition `/filter` queries returned an “invalid symbols” error; a numeric filter attempt returned 502. No binary Parquet file was downloaded.

## Remaining gate and next phase

- Obtain only the `episodes` Parquet config into ignored local `data/` storage, or document why it cannot be retrieved separately.
- Run the pipeline’s pre-analysis validation on that real table: required fields, one run per sequence/arm, 10 ordered episodes per run, matching task IDs, and at least 40 complete sequence blocks.
- If the gate passes, Phase 5 can report the pre-registered analysis and held-out classifier outputs. If it fails, stop, report the failure, and amend the protocol before examining arm outcome differences.
- **Current evidence status:** software functionality has been tested on synthetic data; all research outcomes remain unknown.

## Code-review follow-up — 2026-10-25

- **[Test result]** Recreated the pinned Python environment and reran the suite: **16 synthetic tests passed**. `ruff check analysis tests`, compile checks, and config JSON validation pass. Ruff is an ad-hoc developer tool, not part of the runtime lock.
- **[Code correction / A2]** A classifier view that cannot fit (such as empty message vocabulary) is marked `not_run`; primary estimates and other valid views can still be written. Validation stops now persist a diagnostic report and log with row context where possible.
- No selected SALT rows or outcomes were inspected; the real-data gate remains unresolved.
