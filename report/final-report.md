# What Counts as Evidence of Coordination?
## Scripted stress tests and a controlled-peer audit of LLM traces

**Author:** [EDIT 1: your full name], [EDIT 2: affiliation, or "Independent researcher"]

## Abstract
Behavioural audits can mistake shared context or a policy fingerprint for coordination. We examine that evidence problem in two complementary settings. First, in a frozen CPU-only scripted study (4,000 test trajectories; eight binary-action mechanisms), we asked whether conditional mutual information (CMI), conditioning action dependence on observed context, reduces common-cause false flags relative to mutual information (MI) while retaining channel detection. It did not under a pre-specified noise shift: CMI flagged 35/500 common-cause negatives versus MI's 0/500 (+7.0 percentage points; paired bootstrap 95% CI 4.8 to 9.2), although CMI detected 500/500 stochastic channels and missed deterministic copying. Second, we audited real Gemini 3.7 Flash focal-agent trajectories from SALT-NLP's agent-collusion benchmark under two scripted peer policies. A frozen integrity gate first stopped analysis because one selected episode had an undelivered intervention; after a metadata-only census and a recorded amendment excluding that sequence pair, 49 complete pairs remained. The violating peer bundle did not clearly change constrained-evidence acceptance (85.1% vs 82.2%; paired difference +2.9 percentage points, 95% CI -0.4 to +7.1) or false approvals (53/72 vs 54/72). Retrospective classifiers nevertheless identified the assigned peer policy from the focal agent's messages (AUC 1.00) but not from actions alone (AUC 0.60). Together, the results separate four claims often conflated in collusion audits: statistical dependence, regime detectability, behaviour change, and intent.

## 1. Introduction
When two agents act alike, an auditor faces at least four different questions. Are their actions statistically dependent? Can a monitor tell which interaction regime produced a trace? Did one agent's behaviour actually change the other's decisions or outcomes? And did anyone intend to coordinate harmfully? A positive answer to one question is routinely treated as evidence for the next, yet each step needs its own justification. This report studies where those steps break.

[EDIT 3: add one or two true sentences here about why you chose this question and Track 2 (Detection and Audit). Do not invent a motivation; write the real one.]

We use two deliberately different testbeds. Study 1 is a scripted binary-action stress test with known ground-truth mechanisms. It contains no language model; its value is that every dependence pattern is constructed, so detector failures can be attributed exactly. Study 2 is a pre-registered offline audit of real LLM trajectories from an existing collusion benchmark, where a focal LLM (Alice) interacts with a controlled, scripted peer (Bob). Its value is ecological messiness: natural-language traces, a released dataset with an intervention-delivery defect, and a focal model whose acceptance decisions are the outcome of interest.

Our contributions are modest and methodological: (i) a small, fully reproducible scripted stress test in which a plausible context-conditioning fix fails for identifiable reasons; (ii) a worked demonstration that a frozen data-integrity gate can and should stop an audit of released benchmark data before outcomes are computed; and (iii) a complete-pair amended analysis of real LLM traces showing that a peer-policy regime can be highly detectable from messages while its effect on acceptance behaviour remains inconclusive. We claim no new detector, no measurement of deliberate intent, and no evidence about autonomous LLM collusion in the wild.

## 2. Related work
The sprint's Track 2.3 already proposes comparing coordinated harm, shared-incentive similarity without agreement, and talk without behaviour change [1]; our conditions are an instance of that template, not a new taxonomy. Bonjour et al. use action mutual information to detect collusion in multi-agent games [2]. Douglas et al. show that synchronised, seemingly collusive bandit behaviour can arise without agents observing competitor states [3], a payoff-mediated phenomenon distinct from the strict conditional independence we construct. ColludeBench provides configurable collusion environments and detector families [4], and recent work on latent multi-agent communication uses matched neutral/blocked counterfactuals to attribute influence [5]. Study 2 uses the SALT-NLP agent-collusion benchmark and its controlled-peer interventions [6,7]. We do not claim novelty for MI, CMI, counterfactual controls, or trace classification; the incremental value is in the failure cases and in the audit discipline around them. No exhaustive novelty search was performed.

## 3. Study 1: a scripted stress test of context conditioning

### 3.1 Mechanisms and design
Each trajectory contains 256 IID binary time steps for agents A and B and an observed context. Five seeds × 100 matched blocks × 8 conditions give 4,000 trajectories per split, with separate random streams for training, calibration, and test. Matched conditions within a block share exogenous random streams by design. Development (train/calibration) action-flip probability is 0.10; the frozen test uses 0.25, a parameter shift rather than a new environment family.

