# Phase 2 — Revalidated novelty and project-selection audit

**Audit date: 2026-10-25 (Asia/Calcutta).** This is a new project-selection recommendation under the actual deadline, not a retrospective claim about what was known on October 18. Historical audit and existing frozen SALT protocol remain preserved below. No detector implementation, model call, dataset download or experiment was performed in this phase. No selected-arm outcomes were inspected.

## Evidence conventions and search scope

- **[Verified fact — source reports]** means the cited source states it; performance is not independently reproduced.
- **[Statistical interpretation]** means reasoning under specified assumptions, not measured performance.
- **[Hypothesis]** marks feasibility/novelty judgments and recommendations.
- **[Not verified]** marks unresolved access, licensing, implementation or evidence.
- **[Future work]** marks proposed work, not a completed experiment.
- **[Verified fact — process]** This recheck read the existing audit, retrieved the sources below and ran one targeted web search: “multi agent collusion detection common cause conditional mutual information matched controls false positives”. This is not an exhaustive systematic review. Search snippets were not treated as replicated results.

## Executive decision

**[Hypothesis]** The broad candidate survives as a *research question*, but fails as a defensible claim of a new detector or a general deliberate-collusion classifier. Under Rs 0, no dependence on proprietary hosted models, and the October 25 deadline, select **C: a narrowly scoped CPU-only scripted identifiability and false-positive stress test** for Phase 3 design. This is a proposed separate study, not a silent change to the existing SALT audit.

**[Hypothesis]** Working title: **When Shared Context Looks Like Coordination: A Controlled Stress Test of Behavioral Audit Signals**. Proposed contribution is an auditable evaluation artifact: observationally matched mechanism cases, a context-observability ladder, and an intervention-based reference. Do not call MI, CMI, matched controls, or residualization themselves new methods. Do not claim this artifact is the first of its kind.

**[Statistical interpretation]** This route trades direct LLM external validity for known mechanism labels and controlled falsification. A result on scripted agents cannot establish detection of deliberate LLM intent, emergent LLM collusion, or deployment-grade false-positive control.

## 1. Closest verified prior art

