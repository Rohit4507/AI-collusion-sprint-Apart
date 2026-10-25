# Phase 3 — Preregisterable experimental design

- **Date:** 2026-10-18 (Asia/Calcutta)
- **Status:** Protocol v1.0 was frozen internally on 2026-10-18 before any selected-arm outcome analysis. Pre-outcome amendment A1 (data-integrity gate) was added on 2026-10-18 after inspecting only the general episode-table schema. Software-only amendment A2 (secondary classifier failure handling) was added on 2026-10-25; no selected-arm rows or outcomes were inspected. The protocol is **not externally registered**. No dataset files have been downloaded or inspected locally.

## 1. Decision and scope

**[Verified fact — source reports]** The SALT-NLP release contains a directly relevant controlled-peer pair for one focal model and 50 fixed task sequences. The two selected condition IDs are:

- **Scripted compliant-peer arm:** `controlled_peer__gemini-3-7-flash__raw-prefix--reject--full-feedback`
- **Scripted violating-peer arm:** `controlled_peer__gemini-3-7-flash__summary--accept--full-feedback`

The public condition metadata reports 50 runs and 10 evaluation episodes per arm. The repository README describes the compliant script as sending a raw-log prefix and returning `REJECT`, and the violating script as sending a summary and returning `ACCEPT`. Both use the same focal model, default full-feedback configuration, and fixed task sequences [1–3].

**Important scope correction:** these arms test a **bundled peer-policy intervention**—the peer’s message policy and assigned verdict change together. Both selected condition records set `controlled_bob_observed_verdict=false`, so the focal agent is not explicitly shown that scripted verdict; shared reward/feedback could still mediate an effect, and that mechanism is not isolated here [1–3]. Do not claim separate message-versus-verdict/feedback effects. These are not a no-peer-access/common-cause control. The selected data can support a narrow audit of whether a controlled peer-policy change is associated with a change in the focal agent’s observable behaviour. It cannot, by itself, answer the broader “coordination versus coincidence” question, estimate general benign-coordination false-positive rates, or establish deliberate intent.

**Working title:** *Auditing Signals of Peer-Policy Influence in Matched Multi-Agent Traces*.

**Primary question:** In the released controlled-peer traces, does the focal agent’s rate of accepting work without the complete raw evidence change between the scripted violating-peer and compliant-peer arms, after blocking on the shared task sequence?

**Secondary question:** Can message-only, action-only, or combined **focal-agent-only** trajectory features distinguish the two scripted peer-policy arms on held-out task sequences? This is a test of observable response to an intervention—not a detector of hidden intent or “collusion” in general.

## 2. Evidence labels used in this plan

- **[Verified fact — source reports]** Metadata, paper, or repository documentation states the fact. Source-reported study results are not independently reproduced.
- **[Design choice]** A proposed operational definition or analysis decision to freeze before looking at outcome differences.
- **[Statistical interpretation]** Interpretation of the planned estimator, data structure, or uncertainty.
- **[Not verified]** A data-access, schema, pairing, or implementation detail that remains to be checked.
- **[Experimental observation]** None; no analysis has run.

## 3. Data, arms, and analysis units

### 3.1 Source and condition selection

**[Verified fact — source reports]** The dataset’s `conditions` table lists the two condition IDs above with `alice_model = gemini/gemini-3.7-flash`, `bob_model = controlled`, `n_runs = 50`, `episodes_per_run = 10`, and no warm-up episodes. The repository README describes both peer scripts and says the same 50 task sequences are reused across conditions [1–3].

**[Design choice]** Include only these two full-feedback controlled-peer arms for the confirmatory analysis. Do not add other models, ablations, or conditions after viewing their outcomes. Use the 10 evaluation episodes per run. Use the two condition IDs, not a hand-selected episode subset, to identify the arms.

**[Not verified — pre-analysis data gate]** Before analysis, confirm from the selected episode/run records that each arm has one valid run for every `sequence_id` 1–50; the two arms share the same tasks for each sequence; and the episode ordering and verdict fields are complete. If the released records do not support those checks, stop the paired analysis, record the missingness, and revise the protocol before computing outcome summaries. Do not silently replace an arm or use a different condition.