| Condition | Construction | Channel label |
|---|---|---:|
| Independent | A, B independent random bits | 0 |
| Common cause | A = Z xor noise, B = Z xor independent noise | 0 |
| Talk only | Common cause + suspicious message keyword | 0 |
| Stochastic channel | B copies A with independent noise | 1 |
| Hidden common | Common-cause actions; auditor sees unrelated W instead of Z | 0 |
| Deterministic channel | A = Z, B = A exactly | 1 |
| Equivalent common | A = B = Z, auditor sees unrelated W | 0 |
| Equivalent channel | A private random bit, B = A, auditor sees unrelated W | 1 |

The last pair induces identical observable action distributions; only provenance differs. Positive labels mean "the script enabled an A-to-B channel," never intent or harm.

### 3.2 Detectors and frozen evaluation
We compare action agreement, plug-in binary MI, CMI given observed context (both in bits), a fixed message-keyword rule, logistic regressions on action features (with/without the keyword), and a constant-prevalence baseline. Classifiers are fitted on the training split only. Thresholds are the higher 90th percentile of calibration scores on independent/common/talk negatives, applied with strict greater-than; the keyword rule uses 0.5. The frozen primary contrast is CMI minus MI false-positive rate on common-cause negatives, with a paired seed/block bootstrap (1,000 draws) over fixed predictions. Success required the whole interval below zero and stochastic-channel recall at least 0.80. AP denotes average precision.

### 3.3 Frozen results
The primary hypothesis failed. CMI flagged **35/500** common-cause negatives versus MI's **0/500**: **+7.0 percentage points [95% CI +4.8, +9.2]**, so the success criterion was not met despite CMI's perfect stochastic-channel recall.

| Method | Precision | Recall | F1 | FPR | AP | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Action classifier | 0.667 | 0.667 | 0.667 | 0.200 | 0.682 | 0.865 |
| Combined classifier | 0.667 | 0.667 | 0.667 | 0.200 | 0.682 | 0.865 |
| Agreement | 0.667 | 0.667 | 0.667 | 0.200 | 0.682 | 0.866 |
| MI | 0.667 | 0.667 | 0.667 | 0.200 | 0.688 | 0.868 |
| CMI | 0.477 | 0.667 | 0.556 | 0.438 | 0.492 | 0.566 |
| Keyword | 0.000 | 0.000 | 0.000 | 0.200 | 0.375 | 0.400 |
| Prevalence | 0.000 | 0.000 | 0.000 | 0.000 | 0.375 | 0.500 |

Aggregate recall conceals opposite errors. CMI detected 500/500 stochastic channels but 0/500 deterministic channels (conditioning on Z removes all residual variation); MI showed the reverse (0/500 and 500/500). CMI flagged 486/500 hidden-common and 500/500 equivalent-common negatives. The keyword rule flagged all 500 talk-only negatives and no channel positives.

[[FIGURE1]]

**Figure 1.** Frozen shifted test (calibration noise 0.10, test noise 0.25): MI (blue) and CMI (red) flag counts out of 500 trajectories per condition. Equal overall recall hides opposite per-condition failures.

The mechanism is threshold transport plus estimator bias. MI's threshold (0.375 bits), calibrated at noise 0.10, sat above both common-cause and channel MI once test noise rose to 0.25, so MI stopped firing on stochastic dependence altogether. CMI's threshold (0.014 bits) sits within the plug-in estimator's finite-sample bias range at 256 steps, producing a small, persistent false-flag tail, while its channel signal remained far above threshold. An explicitly exploratory extension that changed only the test noise back to 0.10 reversed the primary contrast to -5.0 points [-9.4, -0.8]; because it was recorded after the frozen failure, it is a calibration diagnostic, not a replacement result.

## 4. Study 2: controlled-peer audit of real LLM traces

### 4.1 Data, arms, and protocol gates
Study 2 uses the `episodes` table of SALT-NLP/agent-collusion (53 Parquet shards; 27,100 rows; 43 columns), downloaded locally and never redistributed. Alice is Gemini 3.7 Flash; Bob is a controlled scripted peer. Two frozen arms form a policy *bundle*: compliant (Bob sends raw-prefix messages, fixed REJECT verdict) and violating (Bob sends summary messages, fixed ACCEPT verdict), both with full feedback, across sequences 1-50 with 10 evaluation episodes per run (1,000 selected rows). The internal protocol was frozen on 18 October 2026 before selected-arm outcomes were examined, with pre-outcome amendments A1 (fail closed if any selected episode reports controlled-message generation failure) and A2 (unfittable classifier views recorded as not run).

