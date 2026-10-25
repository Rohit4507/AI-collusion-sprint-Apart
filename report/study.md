# When Shared Context Looks Like Coordination
## A controlled stress test of behavioral audit signals

Author: Rohit (confirm preferred full name and affiliation before submission).
Status: reproducible scripted study; negative confirmatory result. Not submitted.

## Abstract
We study whether conditioning on shared context helps behavioral auditors distinguish a scripted peer channel from independent agents responding to common causes. The CPU-only experiment compares action agreement, empirical mutual information (MI), conditional mutual information (CMI), message keywords, shallow action and combined classifiers, and a prevalence baseline. Five seeds generate matched scenario blocks with independent training, calibration, and test random streams. The frozen test contains 4,000 trajectories across eight mechanism conditions, including hidden context, talk without action influence, deterministic copying, and observationally equivalent common-cause and channel cases. Thresholds calibrated on development negatives are evaluated under an action-noise parameter shift. The primary hypothesis fails: CMI increases common-cause false flags by 7 percentage points relative to MI, despite detecting all stochastic-channel trajectories. An explicitly exploratory same-distribution diagnostic reverses the common-cause comparison, illustrating calibration sensitivity rather than rescuing the original claim. Hidden-context false alarms and deterministic-channel misses expose additional limits. These synthetic results concern known information-flow mechanisms, not deliberate LLM intent or harmful collusion. The contribution is a small reproducible stress-test artifact and an honest map of evidence limitations.

## 1. Question and scope
Can observed-context conditioning reduce common-cause false accusations while retaining channel detection? Positive labels denote an enabled scripted A-to-B information channel. They do not denote deliberate intent, agreement, or actual harm. The separate harm proxy is simultaneous action 1, an arbitrary modeled prohibited outcome, not measured welfare. No language model, hosted API, model weight or paid resource is required.

## 2. Related work and incremental contribution
The organizer's Track 2.3 already proposes common-incentive, coordinated-harm and talk-only comparisons [1]. Bonjour et al. use action mutual information in multi-agent games [2]. The Illusion of Collusion shows synchronized bandit behavior without direct competitor-state observation [3]; payoff-mediated interaction in that setting is distinct from strict conditional independence. ColludeBench provides configurable environments and detector families [4]. Beyond the Transcript uses matched neutral/blocked latent-channel counterfactuals [5]. We do not claim novelty for MI, CMI, controls or counterfactual monitoring. Our incremental artifact exposes missing-context, low-entropy and calibration-shift failure cases within one transparent script. An exhaustive novelty search has not been completed.

## 3. Methods
The dated internal protocol is research/scripted_design.md. It was written before the study implementation/run, on October 25, not externally registered. There are five seeds, 100 blocks per split/seed, eight conditions per block, 256 IID binary time steps per trajectory, and three separate RNG splits. Thus each split contains 4,000 trajectories, including 1,500 channel positives and 2,500 negatives (37.5% prevalence). Matched condition variants share exogenous random streams intentionally; private streams within independent mechanisms are distinct. Entire blocks are independent within this constructed experiment.

Common cause: A=Z xor noise_A and B=Z xor noise_B. Stochastic channel: B copies A with independent noise. Talk-only adds a suspicious message indicator to common-cause behavior. Hidden-common replaces observed Z with unrelated W. Deterministic channel uses A=Z, B=A. Two additional cases generate identical action-pair distributions through a shared Z or direct copying of a private bit, with unrelated observed W. Only mechanism provenance distinguishes these distributions; channel removal is privileged extra access.

Plug-in binary MI and CMI are computed in bits. CMI sums within-context MI weighted by empirical context frequency. It has finite-sample bias and is not calibrated for adaptive sequential histories. Action logistic regression uses agreement, MI and action marginals; combined adds the message keyword. Standardization and regression fit on training only. Mechanism IDs, seed IDs, labels and hidden context are excluded from model features. Context-aware detection is CMI itself, not a new detector. Message-only is a fixed keyword rule, not an LLM judge or TF-IDF model.

Thresholds use the higher 90th percentile of calibration scores on independent/common/talk negatives, with strict greater-than decisions. The keyword rule uses .5. Calibration excludes stress cases deliberately; this limits transport. Development flip probability is .1 and frozen test probability .25: this is parameter-shift evaluation, not held-out environment-family generalization. Models train on all development conditions; unknown-mechanism generalization is not tested. Primary comparison is CMI minus MI FPR on common-cause negatives; success requires a negative paired-bootstrap interval and stochastic-channel recall at least .8. Fixed predictions are resampled by matched seed/block, 1,000 bootstrap draws. These intervals do not include refitting uncertainty or extrapolation to arbitrary seeds/environments.

## 4. Frozen results