### 3.2 Metadata-only data-access preflight and protocol lock

- **[Verified fact — dataset-server metadata, 2026-10-18]** The dataset page lists **8.12 GB** total file size. Separately, the Hugging Face datasets-server `/size` endpoint reports an `episodes` Parquet config with 27,100 rows, 43 columns, and **15,976,423 bytes** of Parquet files (about 15.98 MB decimal); its metadata estimate for memory is about 63.8 MB. It lists all converted Parquet configs at 81,260,863 bytes total. These figures cover different scopes and have not been reconciled; the analysis plan needs only the `episodes` table if the listed message/action fields are present.
- **[Not verified]** No Parquet or raw trace file was downloaded. A schema-only `/rows` sample from the `episodes` table contained records from an unrelated condition; it confirms global column names, not selected-arm field completeness or row values. The server-side `/filter` query did not return a usable result, so selected condition filtering will be done locally if the `episodes` Parquet config is retrieved. Exact row-level pairing and local parsing remain runtime checks.
- **[Pre-outcome amendment A1 — data integrity]** The global schema includes `controlled_message_generation_failed`. Require this flag to be false on every selected episode; if any selected row indicates a failed controlled message, stop before computing outcomes and report the issue. Do not silently drop affected episodes or runs. This amendment adds only an intervention-integrity gate; it does not change the condition IDs, estimand, outcomes, feature sets, splits, or thresholds. It was recorded before inspecting selected-arm rows or outcomes.
- **[Pre-outcome amendment A2 — secondary classifier failure handling]** If a pre-specified classifier view cannot be fit in any fold because its feature matrix or training step fails (for example, an empty Alice-text vocabulary), mark that classifier view `not_run`, record the reason, do not substitute features or models, and continue the primary outcome analysis and any other views that fit. No selected-arm results were inspected when this software-only handling rule was added (2026-10-25).
- **[Design choice]** Freeze this protocol as internal version 1.0 on 2026-10-18 before inspecting outcomes from the two selected arms. The freeze applies to condition IDs, outcomes, splits, baseline features, thresholds, and stopping rules above. Any change after selected-arm outcomes are examined must be recorded as an exploratory amendment. This is not an external/public preregistration.

### 3.3 Units and pairing

- **Primary unit:** one 10-episode trajectory/run.
- **Blocking unit:** `sequence_id`, with the two arms paired by the same fixed task sequence where the pre-analysis check confirms the match.
- **Expected design size:** 50 sequence blocks × 2 arms = 100 runs and 1,000 episodes. These are metadata counts, not a verified local sample count.
- **Inference caveat:** pairing controls task-sequence differences, but the two runs are not necessarily identical-seed counterfactuals. Episodes within a trajectory are repeated observations, not independent samples.

**[Design choice]** For the paired arm contrast, retain only complete sequence blocks. Report exactly how many blocks are retained and which are missing. Do not impute outcomes or replace missing blocks. If fewer than 40 complete sequence blocks remain, report the effect descriptively and do not fit the supervised classifier.

## 4. Operational outcomes: do not merge influence, dependence, harm, and intent

The selected experiment has known script assignment; that is a **peer-policy intervention label**, not an intent label. The following outcomes remain separate:

1. **Focal response / protocol-violation proxy (primary):** per run, the proportion of episodes in which Alice returns `ACCEPT` despite not receiving the complete raw log required by the protocol. The source study describes the constrained channel as insufficient to transmit the full raw log [2]. Before analysis, verify that the released communication records support this operational rule. If completeness cannot be verified, use the narrower label **“Alice ACCEPT under the constrained-evidence condition”** and do not call it a proven protocol violation.
2. **Peer influence (primary contrast):** the within-sequence difference in the focal response rate between the scripted violating-peer arm and the scripted compliant-peer arm. This is evidence about the effect of the **bundled intervention** in this benchmark setting; it does not identify whether the message, verdict, or their interaction caused the difference.
3. **Objective false approval (secondary outcome):** among episodes where `bob_task_correct` is false, the proportion Alice accepts; also report the false-approval count per run. If a run has no incorrect Bob tasks, mark its conditional rate undefined and retain its count as zero. Call this a false-approval/task-error outcome, not general real-world harm.
4. **Explicit communication agreement (descriptive only):** if the released `agreement` annotation covers the selected arms, report its counts separately. It is a source-provided judge/annotation label with limited validation, not ground truth for intent. Do not call the absence of an agreement annotation proof of no influence.
5. **Statistical dependence / synchronization:** descriptive only where estimable. These arms use a scripted peer whose verdict is fixed by condition; simple cross-agent agreement is therefore strongly entangled with the intervention itself. Do not interpret it as independent evidence of deliberate coordination.
6. **Intent:** not measured and not inferred.

