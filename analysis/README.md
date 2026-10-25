# Offline controlled-peer audit

This implementation follows the internal protocol in `research/experimental_design.md` and config in `configs/controlled_peer_audit.json`.

## Scope

- Reads only a **local** SALT-NLP `episodes` Parquet export (or JSON/JSONL rows); it does not download anything or call a model/API.
- Uses only the two frozen `controlled_peer` condition IDs. It validates configuration, episode counts, sequence pairing, task IDs, peer-script fields, and the A1 no-generation-failure gate before analysis.
- Primary summary is Alice's **constrained-evidence ACCEPT rate** by arm and a sequence-blocked paired difference. False approvals are reported separately.
- Secondary logistic-regression classifiers predict the scripted peer-policy arm from Alice-authored messages, Alice's verdict sequence, or both. This is retrospective arm classification, not online monitoring or an intent detector. If one view cannot be fit (for example, no usable message vocabulary), it is recorded as `not_run`; primary outcomes and other valid views continue.
- Synchronization is descriptive. Action MI/CMI is not treated as an inferential baseline because the controlled peer's verdict is fixed within arm. The selected arms are not a no-peer/common-cause control.

## Install and run

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-analysis.lock
```

Place the **episodes Parquet config only** under an ignored local directory, for example `data/episodes/`, then run:

```bash
python -m analysis.peer_intervention_audit \
  --input data/episodes \
  --config configs/controlled_peer_audit.json \
  --output-dir outputs/controlled-peer-audit
```

The tool supports a Parquet file/directory and local JSON/JSONL for test fixtures. A fresh, empty output directory is required. Expected artifacts are `validation_report.json`, `input_manifest.json` (with SHA-256 hashes), `protocol_config.json`, `run_level.csv`, `paired_differences.csv`, `episode_index_acceptance.csv` (sequence-block bootstrap intervals), `classifier_oof_predictions.csv`, `summary.json`, `paired_acceptance_differences.svg`, `episode_acceptance_by_index.svg`, and `run.log`. Validation-gate failures also write a diagnostic report and stopped-run log, without outcome summaries. Raw conversation text is not copied to outputs.

## Tests

```bash
python -m unittest discover -s tests -v
```

Tests use synthetic fixtures only. They do not claim dataset results. Before any real-data analysis, the program must pass its validation gates on the local table; missing pairs or required fields stop the confirmatory analysis.

For local lint/format checks, install the developer-only pin and run:

```bash
python -m pip install -r requirements-dev.txt
python -m ruff format --check analysis tests
python -m ruff check analysis tests
```

The GitHub Actions workflow runs these checks and the synthetic test suite on pushes and pull requests.