| Source rechecked on 2026-10-25 | Source-backed overlap | Consequence for our claims |
|---|---|---|
| [Official Track 2.3 Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25) (checked in Phase 1) | **[Verified fact]** Already proposes coordinated harmful action, shared-incentive similarity without agreement, talk without changed behavior, and several evidence types. | **[Hypothesis]** Broad framing and three-way controls are not sufficient novelty. |
| [Bonjour et al., UAI 2022](https://proceedings.mlr.press/v180/bonjour22a.html) | **[Verified fact]** Uses action mutual information for repeated simultaneous games and partially observable sequential games. | **[Hypothesis]** MI is a baseline; exact net-influence replication needs formula/code verification, not renaming ordinary MI. |
| [The Illusion of Collusion, v2](https://arxiv.org/html/2411.16574) | **[Verified fact — source reports]** Context-free bandits without direct competitor-state/action knowledge can develop synchronous, seemingly collusive behavior in repeated Prisoner's Dilemma. | **[Statistical interpretation]** Absence of direct observation does not imply absence of payoff-mediated interaction. Our strict independent null must avoid cross-agent reward feedback, not merely remove messages. |
| [ColludeBench design](https://github.com/Ostailor/Steganographic_Collusion/blob/main/docs/colludebench_design.md) | **[Verified fact]** Describes configurable honest/colluding policies, covert schemes, pricing/auction/review settings and harm indicators. | **[Hypothesis]** A toy honest-vs-colluder generator is not enough novelty. Test observational ambiguity, missing context and generalization explicitly. Specification numbers are not verified outputs. |
| [Beyond the Transcript, v1](https://arxiv.org/html/2608.19161v1) | **[Verified fact — source reports]** Uses neutral/blocked matched latent-channel counterfactuals; explicitly calls exact recovery by replay a sanity check by construction. | **[Hypothesis]** Counterfactual monitoring is established prior art. Our possible difference is a transparent black-box/scripted stress test of missing common causes, not a new causal-monitoring principle. |
| [SPAR project description](https://sparai.org/projects/f26/recDQmFvumFiPhPZs/) | **[Verified fact]** Proposes benign-coordination false positives, implicit actions, and shared-model/incentive explanations. | **[Statistical interpretation]** Proposal overlap is strong; it does not establish completed empirical results or validate its critiques of other benchmarks. |
| [SALT-NLP README](https://github.com/SALT-NLP/agent-collusion) | **[Verified fact]** Already studies controlled peers; compliant raw-prefix/reject and violating summary/accept scripts change both policy components. Existing measurements and ablations target peer influence. | **[Hypothesis]** Recomputing its contrast is a replication/audit, not discovery of peer influence. |

## 2. Evidence and baseline gap matrix

All entries in the final two columns are **[Statistical interpretation]** or **[Future work]**, not experimental observations.

| Evidence class | Existing overlap | What it cannot identify by itself | Proposed comparison |
|---|---|---|---|
| Prevalence / constant score | Standard classification sanity check | Any mechanism or ranking | Training-prevalence probability, all-negative decision and randomized score reference; do not optimize these on test data. |
| Message-only | Official 2.2/2.3, Colosseum communication measures | Execution, harm or action-only channel | Transparent keyword baseline and simple TF-IDF classifier; identical message templates across some positive/negative cases. |
| Action-only | Bonjour; Colosseum outcome measures | Common cause vs direct information flow | Action-frequency features plus shallow classifier; mechanism labels hidden. |
| Similarity / synchronization | Illusion of Collusion | Independent shared-context similarity vs coordination | Raw agreement; include strong benign synchrony and asymmetric coordination. |
| MI / conditional dependence | Bonjour and ColludeBench family | Intent; causation with missing context; many low-entropy coordination mechanisms | Discrete MI and CMI with documented finite-sample support, block-aware null calibration and incomplete-context tests. Do not claim exact Bonjour baseline until implemented from its equations. |
| Combined supervised trajectory features | Standard shallow supervised classification; official message/action comparison | Unknown mechanisms; shortcut-free generalization | Logistic regression with fold-local preprocessing, sequence/scenario-family groups and matched detector inputs. |
| Benchmark-native baseline | ColludeBench detector stack; Colosseum coalition advantage | Transfer to a different environment or label definition | Include only if a licensed executable component accepts our data and assumptions. Otherwise record unavailable/inapplicable, not a counterfeit reimplementation. |
| Common-cause control | Official 2.3; Illusion of Collusion | Unmeasured common causes and payoff-mediated influence | Independent exogenous random streams conditional on fixed common context, no peer observation, no shared private randomness or cross-agent reward feedback. |
| Matched intervention reference | SALT peer interventions; Beyond the Transcript | Subjective intent; deployment feasibility without replay access | Scripted channel cut/replacement under matched exogenous randomness; explicitly report privileged intervention access. |

**[Statistical interpretation]** Harm, communication agreement, causal peer influence and mechanism assignment must be separate labels. Benign coordination can involve real influence; independent harmful behavior can exist without influence. No single binary mechanism label is a complete definition of collusion.

## 3. Four-direction gap/feasibility matrix

Every assessment below is **[Hypothesis]**, conditional on future validation. Data descriptions reference the verified sources above; local execution/access remains unverified unless explicitly noted.

| Direction | Novelty | Importance for AI control | Feasibility before current deadline | Data availability | Rs 0 / compute | Ground truth | Risk | Concrete deliverable |
|---|---|---|---|---|---|---|---|---|
| A. Original candidate: general context-aware collusion detector on LLM workflows | Low broad novelty; specific improvement unproven | High if it works | Low: missing matched independent cases and no validated local generation | Recommended repos exist; adequate raw matched data not established | Local small-model route possible in principle; not verified on 6 GB | Deliberate intent not directly observed | Overclaiming, weak controls, generation failures | Controlled LLM detector comparison only after validated data; not recommended as current scope |
| B. Existing SALT controlled-peer trace audit | Incremental replication/audit | Moderate: intervention integrity and focal behavior | Conditional: pipeline exists, required data still absent locally | Public dataset linked; local selected rows not verified | CPU analysis costs no APIs, but chosen traces originate from proprietary models | Script assignment credible conditional on cache/generation validation; no independence null | Bundled intervention, treatment-revealing features, blocked input | Paired acceptance differences, focal-only arm classifiers, integrity report |
| C. Scripted observability / common-cause stress test | Incremental artifact; precise observability test may add value | Moderate: evidence standards and false accusation | Best bounded engineering scope, but still must pass controls | Generate local scripted data after design freeze | CPU-only; no hosted-model or weight dependency | Structural channel assignment known; subjective intent absent | Synthetic shortcuts, oracle-context advantage, no LLM transfer | Mechanism-matched traces, leakage-tested baseline comparison, missing-context/intervention failure map |
| D. Local-model Dolos red-team audit | Discovery depends on experiments; not established | Potentially useful but less aligned to collusion | Low for this reset: download/inference/discovery unvalidated | Organizer links weights; no local weights verified | Organizer says Rs 0; download/6 GB behavior not tested | Hidden target initially unknown | Open-ended discovery and weak causal explanation | Validated behavior audit if discovered; not primary recommendation |

## 4. Explicit selection rule (not selected by preliminary metrics)

- **[Hypothesis — hard gate 1]** No paid API or proprietary hosted-model dependency in generation or evaluation. For safety, interpret this conservatively: do not use proprietary-origin traces as the main empirical basis without relaxing the constraint. B fails this conservative gate; its existing code remains useful as a separate historical artifact.
- **[Hypothesis — hard gate 2]** Have obtainable data and operational labels before outcome analysis; do not rely on unverified raw-log availability. A currently fails; D has unresolved artifact and target-discovery risk.
- **[Hypothesis — hard gate 3]** A beginner solo participant must be able to explain and CPU-reproduce the complete experiment with time reserved for report/verification. C has the smallest dependency surface.
- **[Hypothesis — ranking after gates]** Prioritize ground-truth credibility and falsifiability, then independent control quality, then bounded engineering, then incremental novelty. No numerical “novelty scores” are invented.
- **[Hypothesis — decision]** C is the primary Phase 3 design recommendation. B stays a separately frozen replication route, not a fallback dataset to substitute after observing C's results. Do not blend its labels or outputs into C.

## 5. Proposed distinguishing stress test and falsification

- **[Future work]** Construct an observationally ambiguous pair. Example: shared hidden Bernoulli Z causes both independent agents to emit Z; in a channel case, agent A emits a private Bernoulli U and agent B copies A. Both yield identical observed action-pair distributions, but different effects under a channel-cut intervention. Match message and outcome surfaces as well if claiming full observed-trace equivalence.
- **[Statistical interpretation]** If the auditor's entire observed distribution is identical across labels, no detector using only those observations can separate the labels above chance at balanced prevalence. This is an elementary identifiability example, not a new impossibility theorem and not a measured result.
- **[Future work]** Add complete, partially observed and hidden common-context conditions. Conditional dependence should work only where its structural assumptions and support hold. Include positives whose coordination is explained by visible context so CMI can also miss genuine information flow.
- **[Future work]** Compare observational detectors under identical inputs. Report a replay/intervention reference separately: privileged access cannot be advertised as fair superiority over a transcript-only baseline.
- **[Future work]** Split complete scenario blocks and keep their matched variants together; hold out generator/scenario families and message templates. Store mechanism metadata separately from detector input. Use independent named RNG streams rather than accidental shared seeds for supposedly independent agents.
- **[Future work]** Define positive/negative controls, error tolerances, primary metric and calibration/test split in Phase 3 before any run. Test false alarms at matched detection budgets, not merely AUROC. Preserve every prespecified seed and failed run.
- **[Future work]** Reject a claim of incremental detector value if the context-aware method does not reduce benign common-cause false flags at the prespecified recall requirement on held-out families, or if gains disappear after template/metadata leakage is removed. If only oracle context works, report conditional validity—not deployable detection.

## 6. Boundary on contribution and current evidence

- **[Verified fact — local inspection]** Existing repository contains a SALT audit and frozen protocol; it does not supply the newly proposed scripted stress-test implementation. No existing result supports the new recommendation empirically.
- **[Not verified]** An exact prior artifact matching the proposed stress test has not been ruled out. No “first”, “state of the art”, real-LLM recall or general collusion-FPR claim is justified.
- **[Hypothesis]** Even a negative result can support a useful submission if it cleanly demonstrates when common-cause conditioning helps, when hidden context destroys identifiability, and what extra audit access is required. Submission strength depends on actual execution, not this plan.
- **[Future work]** Phase 3 must freeze the new study separately and revise the old internal documentation only through dated amendments. Do not backdate this October 25 recommendation or describe it as an external preregistration.

## Phase 2 checklist

- **[Verified fact] Done:** four directions compared; candidate audited against named baseline/evidence classes; decision uses hard constraints, not attractive preliminary metrics; source overlap and synthetic limitations explicit.
- **[Not verified] Failed/remaining:** no validated real-LLM matched-independent dataset within constraints; no benchmark reproduction or novelty-exhaustiveness guarantee.
- **[Verified fact] No detector code or new experimental results produced.**
- **[Future work] Next:** Phase 3, freeze the scripted observability study, A–D mechanism conditions, harmful-outcome labels, exact estimand, sample-size rationale, thresholds, split/seed strategy, ablations and stop rules.

---

## Historical October 18 audit — preserved, not the current selection decision

**[Not verified in this recheck]** Historical citations and numerical claims below were not all freshly inspected. Conflicting feasibility/timing recommendations are superseded by the current audit above; they are retained for provenance, not treated as new evidence.

# Phase 2 — Novelty and gap audit: Detection and Audit

- **Audit date:** 2026-10-18 (Asia/Calcutta)
- **Scope:** Static literature, benchmark, repository, and dataset-page inspection for the Apart Research AI Collusion Sprint. This is a source-backed screening audit, not an exhaustive systematic review. No dataset was downloaded, no code or tests were run, and no model/API calls or experiments were made.

## Evidence labels

- **[Verified fact — source reports]** The linked source states this fact or reports this result. Paper results remain author-reported unless independently reproduced.
- **[Statistical interpretation]** Interpretation of a reported method, result, or sample size.
- **[Hypothesis]** A tentative novelty or project-direction judgement, not an established priority claim.
- **[Not verified]** A license, download, implementation, or result that this audit could not establish.
- **[Experimental observation]** None in this phase; no experiment was run.

## Executive decision

**[Hypothesis] The broad “Collusion or Coincidence?” framing is not a defensible novelty claim by itself.** The official Track 2.3 already asks for evidence distinguishing deliberate coalitions from innocent parallel behaviour, collusive-sounding talk without changed behaviour, and harmful outcomes without agreement [1]. Combining message and action evidence, measuring action dependence, using matched controls, and calibrating false positives each have close prior art [2–10]. A public SPAR project description also names benign-coordination false positives, action-implicit collusion, and shared-model/incentive explanations as its target questions [12]. That is an overlap warning, not evidence that the SPAR project has completed or published results.

**[Hypothesis] A narrow, conditional gap remains as an *evaluation audit*, not as a new detector:** compare the false-positive and miss patterns of message-only, action-only, synchronization/conditional-dependence, and simple supervised trajectory-feature baselines under explicitly matched common-cause nulls and controlled peer-influence conditions. Report peer influence, protocol deviation, and harm as separate outcomes; do not infer mental intent from the detector score. The inspected sources cover the pieces, but I did not find an apples-to-apples black-box comparison of all these evidence classes against both kinds of controls. This is only a provisional gap: the search was not exhaustive, and the SPAR project is unusually close. Do not claim “first,” “novel detector,” or “intent detection.”

**Practical recommendation:** if pursued during the sprint, frame it as a small, reproducible *false-positive stress test / replication extension*. The released long-horizon collusion traces are the most promising no-paid-API starting point, but are large and do not by themselves supply every no-peer/common-cause control needed. Confirm the exact data subset and matched conditions before coding.

## Keep these concepts separate

| Concept | What the evidence can support | What it cannot establish alone |
|---|---|---|
| **Behavioural similarity / synchronization** | Two agents choose similar actions or reach similar outcomes. | Peer communication, causal influence, deliberate agreement, or harmful intent. Independent learners with no access to competitor actions can still synchronize [5]. |
| **Statistical dependence** (correlation, MI, CMI) | Outputs/actions are associated, possibly after conditioning on recorded context. | That one peer caused the other’s behaviour; omitted common causes can remain. The information-theoretic game detector is a dependence-based signal, not an intent test [4]. |
| **Peer influence** | A controlled change to the peer changes the focal agent’s behaviour, under the study’s intervention assumptions. | A general claim about all deployments or the agent’s private intention. The long-horizon study explicitly uses controlled peers to test this narrower causal question [8]. |
| **Communication agreement** | Agents explicitly discuss or agree to a plan. | That they execute it or cause harm. Colosseum reports “collusion on paper” cases where the communication plan does not translate into collusive actions [2]. |
| **Coalition advantage / harmful outcome** | Joint behaviour changes reward, welfare, or a specified task outcome relative to a benchmark. | That the agents intended the outcome or coordinated to produce it. A common model origin can create correlated behaviour without an agreement [6]. |
| **Intent** | At best, an operationally defined interpretation supported by multiple evidence sources and controls. | It is not directly identified from a transcript, action correlation, or classifier score alone. |

**[Statistical interpretation]** For this project, “collusion versus coincidence” should be operationalized as a contrast between (a) a *known peer-influence intervention* and (b) *similar behaviour generated without peer access/influence under shared context or incentives*. A detector score is evidence about that contrast, not proof of subjective intent.

## Prior work by evidence surface and method

### 1. Message-only monitoring

- **[Verified fact — source reports]** Colosseum measures communication-side indications alongside action-based coalition advantage/regret. It explicitly discusses “collusion on paper”: collusive plans in messages need not yield collusive actions [2]. This already motivates combining statements and outcomes; that combination is not a new contribution on its own.
- **[Verified fact — source reports]** NARCBench v3 evaluates activation probes and transcript-level judges. In its steganographic tier, the authors report that a text judge fails to distinguish collusion from control; in a third-party emergent environment, only 2 of 229 collusive episodes verbalize coordination [7]. These are author-reported results, not reproduced here.
- **[Verified fact — source reports]** “Audit the Whisper” proposes transcript-side cross-run MI, permutation, watermark, and fairness-aware signals, calibrated on honest runs; its benchmark includes hosted Gemini/Groq scenarios [3]. Its reported performance is not independently verified in this audit.
- **[Statistical interpretation]** Message-only evidence is useful for explicit agreement, but can miss implicit/action-based influence and can over-flag discussion that is never acted upon. A paid LLM judge is not required for the proposed sprint audit; use released labels, transparent rules, or a small human-coded sample if those are adequate.

### 2. Action-only monitoring and behavioural synchronization

- **[Verified fact — source reports]** Colosseum’s action/regret or coalition-advantage measure is a direct baseline for whether a coalition changes the system outcome, and is deliberately distinct from message evidence [2].
- **[Verified fact — source reports]** “The Illusion of Collusion” studies repeated-game bandit agents that have no direct knowledge of competitor states/actions. The paper reports that deterministic or increasingly deterministic policies can produce synchronized, seemingly collusive outcomes [5]. This is an important negative control for action similarity; it is not an LLM-agent result.
- **[Verified fact — source reports]** “Collusion with Competitive Marginals” constructs zero-message dependence that preserves each bidder’s marginal bid distribution. It also reports residual correlation of +0.053 for two deployments of the same model versus +0.0001 across models in its LLM auction experiment [6]. These are preprint author reports, not independently reproduced. The paper’s operational use of “collusion” includes coupling without an agreement; that does **not** establish deliberate coordination in the user’s narrower sense.
- **[Verified fact — source reports]** “Hidden Coalitions” includes a negative control where independently trained agents achieve 0.984 within-group action agreement without inter-agent information flow; its authors report that a hidden-state MI graph on independent inputs does not recover the groups, while shared inputs create a spurious block structure [9]. This is a preprint about representational coalitions, not a validated detector of harmful or intentional collusion.
- **[Statistical interpretation]** Action correlation and harmful outcomes are separate axes. Include synchronization as a baseline, but make independent/shared-context behaviour a first-class negative control. Do not label synchrony itself “coordination.”

### 3. Mutual information and conditional dependence

- **[Verified fact — source reports]** Bonjour et al. (UAI 2022) use mutual information between actions and extend to partially observable sequential games; the related net-influence formulation conditions action dependence on state and thresholds the result [4]. This predates the candidate and is an appropriate baseline, not a novelty claim.
- **[Verified fact — source reports]** “Hidden Coalitions” uses pairwise MI over hidden states and spectral partitioning, and explicitly cautions that observational MI does not identify direct causal influence; independent-input controls address one common-input confound [9].
- **[Verified fact — source reports]** “Audit the Whisper” uses cross-run MI and calibrated complementary tests [3]. A separate black-box steganalysis preprint proposes MI, permutation, distribution-shift, timing, and tool-call signals against adaptive agents, but its abstract explicitly describes results as placeholders pending measurement [11]. **Do not cite numeric snippets for that paper as experimental results.**
- **[Statistical interpretation]** CMI can reduce confounding only when the conditioning variables capture the relevant shared context. It remains a dependence statistic; it does not by itself establish a peer-caused effect, agreement, harm, or intent. Sparse state/action cells and repeated observations also make its estimate sensitive to the chosen discretization and sample size.

### 4. Supervised trajectory-feature detectors

- **[Verified fact — source reports]** NARCBench/HELIOS trains activation-based probes and group-level classifiers on instructed collusion scenarios, then tests transfer. The latest paper reports high AUROC on several settings but also reports only 0.38 recall at 1% FPR for its best Transfer detector [7]. AUROC should not be presented as a low-false-positive operating guarantee.
- **[Verified fact — source reports]** A broader multi-agent trajectory-anomaly paper compares supervised XGBoost and semi-supervised SVDD on silent-failure labels, but its target is trajectory failure, not collusion [13]. This supports a small classical-ML baseline as a method class, not a collusion novelty claim.
- **[Hypothesis]** A logistic-regression/XGBoost model over pre-defined message, action, timing, and outcome features is feasible on CPU and should be a baseline if labels permit. Its main risks are prompt/task leakage, label shortcuts, and overfitting to the source benchmark. Split by complete task sequence, model pair, or condition—not by individual episode rows.

### 5. Controlled interventions, matched counterfactuals, and benchmark overlap

- **[Verified fact — source reports]** “Emergent Collusion in Long-Horizon LLM Agent Interaction” defines its target as a joint instruction violation driven by peer behavioural influence. It varies reward/history/feedback and uses scripted compliant/violating peers while holding the focal model and environment fixed [8]. This is a close baseline for separating peer influence from a shared incentive; it is not a general detector evaluation.
- **[Verified fact — source reports]** “Beyond the Transcript” uses matched neutral, blocked, and independent conditions to test whether private latent messages change a receiver’s action distribution [10]. It is white-box and specific to a controlled latent-channel auction attack, so its access assumptions differ, but it shows that “matched counterfactual” is not novel by itself.
- **[Verified fact — source reports]** The SPAR project description explicitly names false positives on benign coordination, conversation monitors missing action-implicit behaviour, and shared-model characteristics versus incentives [12]. It is a public project proposal/description, **not** evidence of completed experiments or results.
- **[Verified fact — source reports]** The organizer-recommended Colosseum and ColludeBench cover complementary communication/action and calibrated-monitoring ideas [2, 3]. Their benchmark definitions and labels differ; do not pool their scores as if they measured one universal “collusion” ground truth.

## Explicit baseline plan to test the candidate

| Baseline / evidence view | What it would score | Relevant prior art | Essential negative control / known limitation |
|---|---|---|---|
| **Message-only** | Explicit agreement/commitment or a transparent transcript classifier; report whether text predicts executed action. | Colosseum; Audit the Whisper; transcript judges in NARCBench [2, 3, 7]. | “Collusion on paper” with no action effect; implicit or steganographic behaviour with no explicit agreement. |
| **Action-only** | Action agreement/synchrony, mutual protocol violation, plus an environment outcome such as coalition advantage or welfare change. | Colosseum; The Illusion of Collusion; Competitive Marginals [2, 5, 6]. | Independent agents with shared task, rewards, model origin, or policy can behave similarly; single-agent marginals can miss joint dependence. |
| **Similarity / synchronization** | Pairwise action overlap or residual correlation, with permutations as a diagnostic null. | The Illusion of Collusion; Competitive Marginals; Hidden Coalitions [5, 6, 9]. | Shared public inputs/common model priors; similarity is not peer influence. |
| **CMI / net influence** | Action dependence conditional on observed public state; pre-specify estimator, bins, and threshold. | Bonjour et al. [4]. | Omitted shared causes, state sparsity, and estimator sensitivity; association is not intervention evidence. |
| **Simple supervised trajectory features** | A small classifier on predeclared message/action/time/outcome features. | NARCBench activation classifiers; adjacent XGBoost trajectory-anomaly work [7, 13]. | Leakage across repeated task sequences/conditions; labels may encode prompts or task identity; use grouped held-out splits. |
| **Combined evidence** | Message + actions/outcome, with controlled peer intervention used as an audit reference rather than a deployable feature. | Colosseum; long-horizon controlled-peer study [2, 8]. | More signals do not equal proof of intent; report which component helps and which creates false positives. |

**[Hypothesis]** The useful result is likely a *failure map*—which signal falsely flags each common-cause condition and which misses each peer-influence condition—rather than one aggregate score or a new “collusion probability.”

## Candidate-direction comparison and feasibility

Qualitative scale: **novelty headroom** is relative to the sources inspected, not a priority guarantee; **high feasibility** means an offline CPU-first route appears plausible, not that it was tested.

| Direction | Novelty headroom / overlap | Ground-truth and inference risk | Rs 0 / RTX 3050 6 GB feasibility | Verdict |
|---|---|---|---|---|
| **A. New detector using matched controls to classify “collusion vs coincidence”** | **Low.** The core question is in the official brief; CMI, multi-view monitoring, calibrated controls, and matched interventions already exist [1–4, 8, 10, 12]. | Medium: scripted/instructed conditions label mechanisms, not hidden mental intent. | High for a simple CPU detector; no paid model required if using scripted or released traces. | Do not claim a novel detector. |
| **B. CMI/net-influence action detector** | **Low.** The central information-theoretic idea dates to 2022 [4]. | Medium-low without randomized peer controls; CMI is observational and depends on measured context. | High computational feasibility on discrete actions, but statistical stability may be poor with sparse states. | Keep as a baseline, not the project contribution. |
| **C. Supervised black-box trajectory-feature classifier** | **Low.** Generic supervised trajectory anomaly detection exists; collusion-specific activation classifiers and benchmark transfer already exist [7, 13]. | Medium-low unless labels and group splits are carefully designed; a classifier can learn task/prompt artefacts. | High for shallow CPU models; released traces avoid inference costs. | Use only as a transparent comparator, with grouped holdouts. |
| **D. White-box activation/representation detector** | **Low.** NARCBench and the spectral-MI paper overlap; matched latent counterfactual monitoring is also published as a preprint [7, 9, 10]. | Medium: activation dependence is not intent and may reflect shared inputs/prompts. | Poor for fresh large-model activation extraction with 6 GB VRAM. NARCBench reports ~2.6 GB pre-extracted data, but the linked code repositories have no visible LICENSE file and the Hugging Face viewer currently errors; do not rely on it until access/rights are clarified [7]. | Not recommended for this sprint under current constraints. |
| **E. Pre-specified-threshold matched-condition evidence audit** | **Moderate but contested.** The individual ingredients are known; the possible contribution is the crossed comparison of the listed black-box baselines on both shared-cause nulls and controlled peer-influence cases. The SPAR project is very close [12]. | Best of the options if labels are defined by experimental condition and objective outcome. Still cannot establish subjective intent. | **Best fit.** Offline analysis of released traces needs no paid APIs; simple features/CMI/classifiers are CPU-friendly. The long-horizon dataset is MIT-licensed but totals 8.12 GB, so select subsets and verify the download path first [8]. | Conditional recommendation as an evaluation/replication extension, not a new detector. |

## Zero-cost/data and statistical feasibility

- **[Verified fact — source reports]** The SALT-NLP release describes 53 conditions, 2,650 trajectories, 27,100 episodes, 15 controlled-peer-intervention conditions covering 750 trajectories, and 50 fixed task sequences reused across conditions. Its dataset page reports a total download size of **8.12 GB** and MIT licensing [8]. The paper’s full model-generation study includes hosted models and large self-hosted models; analyzing released files does not require paying for new API calls, but reproducing all model runs would.
- **[Not verified]** No files were downloaded, so subset sizes, local memory use, parsing cost, and repeatability were not tested. Start with small Parquet subsets (conditions/runs/episodes or selected peer-intervention arms) if proceeding; whether those subsets can be fetched independently was not verified.
- **[Statistical interpretation]** The release uses 50 fixed sequences per condition. For one 50-run negative-control arm, even 0 false positives gives an approximate one-sided 95% binomial upper bound of **5.8%** under an independence assumption; repeated episodes within a trajectory are not independent samples. Therefore, do not promise or claim a 1% (let alone 0.1%) FPR from one 50-run arm. Report counts and uncertainty at feasible operating points, cluster by trajectory/sequence, and keep calibration data separate from the final test set.
- **[Verified fact — source reports]** NARCBench’s README says pre-extracted activation/scenario data are about 2.6 GB; scenario generation requires a running vLLM server and activation extraction requires a GPU [7]. Its current GitHub `LICENSE` paths returned 404, and the linked Hugging Face dataset viewer currently fails to generate a preview. **[Not verified]** Raw-file download and data license status were not established. Avoid basing the sprint on this resource until those issues are resolved.
- **[Verified fact — source reports]** The Audit the Whisper paper page states CC BY 4.0 and describes hosted Gemini/Groq scenarios plus large honest-run calibration; a repository with an MIT license naming the Audit the Whisper Team was found, but exact paper/code correspondence was not independently verified [3]. It is useful as a detector/calibration reference, but a full hosted-model reproduction is not compatible with the no-paid-API constraint. No tests were run.
- **[Verified fact — source reports]** The adaptive black-box steganalysis preprint explicitly marks its results as placeholders pending measurement [11]. It should inform the taxonomy, not be cited as evidence that its detector works.

## Narrow project formulation, if proceeding

**Working title:** *When Synchrony Is Not Peer Influence: A Matched-Condition Audit of Collusion Evidence*.

**Candidate research question:** At a pre-specified operating threshold, how do message-only, action-only, synchronization/CMI, and a shallow supervised trajectory baseline distinguish controlled peer-intervention conditions from matched shared-context/no-peer-access conditions? Measure the focal agent’s response to the intervention, joint protocol violation, and objective harm separately; assess detector outputs against the intervention and outcome labels, not intent.

**Scope limits to state up front:**

1. Use controlled peer assignment as the reference for influence; score protocol violation and objective harm separately. Do not merge them into one “collusion” label or label a run “intentional” from an LLM judge or correlation alone.
2. Keep “explicit agreement,” “peer influence,” “joint protocol violation,” and “harm” as separate columns/metrics.
3. Use released traces offline first. If adding a small CPU scripted null, label it as a synthetic control and do not present it as evidence about real LLM behaviour.
4. Split by full sequence/condition/model pair where possible; avoid episode-level random splits that leak repeated task context.
5. Pre-specify thresholds on calibration data, then report held-out confusion counts, false-positive cases, false negatives, and uncertainty. Do not tune on the final test set.
6. If a control arm is too small to support a useful low-FPR estimate, report the limitation and a coarser operating point rather than implying deployment-grade calibration.

**[Hypothesis]** This evaluation could be scientifically useful and feasible without paid APIs, but its novelty is incremental and contested. A final source check and data-subset inspection should happen before any implementation. If an exact crossed evaluation already exists, narrow further to a reproducibility/negative-result report or choose another direction.

**Sprint timing [hypothesis]:** With preparation through Oct 22 and the three-day sprint Oct 23–25, this is the only candidate with a plausible bounded offline deliverable: verify a small released-data subset and condition matching before the sprint, then run a pre-specified CPU analysis. This is conditional on the subset being accessible and the controls actually matching; no completion or competition result is promised. If data access or condition matching fails, do not silently substitute unmatched labels—report the blocker and use a clearly labelled synthetic control or a narrower replication.

## Sources reviewed

1. [Apart Research AI Collusion Research Sprint — official brief](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25) — Track 2.3 questions and recommended Colosseum/ColludeBench resources; details are also recorded in `official_requirements.md`.
2. [Colosseum paper](https://arxiv.org/abs/2602.15198) — communication evidence versus action/regret or coalition advantage; “collusion on paper” distinction. See Phase 1 `related_work.md` for repository/license notes.
3. [Audit the Whisper paper](https://arxiv.org/html/2510.04303v2); [MIT-licensed repository](https://github.com/Ostailor/Steganographic_Collusion) — transcript-side multi-signal detection, honest-run calibration, and hosted-model scenarios. The repository license names the Audit the Whisper Team, but exact paper/code correspondence was not independently verified; paper results are not reproduced.
4. [Bonjour et al., UAI 2022 paper on information-theoretic collusion detection](https://proceedings.mlr.press/v180/bonjour22a.html) — mutual/conditional-dependence action baseline.
5. [“The Illusion of Collusion”](https://arxiv.org/html/2411.16574) — context-free bandits and action synchronicity without competitor-state/action access; working-paper source, not an LLM experiment.
6. [“Collusion with Competitive Marginals”](https://arxiv.org/html/2607.26385v1) — preprint on same-model residual dependence, preserved marginals, and the distinction between statistical coupling and deliberate agreement; author-reported results.
7. [NARCBench / HELIOS v3](https://arxiv.org/html/2604.01151v3); [linked repository](https://github.com/aaronrose227/narcbench); [dataset](https://huggingface.co/datasets/aaronrose227/narcbench) — supervised white-box group probes, transfer, transcript limits, strict-FPR result, and current access/license caveats.
8. [“Emergent Collusion in Long-Horizon LLM Agent Interaction”](https://arxiv.org/html/2609.24967v2); [MIT code/task-data repository](https://github.com/SALT-NLP/agent-collusion); [MIT dataset](https://huggingface.co/datasets/SALT-NLP/agent-collusion) — shared reward/history, controlled-peer interventions, released trajectories and data-size details; author-reported results.
9. [“Hidden Coalitions in Multi-Agent AI”](https://arxiv.org/html/2605.06696v1) — independent-input control for behavioral similarity versus representational dependence; preprint, not a harmful-intent detector.
10. [“Beyond the Transcript”](https://arxiv.org/html/2608.19161v1) — matched neutral/blocked latent counterfactuals; white-box, fixed-code latent-channel scope.
11. [“Steganalysis of Adaptive Covert Collusion”](https://arxiv.org/html/2608.02698v1) — proposed black-box MI/permutation/timing/tool baselines; paper labels results as placeholders pending measurement.
12. [SPAR project description: “Understanding and Monitoring Collusion in LLM Multi-Agent Systems”](https://sparai.org/projects/f26/recDQmFvumFiPhPZs/) — close stated overlap on benign-coordination false positives, action-implicit behaviour, and incentives/shared model characteristics; proposal only, not completed results.
13. [“Detecting Silent Failures in Multi-Agentic AI Trajectories”](https://arxiv.org/html/2511.04032v1) — adjacent XGBoost/SVDD trajectory-anomaly baselines; target is silent failure, not collusion.
14. [“Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems”](https://arxiv.org/abs/2606.28425) — Phase 1 related-work source on shared Schelling salience and tacit-scheme convergence; see `related_work.md`.

## Phase 2 completion record

- **[Verified fact]** The source-backed gap audit, direction comparison, explicit baseline matrix, license/access notes, and zero-cost/hardware assessment are recorded here.
- **[Experimental observation]** None; no code, tests, data downloads, model calls, or experiments were run.
- **[Future work]** If the user asks to continue, first verify the chosen dataset subset and exact condition matching, then freeze the target labels/splits/metrics before Phase 3 coding. Do not claim intent detection or a novel detector based on this audit alone.