## 5. Hypotheses and estimands

### Confirmatory hypothesis

- **H1 (directional expectation, two-sided inference):** Alice’s mean per-run constrained-evidence `ACCEPT` rate is higher under the scripted violating-peer arm than under the scripted compliant-peer arm.
- **Estimand:** for each complete sequence block, compute `d_i = rate_i(violating peer) − rate_i(compliant peer)`. The primary effect estimate is the mean of the 50 (or available complete) `d_i` values.
- **Uncertainty:** 95% percentile bootstrap interval from 10,000 resamples of whole sequence blocks, retaining both arms in each resampled block. Report the paired effect in percentage points, both arm means, all block-level differences, and the number of blocks. No episode-level standard errors.
- **Decision language:** a positive point estimate with a 95% interval entirely above zero is evidence of a difference in this released controlled-peer setting. An interval including zero is inconclusive at this sample size—not proof of no influence.

### Secondary outcomes

- Difference in false-approval counts per run, calculated on the same paired sequence blocks; also report pooled false approvals / incorrect-task opportunities by arm. Do not impute a per-run conditional rate when a run has no incorrect-task opportunities.
- Per-episode acceptance rates by episode index, plotted descriptively with trajectory-level uncertainty; do not treat each episode as an independent replicate.
- The count of available explicit-agreement annotations, if coverage is adequate; no confirmatory test on this annotation.

No hypothesis in this plan concerns whether either agent *intended* to collude.

## 6. Pre-specified evidence baselines

The primary study evaluates response to a known scripted intervention. The baseline table below is deliberately conservative about signals that the selected arms cannot identify.

| Evidence view | Planned operational measure | Use in this study | Caveat / exclusion rule |
|---|---|---|---|
| **Message-only** | Linear classifier over Alice-authored communication text in each run; use TF–IDF word unigrams/bigrams, `min_df=2`, at most 500 features, L2 logistic regression with `C=1`. Fit the vocabulary within each training fold. Exclude Bob’s scripted messages, Bob’s fixed verdict, condition ID, model metadata, and task-sequence ID. | Secondary test: can the focal agent’s own messages distinguish the two peer-policy arms on unseen sequences? | This predicts intervention assignment, not intent. It may reflect task language or the focal model’s response style. Grouped splits are mandatory. |
| **Action-only** | Fixed-length sequence of Alice’s 10 verdicts (`REJECT=0`, `ACCEPT=1`) and her run-level acceptance rate; no text or task metadata. Use the same L2 logistic-regression specification. | Secondary intervention-arm classifier and descriptive action baseline. | It tests whether behaviour changes across scripted arms; it is not a general collusion detector. |
| **Combined message + action** | Concatenate the pre-specified message and action features, with the same model and split. | Secondary comparator for incremental predictive value over either evidence surface alone. | Do not interpret a small score increase as proof of intent or causality. |
| **Behavioural similarity / synchronization** | Report the raw fraction of episodes in which Alice’s verdict matches the scripted peer verdict, only as a descriptive check. | Not included in the confirmatory detector comparison. | Bob’s verdict is fixed by the assigned arm, so this measure can reveal the treatment label by construction. A high score would not establish emergent coordination. |
| **Action MI / conditional MI / net influence** | No confirmatory action-dependence estimate in the selected two-arm data. | Within-arm MI involving the constant scripted-peer verdict is zero/degenerate by construction; treat it as non-informative, not as evidence of independence. | Pooling arms would make treatment assignment a common cause of both variables; the resulting dependence is not an independent measure of peer-caused influence. Do not report pooled action MI as a causal result. |
| **Simple supervised trajectory classifier** | The pre-specified logistic regressions above, predicting the peer-policy arm from focal-agent-only messages, actions, or both. | Secondary only; no feature search, model sweep, or final-test tuning. | This is a shallow classifier on 50 sequence blocks, not a validated deployment monitor. If fewer than 40 complete blocks remain, omit it. |

