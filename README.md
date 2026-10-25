# Behavioral audit signals under shared context

A CPU-only, Rs 0 scripted stress test for the Apart AI Collusion Research Sprint.
**This is not a validated LLM collusion/intent detector. The frozen primary hypothesis failed.**

## Main finding

On the frozen parameter-shift test, context-conditioned MI (CMI) produced 35/500 common-cause false flags versus MI's 0/500: **+7 percentage points**, paired block-bootstrap 95% CI **[+4.8,+9.2]**. CMI detected 500/500 stochastic channels but missed 500/500 deterministic channels; MI showed the opposite pattern on those two conditions. Hidden context caused substantial CMI false alarms. Overall metrics alone conceal these distinct errors.

An explicitly exploratory same-distribution extension reverses the common-cause contrast to −5 points. It does not replace the frozen result. All results are scripted mechanisms, not real LLM behavior, intent or measured real-world harm.

## Reproduce (Python 3.11, CPU)

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-analysis.lock
bash scripts/reproduce_observability.sh outputs/my-fresh-run
```

The output directory must be fresh. Runtime on this sandbox was a few seconds after installation; hardware-dependent. No network is used by the study itself. Installing dependencies requires package access.

```bash
# Exploratory calibration-shift diagnostic
python -m analysis.observability_study \
  --config configs/observability_same_distribution.json \
  --output outputs/my-extension
# Rebuild report/figure/metrics from checked-in results
python scripts/build_study_report.py
# Optional draft PDF rendering
python -m pip install -r requirements-report.txt
python scripts/build_study_report.py
```

## Artifacts

- [Study report](report/study.md) and [reading PDF draft](report/study-draft.pdf)
- [Frozen protocol](research/scripted_design.md), [extension plan](research/extension_plan.md)
- [Validation log](research/validation_log.md), [results interpretation](research/results_analysis.md)
- `results/observability-v1/`: original config, versions, per-trajectory feature records, predictions, summary
- `results/observability-extension/`: separately labeled exploratory run
- `results/metrics.csv`, [error plot](figures/observability_errors.svg)
- [Submission handoff](report/submission_checklist.md)

Binary time-step arrays are deterministically regenerated from recorded configs; CSVs contain features, not full arrays. Thresholds are calibrated before evaluating test metrics. Bootstrap intervals resample matched blocks conditional on fitted predictions, not model retraining. AP is average precision, not trapezoidal PR-AUC.

## Provenance and preexisting work

The SALT-NLP offline peer-policy audit in `analysis/peer_intervention_audit.py`, its config/tests and research records **preexisted this new scripted study**. That separate audit remains blocked on obtaining/validating local real-data episodes. Its results are not used here. See [analysis instructions](analysis/README.md).

`experiments/controlled.py` is an upstream SALT snapshot with a fenced-JSON parsing fix; it is not a standalone runnable experiment harness here. Its upstream imports are absent. See [provenance and MIT license](experiments/README.md).

The new scripted study was designed/implemented/run on October 25, 2026 with extensive AI-agent assistance. The final human author must inspect and understand the code and results, supply confirmed authorship details, and revise the report. No automatic submission occurred. Historical audits are preserved and explicitly distinguished from current-source rechecks.

## Scope and gaps

No real-LLM validation, unseen environment-family test, prevalence sweep, realistic text monitor, full benchmark-native detector comparison, or deployment-FPR guarantee. A fresh virtual-environment reproduction passed; no clean-container reproduction was performed. See the report for dual-use and false-accusation risks. Root original-work licensing has not been assigned; upstream licensed code retains its notices. Do not assume a blanket reuse license.