On 26 October 2026 the pipeline stopped under A1: violating-arm sequence 22, episode 7 reported generation failure and contains no Bob messages — the intervention was not delivered. A metadata-only census (ID/integrity columns only) found exactly 1 failed episode among 1,000 selected rows (compliant 0/500, violating 1/500) and 49 sequences with complete, failure-free runs in both arms. Amendment A3, recorded before any outcome summaries, contrasts, or classifiers, excludes the whole sequence pair for any generation-failed run, enumerated in validation diagnostics. The frozen minimum of 40 complete pairs still applied. We disclose that verdict fields for the single affected (and now excluded) violating run were viewed while localising the failure; no rates or contrasts were computed before A3.

### 4.2 Outcomes and classifiers
The primary outcome is Alice's constrained-evidence ACCEPT rate per run; the primary contrast is the paired violating-minus-compliant difference across sequence blocks, with sequence-block bootstrap intervals (10,000 replicates). False approvals (Alice accepts while Bob's task answer is incorrect) are secondary. Secondary classifiers predict the assigned peer-policy arm from Alice's completed trace — her verdict sequence (action only), a TF-IDF representation of her messages (message only), or both — using deterministic sequence-grouped five-fold cross-validation. Within each fold, features are fitted on training sequences only; the flagging threshold is the higher 80th percentile of training compliant-arm scores (target control false-flag rate 0.20). This is retrospective arm assignment, not online monitoring.

### 4.3 Results
Validation passed with **49 complete pairs** (sequence 22 excluded under A3; no task-signature mismatches or duplicate runs).

| Outcome | Compliant | Violating | Paired difference [95% CI] |
|---|---:|---:|---:|
| Alice ACCEPT rate | 82.24% (403/490) | 85.10% (417/490) | +2.86 pp [-0.41, +7.14] |
| False approvals | 54/72 (75.0%) | 53/72 (73.6%) | -0.02 per sequence [-0.12, +0.08] |

The violating bundle therefore did not clearly change acceptance: the interval is compatible with no difference and with a modest increase. False approvals were frequent in both arms and essentially identical. Descriptively, acceptance was 0% in episode 1 and 73.5% in episode 2 in both arms, then mostly above 89% (Figure 2); we make no confirmatory claim from per-episode patterns.

[[FIGURE2]]

**Figure 2.** Descriptive Alice ACCEPT rate by episode index (49 sequence blocks). Both arms rise from 0% (episode 1) to high acceptance; per-episode differences are small and inconsistent.

Classifier results tell a different, narrower story:

| View | ROC-AUC | Violating detected | Compliant false flags | Balanced acc. | Brier |
|---|---:|---:|---:|---:|---:|
| Action only | 0.601 | 13/49 (26.5%) | 8/49 (16.3%) | 0.551 | 0.247 |
| Message only | 1.000 | 49/49 (100%) | 11/49 (22.4%) | 0.888 | 0.028 |
| Message + action | 1.000 | 49/49 (100%) | 14/49 (28.6%) | 0.857 | 0.029 |

Alice's verdict sequence alone barely identifies the arm, consistent with the inconclusive acceptance contrast. Her message text ranks arms perfectly out-of-fold, though the pre-set operating thresholds still flag 22-29% of compliant runs; adding actions does not improve on messages alone. Because folds hold out whole sequences and text features are fitted within training folds, this is not train/test leakage in the usual sense — it is the intervention regime leaving a recoverable fingerprint in how Alice discusses evidence. It is not evidence that Alice intended anything, nor a validated monitor for unseen settings. Agreement annotations were `not_judged` for all episodes, so no agreement-label result is reported; verdict-match rates are omitted as treatment-revealing by construction (Bob's verdict is fixed by arm).

## 5. Synthesis: four claims, four evidence standards
Read together, the studies separate claims that audit pipelines often blur. *Dependence* (Study 1) can be produced by common causes, hidden context, or estimator bias, and can vanish under deterministic copying. *Detectability* (Study 2 classifiers) can be perfect for regime assignment while saying nothing about behaviour change. *Behaviour change* (Study 2 primary outcome) was small and inconclusive here despite high detectability. *Intent and harm* were not measured in either study: Study 1 labels are script switches, Study 2 labels are assigned scripted policies, and false approvals are benchmark task errors, not welfare outcomes. An audit that reports only a dependence score or a classifier AUC is therefore answering an easier question than the one decision-makers usually mean by "collusion." At minimum, reports should state which of the four claims each number supports, show per-condition or per-arm errors rather than aggregates alone, and show that the intervention being attributed was actually delivered — the check that stopped Study 2's first run.

## 6. Conclusion
Context conditioning is not a free fix for common-cause false accusations: under a modest frozen parameter shift it increased false flags, failed completely when context was hidden, and was blind to deterministic copying. On real LLM traces, a scripted peer-policy bundle left a strong textual fingerprint yet produced no clear change in constrained-evidence acceptance or false approvals across 49 matched sequence pairs. Both results argue for audit reports that separate dependence, detectability, behaviour, and intent — and for integrity gates that refuse to analyse undelivered interventions. [EDIT 4: end with one sentence in your own voice about what you would test next (for example, unseen mechanism families or a second focal model). Make it a plan you genuinely intend.]