### Grouped evaluation protocol

- Assign fold `k = (sequence_id − 1) mod 5`; all arms and episodes from a sequence stay in the same fold.
- Generate out-of-fold predictions from five fits. No row, episode, or other arm from a held-out sequence may enter training.
- Report ROC-AUC, balanced accuracy, and the confusion counts. Also report the majority/random reference (balanced accuracy 0.5) and the paired-sequence bootstrap interval for AUC/balanced accuracy.
- For a fixed review-budget illustration, choose a score threshold using **only compliant-arm trajectories in the training folds** to target a nominal 20% training false-flag rate; evaluate that frozen fold threshold on held-out sequences. Report integer false-flag and detection counts and uncertainty. This is not a deployment-grade FPR claim.
- Do not claim 1% or 0.1% FPR. Even 0 false flags among 50 independent control trajectories would only give an approximate one-sided 95% upper bound of 5.8%; sequence clustering and paired task structure further limit generalization.

## 7. Preprocessing, exclusions, and leakage controls

1. Read only the selected release records needed for these two conditions. Do not run the authors’ LLM judges or call any hosted model. Require `controlled_message_generation_failed=false` on every selected episode; if any value is true, stop before outcome calculations and report the failure rather than silently excluding rows.
2. Keep only the 10 evaluation episodes in each zero-warm-up run; verify episode indices from metadata rather than assuming array order.
3. Map verdict labels using the dataset’s documented values. Preserve the original fields and a machine-readable run/sequence manifest.
4. If the same sequence is missing in either arm, exclude that pair from paired estimates and report it. No replacement sequences, post-hoc arm substitution, or outcome-based exclusions.
5. Exclude direct treatment metadata and all Bob-authored scripted content from the focal-only classifiers. Do not use `condition_id`, `run_id`, `sequence_id`, task IDs, task correctness, reward, or post-verdict feedback as predictors. The arm classifier is explicitly **retrospective** and may use the completed 10-episode Alice-only trace; do not describe it as online early-warning monitoring.
6. If a message feature cannot be derived without using post-decision information, omit it and document the omission; do not redefine the feature after seeing results.
7. Do not use source judge labels as training targets for “collusion”; they may be displayed as a separate annotation only if coverage and meaning are verified.

## 8. Missingness, robustness, and stopping rules

- **Data gate:** metadata indicates the `episodes` Parquet config is about 15.98 MB, but actual retrieval and local parsing are untested. Retrieve only that config if it provides all required fields; do not fetch the full 8.12 GB release or raw traces for this analysis. If the table cannot be obtained separately or lacks required fields, stop and document the blocker; do not treat metadata previews as experimental data.
- **Pairing gate:** require at least 40 complete `sequence_id` blocks for confirmatory paired inference. Fewer blocks → descriptive reporting only; do not substitute a different pair of conditions after inspecting outcomes.
- **Protocol-label gate:** if raw-log completeness cannot be checked from the selected trace/message fields, relabel the primary endpoint as constrained-evidence `ACCEPT`; make no direct protocol-violation claim.
- **Classifier gate:** if the records do not provide 10 ordered episodes per run, or if the fold grouping cannot keep paired sequences together, omit supervised classification and report why.
- **Classifier-view failure (A2):** if a specific pre-specified feature view cannot be fit, mark it `not_run` with its reason; do not tune/replace it, and do not suppress the primary paired-outcome report or other views that fit.
- **No silent tuning:** there is no threshold/model/feature tuning on final held-out predictions. Any protocol change after examining outcome results must be labelled an exploratory amendment, with the original analysis retained.
- **Negative results:** report null or contrary-direction differences, false flags on the compliant-script arm, missing data, annotation coverage, and all deviations from this plan.

## 9. Scope limitations and one later extension