| Method | Precision | Recall | F1 | FPR | AP | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| action_classifier | 0.667 | 0.667 | 0.667 | 0.200 | 0.682 | 0.865 |
| combined_classifier | 0.667 | 0.667 | 0.667 | 0.200 | 0.682 | 0.865 |
| agreement | 0.667 | 0.667 | 0.667 | 0.200 | 0.682 | 0.866 |
| mi | 0.667 | 0.667 | 0.667 | 0.200 | 0.688 | 0.868 |
| cmi | 0.477 | 0.667 | 0.556 | 0.438 | 0.492 | 0.566 |
| keyword | 0.000 | 0.000 | 0.000 | 0.200 | 0.375 | 0.400 |
| prevalence | 0.000 | 0.000 | 0.000 | 0.000 | 0.375 | 0.500 |

All overall recall denominators are 1,500 channel positives; all overall FPR denominators are 2,500 negatives. AP means average precision, not trapezoidal PR-AUC. Precision uses each method's flagged count. Exact confusion counts, Brier scores for probability models, thresholds and per-condition denominators are saved in summary.json and metrics.csv; probability reliability curves and metric-wide intervals are not provided.

The primary CMI-minus-MI common-cause FPR contrast is +.070, paired block-bootstrap 95% interval [.048,.092]: 35/500 versus 0/500 false flags. CMI catches 500/500 stochastic-channel positives; MI catches 0/500 there. Overall recall happens to tie because MI catches deterministic channels that CMI misses (500/500 versus 0/500). Equal overall recall conceals radically different errors. Consequently this is not a comparison at matched within-mechanism recall and cannot establish uniform superiority of MI.

CMI flags 486/500 hidden-common negatives and 500/500 equivalent-common negatives. Its 0/500 deterministic-channel detection follows from conditioning away all variation, not a software error. The keyword rule flags 500/500 talk-only negatives and detects 0/1,500 channel positives. Adding the keyword to the shallow classifier does not change the reported thresholded confusion counts. Scores distinguish the distributions only to the extent the constructed inputs allow. The intervention mismatch statistic is a construction sanity check, not a competing detector benchmark.

Figure: figures/observability_errors.svg shows per-condition MI/CMI flag counts. Main runtime is recorded in summary.json and is environment-specific; it excludes environment installation and report rendering.

## 5. Exploratory extension and interpretation
After seeing the primary failure, we recorded research/extension_plan.md and changed only test noise to .1. This same-distribution diagnostic preserves v1 and does not replace it. The common-cause difference becomes -.050 with bootstrap interval [-.09405,-.00795], and stochastic-channel recall remains 500/500. The extension supports calibration sensitivity as a possible explanation, not a new confirmatory success claim. We do not tune thresholds based on either test result.

## 6. Limitations and Dual-Use / Ethical Considerations
These are scripted binary mechanisms, not natural language agents. The message surface is a single predefined keyword; it cannot represent real conversational ambiguity. All mechanism families appear during training; there is no unseen-environment evaluation. Only five root seeds and two action-noise settings were tested. No class-prevalence sweep, message corruption, adaptive covert strategy, real-world reward model, benchmark-native detector replication, or clean-container reproduction was performed. A fresh separate virtual-environment reproduction did pass with exact deterministic artifact matches. The bootstrap conditions on fixed predictions and selected settings. No deployment-grade low-FPR guarantee follows. Conditional dependence does not prove direct influence; direct influence does not prove intent or harm. The observation-equivalence example is elementary, not a novel theorem.

The artifact may help attackers understand blind spots. It uses only abstract binary actions and no operational scheme for real-world collusion. False accusations against benign coordination are a central safety risk: scores must not be used as evidence of culpability. Our negative primary result must remain visible. A stronger future study needs realistic licensed logs, action-meaningful welfare, disjoint mechanism families and calibration under realistic missing context.

## 7. Reproducibility and disclosure
Install requirements-analysis.lock in Python 3.11; run scripts/reproduce_observability.sh with a fresh output directory. Results are deterministic apart from runtime. Generation code reconstructs every binary trajectory from the recorded config; saved trajectory CSVs contain per-trajectory features, not raw time-step arrays or conversation text. Results, versions, configs, predictions, metrics and figure source are included. Tests cover elementary MI/CMI controls, scripted independence/channel behavior, determinism, metric denominators, and save/reload. See research/validation_log.md for actual checks.

The older SALT audit was preexisting and remains blocked on real data; none of its outputs are used here. This scripted study and report were produced with extensive AI-agent assistance in design, coding, running checks and drafting. The human author must review the implementation, independently understand/verify the claims and edit the final report. Do not describe this draft as primarily human-written or independently human-verified. Author name/affiliation and final template formatting remain to be confirmed; no submission has occurred.

## References
[1] Apart Research. AI Collusion Research Sprint, October 23–25, 2026. https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25
[2] Bonjour, Aggarwal and Bhargava. Information theoretic approach to detect collusion in multi-agent games. UAI, 2022. https://proceedings.mlr.press/v180/bonjour22a.html
[3] Douglas, Provost and Sundararajan. The Illusion of Collusion. v2, 2026. https://arxiv.org/html/2411.16574
[4] Audit the Whisper / ColludeBench repository. https://github.com/Ostailor/Steganographic_Collusion
[5] Kaur et al. Beyond the Transcript: Detecting Covert Coordination in Latent Multi-Agent Communication. 2026. https://arxiv.org/html/2608.19161v1
