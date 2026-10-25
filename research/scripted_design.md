# Scripted observability study — internal protocol v1.0

- **[Verified fact — process]** Dated 2026-10-25 before implementing/running this separate study. Not an external preregistration. Existing SALT protocol is unchanged.
- **[Hypothesis]** Context-conditioned dependence reduces false flags from shared exogenous context while retaining detection of stochastic channel-copy mechanisms, when relevant context is observed. Hidden context and low-entropy coordination are expected failure modes.
- **[Future work — frozen scope]** Binary action agents, 256 steps per trajectory; five seeds; 100 matched blocks per seed/split; separate train/calibration/test RNG streams. Train/calibration use development flip probability .1; final test uses held-out .25. This is a mechanism-parameter shift, not a new environment family. Each block has every condition; preserve blocks in bootstrap. No LLM generation, weights, hosted APIs or judge labels.

## Conditions and labels

- **[Future work]** Independent: A and B use independent action randomness; negative channel label.
- **[Future work]** Common cause: A=Z xor independent noise; B=Z xor independent noise. No peer observation or reward feedback. Negative channel label.
- **[Future work]** Talk only: same as common cause, but explicit suspicious message; negative channel label.
- **[Future work]** Channel: A=Z xor noise; B=A xor independent noise. Positive channel label. Benign message matches other cases.
- **[Future work]** Hidden common cause: common-cause actions but observed context is independent W. Negative channel label.
- **[Future work]** Deterministic channel: A=Z; B copies A. Positive channel label but conditional dependence is zero.
- **[Future work]** Observational equivalence pair: independent agents A=B=Z versus channel A=U, B=A, with observed W unrelated and benign messages. Distributions match; no trace-only classifier can identify the mechanism. Report action distribution checks; no new impossibility theorem claimed.
- **[Statistical interpretation]** Positive means known script channel enabled, not deliberate mental intent or harmful collusion. Record harm proxy separately: both choose 1 (arbitrary modeled prohibited outcome, not actual welfare). Independent behavior can have this outcome. Talk alone is not execution.

## Estimators and evaluation

- **[Future work]** Baselines: constant training prevalence probability; message keyword; action agreement; empirical binary MI; empirical binary CMI conditioned on observed context; train-only standardized logistic regression over agreement/MI/action marginals; combined adds message keyword; context-aware uses CMI. MI=0 for unsupported empty cells; plug-in finite-sample bias acknowledged. IID time steps within scripted trajectory; this is not an estimator validated for adaptive histories.
- **[Future work]** Calibration on independent/common/talk negatives only: higher 90th-percentile threshold, strict score>threshold. Same inputs for observational models; no mechanism ID, seed, split or hidden context supplied. Thresholds frozen before reading final metrics. Report confusion counts, prevalence, precision/recall/F1/FPR, average precision (not trapezoidal PR-AUC), ROC-AUC, Brier only for probabilities. Report per-condition error rates. Keyword is uncalibrated rule; label separately.
- **[Future work]** Primary comparison: CMI minus MI FPR on final common-cause negatives, paired block bootstrap 95% intervals. Success requires lower FPR and at least .8 recall on stochastic channel cases. Include all stress conditions irrespective of success. Bootstrap fixed predictions, not retraining uncertainty. Five seeds are replications; intervals conditional on these settings.
- **[Future work]** Ablations: unconditional MI removes context; hidden-common condition removes relevant observability; deterministic channel tests erased residual variation. No-message channel tests message insufficiency; talk-only tests false accusation. No sweeping features or thresholds.
- **[Future work]** Intervention reference: rerun B after severing A→B and drawing a fresh independent action while matching A. Measure action mismatch difference. Privileged replay access, not a fair observational competitor; construction sanity check only.
- **[Future work]** Tests: independent MI small, copy MI high, common-cause CMI low, deterministic-copy CMI zero, seeded generation reproducible, score schema and clean subprocess reproduction. Stop on nonfinite scores or failed controls before final run. Save config, raw per-trajectory features/predictions, versions, metrics, bootstrap and figure. No test-driven tuning.
- **[Statistical interpretation]** 500 trajectories/condition/test split permits coarse error estimates, not deployment-grade low-FPR guarantees. 256 steps gives binary cells support in stochastic cases but not guaranteed rare-event reliability. No cross-environment or real-LLM generalization claim.