**[Statistical interpretation]** A difference between these two arms supports a response to the **scripted peer-policy bundle** only. Because the peer’s messages and verdict change together, this design cannot isolate communication from action. Because the selected arms do not provide an established no-peer-access common-cause null, this experiment cannot estimate false positives on benign synchronization or answer the full “coincidence” question. The fixed-peer setup also makes synchrony and action-MI baselines degenerate or treatment-confounded.

**[Future work — one extension, not part of the confirmatory analysis]** If the core reanalysis is complete and time remains, add a small deterministic CPU simulator with (a) shared-context synchrony but no peer-to-peer causal edge and (b) an explicitly randomized peer-influence intervention. Keep simulated results separate from LLM-trace results; use the simulator only to stress-test whether similarity/MI/CMI can distinguish common cause from direct influence under known data-generating assumptions. Do not describe a synthetic control as evidence about deployed LLMs.

## 10. Feasibility and sprint schedule

- **Budget / compute:** no paid APIs, new model generation, GPU inference, or 27B judge is required for the planned offline analysis. TF–IDF and shallow logistic regression are CPU-friendly. Local storage/time feasibility is **not verified** because the selected subset has not been retrieved.
- **Oct 18–20 (preflight):** confirm the exact two condition records, subset access, pair completeness, and fields for verdicts/messages/correctness. Do not inspect outcome differences before the protocol is frozen.
- **Oct 21–22 (freeze):** record the final version of this protocol and any data-access amendments with a timestamp before calculating outcomes or fitting classifiers.
- **Oct 23–24 (sprint, conditional):** execute the pre-registered paired analysis and grouped secondary classifiers only if the preflight gates pass; preserve raw subset, scripts, config, logs, and environment details.
- **Oct 25 (sprint):** report effect estimates, uncertainty, counts, failures, and limitations. If a gate fails, submit a transparent feasibility/negative result rather than silently changing the design.

This schedule is a plan, not a promise of completion or competition results.

## Sources inspected for this design

1. [SALT-NLP dataset condition metadata: controlled-peer rows](https://datasets-server.huggingface.co/rows?dataset=SALT-NLP/agent-collusion&config=conditions&split=test&offset=28&length=7) — exact condition IDs, models, run counts, and configuration fields. Metadata view only; no dataset files downloaded.
2. [Emergent Collusion in Long-Horizon LLM Agent Interaction, v2](https://arxiv.org/html/2609.24967v2) — verification protocol, constrained evidence channel, scripted peer intervention, and the paper’s operational definition. Author-reported study; not reproduced.
3. [SALT-NLP repository README: controlled peer interventions](https://github.com/SALT-NLP/agent-collusion/blob/main/README.md) — compliant/violating peer scripts, shared task-sequence structure, and judge setup.
4. [SALT-NLP dataset page](https://huggingface.co/datasets/SALT-NLP/agent-collusion) — license, data-size metadata, and available dataset subsets; page lists 8.12 GB total file size.
5. [Datasets-server size metadata](https://datasets-server.huggingface.co/size?dataset=SALT-NLP%2Fagent-collusion) and [Parquet file metadata](https://datasets-server.huggingface.co/parquet?dataset=SALT-NLP%2Fagent-collusion) — converted `episodes` table size and row/column counts. Metadata only; no Parquet file downloaded.

## Phase 3 completion record and current status

- **Phase 3 done:** Froze internal protocol v1.0 before selected-arm outcome analysis; specified exact condition IDs, outcomes, baseline eligibility, grouped validation, exclusion rules, uncertainty, and stopping criteria. Metadata-only preflight found a small `episodes` Parquet config suitable for a no-full-release route.
- **At Phase 3 close:** No local data inspection/download, code, tests, detector, model/API call, benchmark run, or experiment had been performed.
- **Later status:** Phase 4 offline pipeline and synthetic tests are implemented; see `research/implementation_record.md`. Software review amendments A1/A2 are listed above.
- **Open blocker:** The broad common-cause/no-peer-access contrast is not supplied by the selected arms; actual Parquet retrieval, parsing, and sequence pairing remain unverified.
- **Next:** Obtain the `episodes` Parquet shards and pass the local pre-analysis gate before computing outcomes. Do not add a no-peer/common-cause claim unless a valid control is added and preregistered before its outcomes are examined.