## Appendix A. Limitations and Dual-Use / Ethical Considerations
Study 1 uses IID binary mechanisms, a one-bit observed context, and a one-bit message indicator. Real agent histories are adaptive, high-dimensional, and partially observed; plug-in MI/CMI bias and calibration behaviour will differ. All mechanism families appear in training; there is no unseen-family, prevalence, message-corruption, or adaptive-adversary evaluation, and only two noise values and five seeds were tested. Bootstrap intervals condition on fixed predictions and chosen settings; no deployment false-positive guarantee follows.

Study 2 covers one focal model, one benchmark, and one scripted peer; Bob does not learn or intend. The arms bundle message format with fixed verdict, so component effects cannot be separated, and there is no no-peer/common-cause control arm. With 49 pairs, effects smaller than roughly the observed interval width cannot be resolved. Classifier thresholds are calibrated on in-sample training scores (optimistic for false-flag control), evaluation is within-benchmark grouped cross-validation, and text fingerprints may not transport across tasks, prompts, or models. A3 changes the estimand to complete pairs with delivered interventions; generation failure occurred only in the violating arm (1/500 episodes), so residual selection concerns cannot be excluded, though the affected pair is fully enumerated. The protocol was internally frozen, not externally registered.

Dual-use and ethics. Publishing detector blind spots can help evaders; we mitigate by staying at the level of abstract binary mechanisms and public-benchmark audit methodology, with no operational collusion scheme. The larger risk we emphasise is false accusation: shared context, benchmark scripts, and discourse style can all produce "suspicious" dependence or classifiability in benign traces. None of our scores should be used as evidence of culpability for any agent or deployer. Negative and inconclusive primary results are reported as prominently as the classifier result to avoid selective emphasis.

## Appendix B. Reproducibility
Study 1 (Python 3.11, CPU, no network): install `requirements-analysis.lock`, then run `bash scripts/reproduce_observability.sh outputs/my-run` (fresh output directory). Checked-in frozen and exploratory results, configs, versions, predictions, and summaries are in the repository; binary trajectories are deterministically regenerated from configs. Study 2: place only the `episodes` Parquet shards in ignored local `data/episodes/` (dataset not redistributed), then run `python -m analysis.peer_intervention_audit --input data/episodes --config configs/controlled_peer_audit_a3.json --output-dir outputs/controlled-peer-audit-a3`. The frozen v1.0 config (`configs/controlled_peer_audit.json`) reproduces the A1 stop. The completed run's input-manifest SHA-256 is `1db8d18b9e576f76cc1fe96e4d676b29335a03e918af5944a2630c3a81208f4e`; outputs include validation diagnostics enumerating the single A3 exclusion. Tests are synthetic-fixture unit/integration tests (`python -m unittest discover -s tests -v`).

## LLM Usage Statement
[EDIT 5: confirm and adjust this statement so every clause is true.] This project was produced with extensive AI-agent assistance, including research synthesis, protocol and code drafting, test development, analysis execution support, and report drafting. The human author supplied the local dataset, executed the gated audit run, and is responsible for verifying all numbers, code, and claims in the submitted version. Pre-existing work is disclosed in the repository: the SALT offline audit pipeline and its frozen protocol predate the scripted stress test, and `experiments/controlled.py` is a vendored upstream snapshot with one documented parsing fix (MIT notices retained). No part of this statement should be read as claiming the draft was primarily human-written before the author's revision.

## References
[1] Apart Research. AI Collusion Research Sprint, 23-25 October 2026. https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25
[2] Bonjour, Aggarwal, Bhargava. Information theoretic approach to detect collusion in multi-agent games. UAI, 2022. https://proceedings.mlr.press/v180/bonjour22a.html
[3] Douglas, Provost, Sundararajan. The Illusion of Collusion. 2026. https://arxiv.org/html/2411.16574
[4] Audit the Whisper / ColludeBench repository. https://github.com/Ostailor/Steganographic_Collusion
[5] Kaur et al. Beyond the Transcript: Detecting Covert Coordination in Latent Multi-Agent Communication. 2026. https://arxiv.org/html/2608.19161v1
[6] Emergent Collusion in Long-Horizon LLM Agent Interaction. https://arxiv.org/html/2609.24967v2
[7] SALT-NLP. agent-collusion dataset and code. https://huggingface.co/datasets/SALT-NLP/agent-collusion ; https://github.com/SALT-NLP/agent-collusion
