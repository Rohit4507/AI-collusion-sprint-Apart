# Validation log — 2026-10-25

## Completed checks

- **[Verified fact — execution]** Installed requirements-analysis.lock and developer Ruff in ignored `.venv`.
- **[Experimental observation]** Four new unit tests passed before first full study: independent/copy MI, conditional-zero control, stochastic common-cause/channel distinction, deterministic generation and metric denominators.
- **[Experimental observation]** Main frozen run: 12,000 trajectory-feature records (4,000 per split), 28,000 final prediction rows (seven models), original primary failure preserved. Command: `python -m analysis.observability_study --output results/observability-v1`.
- **[Experimental observation]** Exploratory extension recorded in extension_plan.md before execution; only held-out noise changed. Saved separately under results/observability-extension.
- **[Experimental observation]** Added save/reload/fresh-output integration test. Full suite: **39 tests passed**, including existing SALT and fenced-JSON tests. No network/model/data calls in synthetic tests.
- **[Experimental observation]** CLI rerun into outputs/observability-reproduction matched trajectories.csv, predictions.csv, config.json and versions.json exactly.
- **[Experimental observation]** Created a separate fresh virtual environment outputs/reproduction-env, installed requirements-analysis.lock, ran all 39 tests successfully, and reran main into outputs/clean-reproduction. Same four deterministic artifacts matched byte-for-byte. Runtime is deliberately not compared. This is fresh-environment verification, not independent human replication or a clean-container test.
- **[Experimental observation]** `ruff check analysis tests`, `ruff format --check analysis tests`, and `git diff --check` passed after code formatting/import cleanup. Main numerical artifacts were reproduced after formatting.
- **[Verified fact — artifacts]** Report, SVG and metrics CSV generated from saved result files by scripts/build_study_report.py. Optional PDF uses requirements-report.txt. PDF is a reading draft, not an assertion of official-template compliance.

## Not verified / not completed

- **[Not verified]** No real LLM trajectories generated or analyzed; SALT data gate remains blocked.
- **[Not verified]** No benchmark-native exact Bonjour/Colosseum/ColludeBench detector reproduction. MI/CMI here are generic discrete plug-in estimators, not claimed exact replications.
- **[Not verified]** No human-independent verification, real-world harm validity, hidden-intent ground truth, adaptive-history estimator validation, unseen environment families, message-noise or prevalence sweep.
- **[Not verified]** No competition submission transaction, author identity/affiliation confirmation, official-template finalization or blanket original-code license assignment.
- **[Statistical interpretation]** These limitations restrict completion to the stated scripted study, not every ambition of the original multi-phase proposal.
