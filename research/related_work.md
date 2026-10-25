# Phase 1 — Source inventory revalidation, 2026-10-25

**[Verified fact]** The following entries were checked through live pages and GitHub API/README reads on 2026-10-25. No external benchmark was installed or executed in this recheck. Historical paper metadata below was not revalidated; do not treat the old inventory as fresh source verification.

| Source / date checked | Source-reported key claim | License evidence | Rs 0 / local status |
|---|---|---|---|
| [Official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25), 2026-10-25 | **[Verified fact]** Track 2.3 already asks for coordinated harm vs common incentives vs talk-only cases, with conversation, advantage and dependence evidence. | **[Not verified]** Public webpage availability is not a reuse license. | **[Verified fact]** Default Track 2 pilots estimate paid API costs; no-GPU does not mean Rs 0. |
| [Colosseum](https://github.com/umass-ai-safety/colosseum), README and default branch, 2026-10-25 | **[Verified fact]** Tool-calling multi-agent audit framework; current README documents Terrarium 0.2.1 and paper tag `paper-v0.1.1` using 0.1.1, with behavioral differences. Local Qwen2.5-7B/vLLM configs documented. | **[Verified fact]** GitHub license endpoint returned 404 and root listing exposed no LICENSE. **[Not verified]** No blanket reuse permission established; dependencies and paper may have separate licenses. | **[Verified fact]** Local-model route is documented. **[Not verified]** It was not run; CPU or RTX 3050 6 GB feasibility and complete local judging remain unestablished. |
| [ColludeBench / Audit the Whisper](https://github.com/Ostailor/Steganographic_Collusion), README and license API, 2026-10-25 | **[Verified fact]** Authors describe MI/permutation/watermark/fairness detectors, synthetic environments and honest-run calibration; reported strong performance is not independently reproduced here. | **[Verified fact]** GitHub license API identifies MIT for repository code; dataset and external baseline rights still need separate inspection. | **[Verified fact]** README separates smoke/regeneration commands from Gemini/Groq runs requiring keys. **[Not verified]** Commands, referenced artifacts and full no-cost reproduction have not been tested. |
| [Bonjour et al.](https://proceedings.mlr.press/v180/bonjour22a.html), organizer description checked 2026-10-25 | **[Verified fact — organizer report only]** Organizer describes pairwise net influence in small discrete games, assumes exactly two colluders, and says no public author implementation located. | **[Not verified]** Paper/implementation license not checked this turn. | **[Hypothesis]** Scripted CPU validation is plausible; correctness and applicability need dedicated checks. |
| [Omission Attacks](https://apartresearch.com/sprints/projects/omission-attacks-when-doing-nothing-is-the-attack-0y1v), 2026-10-25 | **[Verified fact — source reports]** Explicit omission threat model and postcondition-monitor comparison; reviews request scale, repeats and overfitting checks. [Event](https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22) lists first place. | **[Not verified]** Report/code reuse license not established. | **[Not verified]** Full no-paid-API reproduction not established; this is a presentation/control-design precedent. |
| [Loyal Lies](https://apartresearch.com/sprints/projects/loyal-lies-auditing-secret-loyalties-under-attack-and-the-falsepositive-problem-in-blind-elicitation-ezwb), 2026-10-25 | **[Verified fact — source reports]** Decoy/exposure controls, blind checks and detector attacks; reviews identify one prespecified-gate inconsistency and narrower evasion scope. | **[Not verified]** License not rechecked this turn. | **[Not verified]** Reported experiments not reproduced. No inference that they fit our compute budget. |

**[Hypothesis]** The novel contribution must be more specific than “distinguish coincidence from collusion”: the organizer already proposes that question and corresponding controls. Phase 2 should compare a concrete control/calibration improvement, an offline empirical trace audit, and a limited synthetic identifiability/failure-mode study.

**[Future work]** Audit paper methods, exact code paths and available trajectory artifacts before selecting a project. Hosted-model provenance of public logs must be disclosed even if analysis itself costs Rs 0; if the constraint excludes proprietary-origin data entirely, reject that route.

---

## Historical source inventory (not freshly verified)

# Phase 1 — Related-work and source inventory

- **Inventory date:** 2026-10-17 (UTC)
**Scope:** Organizer-linked resources and the nearest public methods/benchmarks, plus a few Apart project precedents. This is an initial source map for the Phase 2 novelty audit, not a complete systematic review.

## How to read this inventory

- **[Verified fact]** means the linked page/paper/repository states the item; it does not mean we independently reproduced the study’s reported result.
- **[Experimental observation]** would mean an experiment we ran. **None** of the studies or repositories below was executed by us in Phase 1.
- **[Statistical interpretation]** is reserved for interpretation of measured data. No new effect estimate is reported here.
- **[Hypothesis]** marks an inference that needs later testing.
- **[Future work]** marks a planned check.
- **[Not verified]** marks unknown license, runnability, reproduction, or claim status. All repository-runability statements below are from static documentation inspection only.

## Research sources and reusable methods

### R1. Colosseum — cooperative multi-agent collusion audit

- **[Verified fact] Source/date:** [Paper](https://arxiv.org/abs/2602.15198), submitted 2026-02-16 and revised 2026-05-27; [code](https://github.com/umass-ai-safety/colosseum), repository README updated 2026-10-09; both inspected 2026-10-17.
- **[Verified fact] Key claim in the paper:** Colosseum models cooperative agent tasks using a formal multi-agent decision framework and compares action-based coalition advantage/regret with communication-based judging. The paper reports both emergent coordination when private channels are available and “collusion on paper,” where text expresses a plan that does not yield corresponding actions. These are authors’ reported results, not independently reproduced here. [Paper](https://arxiv.org/abs/2602.15198)
- **[Verified fact] Organizer relevance:** The sprint recommends Colosseum for Track 2 questions 2.1/2.3; organizer documentation says it has Hospital/Jira tasks, assigned colluding pairs, private channels, individual rewards, and coalition-advantage measures. [Official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact] License:** The paper’s arXiv page displays CC BY 4.0. The GitHub default branch has no `LICENSE` file; do not assume the code has the paper’s license. [Paper](https://arxiv.org/abs/2602.15198); [repository file list](https://github.com/umass-ai-safety/colosseum); [LICENSE path check](https://github.com/umass-ai-safety/colosseum/blob/main/LICENSE)
- **[Verified fact] No-paid-API feasibility:** The repository instructions call for Terrarium/CoLLAB setup and say to configure API keys if needed; they warn API cost scales with agent count. The organizer estimates $15–$75 for short episodes with an API provider. [Repository README](https://github.com/umass-ai-safety/colosseum); [official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Not verified]** We did not install Colosseum, run its tests, generate logs, establish a full local-model route, or inspect every submodule/data asset. Full no-cost reproducibility on a 6 GB laptop is not verified.

### R2. ColludeBench / “Audit the Whisper” — benchmark and calibrated detector suite

- **[Verified fact] Source/date:** [Paper](https://arxiv.org/abs/2510.04303), submitted 2025-10-05 and revised 2025-10-17; [repository](https://github.com/Ostailor/Steganographic_Collusion), latest release shown as 2025-10-17; inspected 2026-10-17.
- **[Verified fact] Key claim in the paper/repository:** The authors describe ColludeBench-v0 across pricing, auctions, peer review, and other scenarios, and a detector suite using mutual information, permutation invariance, watermark variance, and fairness-aware signals. The paper/repository report a 10,000-honest-run calibration and strong fixed-FPR results. These are author claims; they should not be treated as independently verified performance or as a guaranteed state-of-the-art baseline. [Paper](https://arxiv.org/abs/2510.04303); [repository README](https://github.com/Ostailor/Steganographic_Collusion)
- **[Verified fact] License:** The arXiv paper page displays CC BY 4.0; the repository contains an MIT license. [Paper](https://arxiv.org/abs/2510.04303); [repository LICENSE](https://github.com/Ostailor/Steganographic_Collusion/blob/main/LICENSE)
- **[Verified fact] No-paid-API feasibility:** The repository documents a local smoke check (`compileall` plus selected `pytest` files); its hosted Gemini/Groq experiments explicitly require API keys. Therefore, local smoke tests appear separable from hosted runs, while complete hosted-model reproduction is not no-paid-API. [CI check](https://github.com/Ostailor/Steganographic_Collusion/blob/main/scripts/ci_check.sh); [README](https://github.com/Ostailor/Steganographic_Collusion)
- **[Verified fact] Organizer caution:** Apart explicitly says ColludeBench contains environments, detectors, and stored manifests, but should be preflighted rather than treated as a turnkey raw-trajectory dataset. [Official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Not verified]** No code, data, or results from this repository were run or independently checked in Phase 1; the paper’s exact result claims remain unverified by this project.

### R3. “When Agents Lie” / LLM-Trust-Breaking — private plans, public claims, and actions

- **[Verified fact] Source/date:** [Paper](https://arxiv.org/abs/2607.05132), submitted 2026-07-06 and revised 2026-07-07; [repository](https://github.com/Jerick-1380/LLM-Trust-Breaking), README updated 2026-06-29; inspected 2026-10-17.
- **[Verified fact] Key claim in the paper:** It separates private intent, public announcement, and final action in repeated games, and reports that many announcement deviations were already present in private plans, with strong variation across games and models. It is relevant to statement/action mismatch, but it is not presented as a general collusion-intent detector. [Paper](https://arxiv.org/abs/2607.05132)
- **[Verified fact] Organizer relevance:** The sprint recommends the harness for Track 2.2 because it records plans, announcements, actions, and outcomes; it recommends TraceGuard only as a source of reusable action-trace consistency ideas, not as a drop-in collusion detector. [Official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact] License:** The paper page displays CC BY 4.0; the inspected repository has no `LICENSE` file. [Paper](https://arxiv.org/abs/2607.05132); [repository](https://github.com/Jerick-1380/LLM-Trust-Breaking); [LICENSE path check](https://github.com/Jerick-1380/LLM-Trust-Breaking/blob/main/LICENSE)
- **[Verified fact] No-paid-API feasibility:** The repository’s quick start asks for OpenAI and OpenRouter keys and runs a hosted model by default. It is not a zero-cost/offline baseline as documented. [Repository README](https://github.com/Jerick-1380/LLM-Trust-Breaking)

### R4. TraceGuard — action-trace consistency monitor (adjacent, not a collusion detector)

- **[Verified fact] Source/date:** [GitHub repository](https://github.com/linhkid/TraceGuard), README/license last updated 2026-03-22; inspected 2026-10-17.
- **[Verified fact] Key claim/purpose:** TraceGuard proposes multi-dimensional monitoring of agent actions, including action–trace consistency. Its README identifies it as an AI-control monitor and distinguishes experimentally validated from implemented-but-not-yet-validated components; the sprint calls it a single-agent monitor, not a collusion detector. [Repository README](https://github.com/linhkid/TraceGuard); [official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact] License:** MIT. [Repository LICENSE](https://github.com/linhkid/TraceGuard/blob/main/LICENSE)
- **[Not verified] No-paid-API feasibility:** A complete no-cost run was not established; it is an LLM-monitoring system and no local/offline monitoring route was verified in this audit.

### R5. Bonjour et al. — information-theoretic dependence baseline

- **[Verified fact] Source/date:** [PMLR paper](https://proceedings.mlr.press/v180/bonjour22a.html), UAI 2022; inspected 2026-10-17.
- **[Verified fact] Key claim:** The paper studies mutual information between agent actions as a domain-independent indicator of collusion in repeated simultaneous games and partially observable sequential games. The organizer specifically notes pairwise net influence as a compact candidate statistic, its assumption of exactly two colluders, and that an author implementation was not found. [Paper](https://proceedings.mlr.press/v180/bonjour22a.html); [official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Not verified] License:** The inspected PMLR page did not expose an explicit paper license; no reuse license is inferred here.
- **[Verified fact] No-paid-API feasibility:** The statistic can be evaluated on already-generated discrete trajectories without model/API calls, but the inspected source is a paper rather than an author implementation; a faithful implementation and validation would still be required. [Official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)

### R6. Fish et al. — LLM algorithmic pricing and prompt sensitivity

- **[Verified fact] Source/date:** [Paper](https://arxiv.org/abs/2404.00806), submitted 2024-03-31, revised 2026-08-31, arXiv comments state accepted to EC 2026; [code](https://github.com/luciasauer/algorithmic_pricing_llms), MIT license; inspected 2026-10-17.
- **[Verified fact] Key claim:** The paper reports that LLM pricing agents can reach supracompetitive prices in oligopoly settings and that seemingly innocuous prompt variations affect the result. The official page describes the code as a repeated two-seller game with visible history and suggests single-variable ablations. [Paper](https://arxiv.org/abs/2404.00806); [repository](https://github.com/luciasauer/algorithmic_pricing_llms); [official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact] License:** The code repository has an MIT license. The arXiv page displays arXiv non-exclusive distribution terms rather than a CC license. [Code LICENSE](https://github.com/luciasauer/algorithmic_pricing_llms/blob/main/LICENSE); [paper rights](https://arxiv.org/abs/2404.00806)
- **[Not verified] No-paid-API feasibility:** Local game mechanics are distinct from model generation, but reproducing the LLM results requires the model route used by the study; an all-local no-cost reproduction was not verified.

### R7. Agrawal et al. — LLM collusion in double auctions

- **[Verified fact] Source/date:** [Paper](https://arxiv.org/abs/2507.01413), submitted 2025-07-02; [code](https://github.com/andyjliu/llm-agent-collusion), initial repository commit 2025-07-08; inspected 2026-10-17.
- **[Verified fact] Key claim:** The paper studies seller communication, model choice, oversight, and urgency in continuous double auctions, and reports that communication and environmental pressure influence collusive behaviour. [Paper](https://arxiv.org/abs/2507.01413)
- **[Verified fact] License:** The paper page displays CC BY 4.0. The inspected code repository has no `LICENSE` file; do not assume permission to reuse it. [Paper](https://arxiv.org/abs/2507.01413); [repository](https://github.com/andyjliu/llm-agent-collusion); [LICENSE path check](https://github.com/andyjliu/llm-agent-collusion/blob/main/LICENSE)
- **[Verified fact] No-paid-API feasibility:** The repository README asks users to configure OpenAI, Anthropic, and OpenRouter API keys; its model defaults are hosted LLMs. It is not a documented no-paid-API path. [Repository README](https://github.com/andyjliu/llm-agent-collusion)

### R8. Rippin et al. — compatible schemes and Schelling salience

- **[Verified fact] Source/date:** [Paper](https://arxiv.org/abs/2606.28425), submitted 2026-06-25; inspected 2026-10-17.
- **[Verified fact] Key claim:** The paper frames tacit steganographic coordination as a Schelling-point problem. Its abstract reports broad convergence on scheme families but limited strict one-shot coordination, with shared artifacts, repeated interaction, and tool-mediated search identified as more concerning settings. This is directly relevant to the common-cause/independent-similarity side of the proposed audit question. [Paper](https://arxiv.org/abs/2606.28425)
- **[Verified fact] License:** The arXiv page shows non-exclusive distribution terms; no separate permissive license is inferred. [Paper rights](https://arxiv.org/abs/2606.28425)
- **[Not verified] No-paid-API feasibility:** This is a paper, not a runnable benchmark; no author code was linked from the inspected arXiv record.

## Apart project precedents (not peer-reviewed literature)

### P1. “Loyal Lies” — Secret Loyalties Hackathon, July 2026

- **[Verified fact] Result/status:** Apart lists the project as first place; the project page links a report and GitHub repository. [Sprint results](https://apartresearch.com/sprints/secret-loyalties-hackathon-2026-07-24-to-2026-07-26); [project page](https://apartresearch.com/sprints/projects/loyal-lies-auditing-secret-loyalties-under-attack-and-the-falsepositive-problem-in-blind-elicitation-ezwb)
- **[Verified fact] Claim/design in the authors’ report:** The authors report that clean fine-tuning/exposure controls exposed confounds in several probes; a blind audit generated false accusations; a grey-box method worked on their model organisms; and an obfuscation attack defeated one targeted channel while a different un-attacked channel remained. Reviewer comments praise the decoy controls and attempts to break the proposed method, while criticizing a pre-specified behavior-gate inconsistency and recommending narrower claims. [Project report/reviews](https://apartresearch.com/sprints/projects/loyal-lies-auditing-secret-loyalties-under-attack-and-the-falsepositive-problem-in-blind-elicitation-ezwb)
- **[Verified fact] License:** The linked GitHub repository has an MIT license. [Repository LICENSE](https://github.com/PotatoChoudhary/loyal-lies/blob/main/LICENSE)
- **[Not verified] No-paid-API feasibility:** The repository contains result artifacts, but complete reproduction depends on model artifacts/compute that are not all present in the repository; a laptop/CPU reproduction was not established. [Repository README](https://github.com/PotatoChoudhary/loyal-lies)

### P2. “Omission Attacks” — AI Control Hackathon, March 2026

- **[Verified fact] Result/status:** Apart lists the project as first place; its public project page links the report and reviews. [Sprint results](https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22); [project page](https://apartresearch.com/sprints/projects/omission-attacks-when-doing-nothing-is-the-attack-0y1v)
- **[Verified fact] Claim/design in the authors’ report:** The report defines an omission attack, gives a taxonomy and test traces, compares monitor behaviour, and proposes a postcondition monitor; reviewers praise the operationalization but request repeated/larger runs, false-positive analysis, and broader validation. [Project page/reviews](https://apartresearch.com/sprints/projects/omission-attacks-when-doing-nothing-is-the-attack-0y1v)
- **[Not verified] License / runnability:** The inspected project page does not state a report license or provide a code link; no standalone reproduction route was verified.

## Initial synthesis for Phase 2

- **[Verified fact]** The organizer’s own brief already names innocent parallel conduct/shared Schelling salience, conversation/action disagreement, and positive/negative controls as important parts of Track 2.3; Colosseum supplies complementary communication and action measures, while ColludeBench advertises a broader detector/benchmark suite. [Official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25); [Colosseum](https://arxiv.org/abs/2602.15198); [ColludeBench paper](https://arxiv.org/abs/2510.04303)
- **[Statistical interpretation]** The source inventory suggests the useful comparison is not simply “new score versus old score”: evidence labels and ground truth differ across benchmarks, and many starter runs assume hosted API calls. This is a design warning, not yet a novelty conclusion.
- **[Hypothesis]** A defensible contribution, if any, will likely need to define exactly what the detector is predicting (observable coordination, coalition advantage, deliberate mechanism, harmful outcome, or intent) and make shared-incentive independent behaviour an explicit negative control rather than treating correlation as collusion.
- **[Future work]** Phase 2 will search for additional common-cause, behavioral-similarity, conditional-dependence, supervised trajectory-feature, benchmark-baseline, and antitrust-plus-factor methods; verify current license/data status; then compare at least three project directions against explicit feasibility and evidence criteria.

## Execution record

- **[Experimental observation]** No paper benchmark, repository test, model, API, or detector was executed in Phase 1.
- **[Verified fact]** Static workspace inspection found the current checkout is `/home/user/AI-collusion-sprint` on `arena/00a1b645-ai-collusion-sprint`, with only a two-line `README.md` tracked at the root. [Workspace `README.md`](../README.md)
- **[Not verified]** The separate user-mentioned repository [`Rohit4507/GCG_Implementation_Beginners`](https://github.com/Rohit4507/GCG_Implementation_Beginners) is not the checked-out repository and was not fetched or inspected in this phase.
