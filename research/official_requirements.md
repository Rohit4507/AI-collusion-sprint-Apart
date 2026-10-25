# Phase 1 — Current official requirements audit

**Rechecked: 2026-10-25, Asia/Calcutta.** This section supersedes conflicting statements in the historical audit below. No detector code or benchmark execution was performed in this Phase 1 recheck.

## Sources actually retrieved in this recheck

- **[Verified fact — source]** [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25), Overview, Resources, Guidelines and FAQ, retrieved 2026-10-25.
- **[Verified fact — source]** [Official template](https://docs.google.com/document/d/1Y5wd3VRbXU5N08BvAGiJUQTaWbMCSPjhzXsR-ozuehg/export?format=html), retrieved 2026-10-25.
- **[Verified fact — source]** [Submission/prize terms](https://apartresearch.com/sprints/prize-terms), retrieved 2026-10-25.

## Current submission requirements

Every verified rule in this section is from the official sprint page above unless another source is named.

- **[Verified fact]** Tracks: Markets and Collusion; Detection and Audit of Collusion; Collusion Carriers and Countermeasures. Track 2 questions cover task types, messages plus actions, and standards of convincing evidence. Tracks share the same rubric.
- **[Verified fact]** Deadline: October 25, 2026, 23:59 Anywhere on Earth. **[Verified fact — arithmetic]** Using AoE UTC−12 and IST UTC+05:30 gives October 26, 2026, **17:29 IST**. This is a conversion, not an India-specific statement printed by the organizer.
- **[Verified fact]** Required report: PDF using the official template, **maximum 8 pages excluding references and appendices**, title, **150–250-word abstract**, author names and affiliations, and a **Limitations and Dual-Use / Ethical Considerations** appendix. The form accepts PDF up to 25 MB.
- **[Verified fact]** Public code and a 3–5-minute video are optional. The template supports adaptable section structure and recommends four pages; this recommendation does not override the sprint's eight-page cap.
- **[Verified fact]** The form includes title, summary, publishing-interest question, tracks, team name/location and member name/email; optional fields include code, recording, slides, image and additional material. Current retrieved page says “Live now” and exposes submission controls.
- **[Not verified]** End-to-end submission acceptance was not tested; no form was submitted. Prior closed-widget observations below are historical, not the current page-state finding.
- **[Verified fact]** Solo entry is allowed; teams up to five recommended, larger groups allowed; at most two projects per person. Global remote participation is allowed. Unfinished work may be submitted with honest limitations.
- **[Verified fact]** Preexisting code must be marked in README and report; new sprint contributions must be identified. Undisclosed prior work can lead to disqualification.
- **[Verified fact]** AI tools may help reasoning, coding, debugging and writing; the team remains responsible for all content. Fabricated references/results can disqualify a project. The template requests an LLM Usage Statement and strongly encourages primarily team-written final text.
- **[Future work]** Maintain a truthful contribution/time ledger and disclose AI assistance; do not claim independent verification for checks the author has not performed.
- **[Verified fact]** Correcting form metadata with the same title does not replace the PDF. For a changed PDF, submit with a slightly different title or email the new PDF before the deadline. Confirmation should arrive shortly; contact sprints@apartresearch.com if absent.

## Rubric and practical implications

- **[Verified fact]** Three dimensions, each scored 1–5: **Impact Potential & Innovation**, **Execution Quality**, **Presentation & Clarity**. High scores emphasize original important work, convincing validation and clearly supported conclusions, and accessible presentation. Individual judge scores are internal. No aggregation weights were established from the inspected page.
- **[Hypothesis]** A narrow, verified contribution with explicit negative controls is more defensible than a broad unvalidated “collusion detector”; this is a research strategy, not a predicted competition outcome.

## Licensing and compute

- **[Verified fact — terms]** Authors retain copyright and grant Apart a worldwide, nonexclusive, royalty-free license to store, publish, share and process submissions, including with AI tools, for judging, promotion, programs and tool development. Submission confirms named members agree. This does not itself supply a public open-source license.
- **[Not verified]** No mandatory public software/data license was established. Third-party code, model and data rights require separate checking.
- **[Verified fact]** Current overview offers Modal credits of $250 per person at the New York hub and $50 for other participants; older claims below about hub-only credits are superseded.
- **[Hypothesis]** Keep the Rs 0 project independent of promotional credits and hosted models. CPU-compatible offline analysis or small scripted controls remain plausible; GPU-local end-to-end benchmark feasibility is not yet demonstrated.

## Resources and past-project evidence

- **[Verified fact]** Resources explicitly recommend Colosseum and ColludeBench for Track 2.3. They warn ColludeBench should be preflighted, not treated as a turnkey raw-trajectory dataset. Track 2.3 already proposes coordinated harmful action, shared-incentive similarity without agreement, and talk without changed behavior. Thus the general candidate framing is not by itself novel.
- **[Verified fact]** Colosseum current README documents local Qwen2.5-7B/vLLM as well as API runs, and warns Terrarium 0.2.x changes behavior relative to the paper tag. See the refreshed related-work inventory.
- **[Verified fact]** [March AI Control results](https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22) list Omission Attacks first. Its [project reviews](https://apartresearch.com/sprints/projects/omission-attacks-when-doing-nothing-is-the-attack-0y1v) praise operationalization/artifacts but ask for larger repeated evaluations and question task-specific overfitting.
- **[Verified fact]** [Loyal Lies public reviews](https://apartresearch.com/sprints/projects/loyal-lies-auditing-secret-loyalties-under-attack-and-the-falsepositive-problem-in-blind-elicitation-ezwb) praise decoy controls and attacking the team's own detector, but criticize inconsistent enforcement of a prespecified behavioral gate and overbroad evasion framing. These are source-reported critiques, not reproduced results.
- **[Statistical interpretation]** Two selectively visible projects cannot establish which features caused high scores; individual scores are not public. Use these as qualitative design lessons, not a winning recipe.

## Phase checklist

- **[Verified fact] Done:** current official requirements, template, terms, recommended benchmark documentation and two past-project review pages checked.
- **[Not verified] Remaining:** actual submission transaction, complete benchmark reproduction, third-party data availability/rights and 6 GB hardware feasibility.
- **[Future work] Next:** Phase 2, refresh the three-direction novelty/feasibility matrix before choosing or changing any detector implementation.

---

## Historical audit — retained for provenance, not current requirements

**[Not verified in this recheck]** The historical entries below retain their original dates and source claims. Conflicts with the current section must not be used as submission instructions.

# Phase 1 — Official sprint requirements audit

- **Audit date:** 2026-10-17 (UTC)
- **Primary source:** [Apart Research — AI Collusion Research Sprint](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
**Scope:** Official page, its linked submission template and prize terms, organizer-linked Colosseum/ColludeBench materials, and a small set of public past Apart sprint projects. No experiment, benchmark run, model call, or detector implementation was performed in this phase.

## Evidence labels

- **[Verified fact]** Directly stated in a linked official/source document or directly visible in the checked-out repository; source linked in the same item.
- **[Experimental observation]** An observation from an experiment or test actually run. None are reported in this document.
- **[Statistical interpretation]** A statistical interpretation of measured data. None are reported in this document.
- **[Hypothesis]** An explicitly tentative explanation or recommendation, not an official rule.
- **[Future work]** A check or action still to perform.
- **[Not verified]** An item that could not be established from the inspected sources or was not executed.

## 1. Tracks and project scope

- **[Verified fact]** The sprint has three tracks: **(1) Markets and Collusion**, **(2) Detection and Audit of Collusion**, and **(3) Collusion Carriers and Countermeasures**. The official page says projects may fit more than one track and that all tracks use the same judging rubric. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** Track 1 asks which conditions cause market collusion, whether collusion survives participant replacement, whether existing detection can be improved, whether information-theoretic methods can help, and which restriction best reduces collusion per cost. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** Track 2 asks which non-market tasks lead to collusion, whether combining agents’ statements and actions improves detection, and what should count as convincing evidence of collusion. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** Track 3 asks whether actions/tools/side channels can carry coordination, whether trusted agents can disrupt it, whether agents recognize peers, and how coalitions respond to monitoring. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** The official Track 2.3 brief explicitly asks for evidence that distinguishes deliberate coalitions from innocent parallel behaviour, collusive-sounding talk without changed behaviour, and harmful outcomes without agreement. It points to antitrust “plus-factors” as an analogy, and recommends Colosseum and ColludeBench as starter resources. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Hypothesis]** The user's preferred Detection and Audit track is an especially direct fit for the stated question “what should count as convincing evidence,” but that fit alone does not establish novelty; novelty is reserved for Phase 2.

## 2. Dates, deadline, and participation

- **[Verified fact]** The sprint is scheduled for Friday, October 23 through Sunday, October 25, 2026; remote participation is allowed, with optional in-person hubs listed by the organizer. The official submission deadline is Sunday, October 25, 2026, at **11:59 PM Anywhere on Earth (AoE)**. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** AoE is UTC−12; converting 23:59 AoE on Oct 25 to UTC+05:30 gives **17:29 IST on Monday, October 26**. This is a time-zone calculation, not a separately printed India deadline. [AoE definition](https://www.timeanddate.com/time/zones/aoe); [official deadline](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** Individuals may participate solo; teams of one to five are recommended, and the page says larger teams are allowed. No prior AI-safety background is required, and attendance for all three days is not required. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** The official page says participating in-person teams at participating hubs receive $250 per team in Modal credit; it does not promise this credit to remote participants. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)

## 3. Submission format and eligible artifacts

- **[Verified fact]** Required submission items are a research report PDF using the official template, a project title, an abstract of **150 words or fewer**, author names and affiliations, and a required appendix titled **“Limitations and Dual-Use / Ethical Considerations.”** Submission is through the form on the sprint page. [Official sprint Guidelines](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25); [official template](https://docs.google.com/document/d/1Y5wd3VRbXU5N08BvAGiJUQTaWbMCSPjhzXsR-ozuehg/copy?usp=sharing)
- **[Verified fact]** The project form asks for project title, a short project summary, PDF report (up to 25 MB), track selection, team name/location, and team-member details. It also exposes fields for presentation recording, code, slides, project image, and additional material. [Official sprint page / submission form](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** A public GitHub repository and a 3–5 minute video demo are described as optional on the Guidelines tab. The project form likewise presents code and presentation-related fields without marking them required. [Official sprint Guidelines](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** The report guidance recommends an introduction, related work, reproducible methodology, quantitative results where possible (including variance, seeds, baselines, and a positive control), discussion/limitations, the required dual-use appendix, and references. The template calls four pages (excluding references and appendix) a recommended length; the sprint page says most strong projects are 4–8 pages. [Official sprint Guidelines](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25); [official template](https://docs.google.com/document/d/1Y5wd3VRbXU5N08BvAGiJUQTaWbMCSPjhzXsR-ozuehg/copy?usp=sharing)
- **[Verified fact]** The sprint page and linked template conflict on abstract length: the event Guidelines specify **≤150 words**, while the template guidance says **150–250 words**. [Official sprint Guidelines](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25); [official template](https://docs.google.com/document/d/1Y5wd3VRbXU5N08BvAGiJUQTaWbMCSPjhzXsR-ozuehg/copy?usp=sharing)
- **[Hypothesis]** In the absence of clarification, using **≤150 words** is the safer choice because it satisfies the explicit sprint-page limit, even though the template’s own guidance differs.
- **[Not verified]** The sprint page does not state a hard maximum page count. The 4-page and 4–8-page statements are recommendations, not a confirmed maximum.

## 4. Judging rubric

- **[Verified fact]** The published rubric has three 1–5 dimensions: **Impact Potential & Innovation** (importance and novelty), **Execution Quality** (soundness of methods, implementation, findings), and **Presentation & Clarity** (communication of work, findings, and impact). The page gives score descriptors for each dimension. [Official sprint Guidelines](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** The official FAQ says tracks orient the project but do not alter scoring; submissions compete under the same rubric. [Official sprint FAQ](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Not verified]** No weighting scheme among the three dimensions is published on the page inspected; do not assume equal or weighted aggregation.

## 5. Authorship, prior work, and AI use

- **[Verified fact]** Solo participation is allowed. The report must identify authors and affiliations. Building on existing research is allowed and encouraged, but the team must clearly identify the work that is new during the sprint; the page warns that undisclosed prior work can lead to disqualification. [Official sprint Guidelines/FAQ](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** The organizer permits AI tools as a colleague-like aid for checking reasoning, finding gaps, and debugging. The report must be the team's own writing about its own work; generic/padded AI-like prose and unsupported claims may not be scored, and factual claims should be linked to sources. [Official sprint Guidelines](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** The linked template contains an **LLM Usage Statement** section asking teams that used LLM assistance during project development or report writing to briefly describe how, verify claims/results, and keep the final report primarily team-written. [Official template](https://docs.google.com/document/d/1Y5wd3VRbXU5N08BvAGiJUQTaWbMCSPjhzXsR-ozuehg/copy?usp=sharing)
- **[Not verified]** The inspected sprint page does not provide a separate, more detailed rule about AI-generated code, prompt disclosure, or ownership of AI-generated text beyond the colleague-use guidance and template statement.

## 6. Licensing and publication

- **[Verified fact]** The page makes a public GitHub repository optional and asks in the form whether the team is interested in publishing its project. [Official sprint page / submission form](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** The linked prize terms cover prize payment logistics; the inspected terms do not state an intellectual-property assignment or a license for submitted reports, source code, or data. [Sprint prize terms](https://apartresearch.com/sprints/prize-terms)
- **[Not verified]** No license for this sprint’s report, code, data, template, or submission was identified in the sprint page, template, or prize terms inspected. This is not a legal conclusion and does not establish permission to reuse third-party artifacts.
- **[Future work]** Before publishing, select and document a license for original code/data and ask the organizer if the “interested in publishing” option implies any separate publication or reuse terms; preserve upstream licenses and attribution for any reused code/data.

## 7. Organizer-recommended Colosseum and ColludeBench preflight

- **[Verified fact]** For Track 2.3 the organizer recommends [Colosseum](https://github.com/umass-ai-safety/colosseum) and the [ColludeBench repository](https://github.com/Ostailor/Steganographic_Collusion). The organizer specifically says ColludeBench should be preflighted and not treated as a turnkey bag of raw trajectories. [Official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** Colosseum’s repository setup uses the Terrarium framework and CoLLAB for some environments; its README says API keys may be required and warns that API usage increases with the number of agents. The default code dependency is `terrarium-agents[providers,science,plots]`. [Colosseum README](https://github.com/umass-ai-safety/colosseum); [Colosseum pyproject](https://github.com/umass-ai-safety/colosseum/blob/main/pyproject.toml)
- **[Verified fact]** The ColludeBench repository is MIT-licensed, includes local compilation/unit-test instructions, and states that hosted Gemini and Groq experiments require API keys. [ColludeBench README](https://github.com/Ostailor/Steganographic_Collusion); [LICENSE](https://github.com/Ostailor/Steganographic_Collusion/blob/main/LICENSE); [CI check](https://github.com/Ostailor/Steganographic_Collusion/blob/main/scripts/ci_check.sh)
- **[Verified fact]** The official resource page estimates approximately $5–$30 for Track 2.3 if cached logs are reused, and up to $100 if trajectories must be generated; it gives an estimated $15–$75 for Colosseum short episodes with one API provider. These are organizer estimates, not measured costs for this project. [Official sprint Resources](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Not verified]** No benchmark repository was installed or run in this phase. A complete offline/no-paid-API reproduction on the participant’s RTX 3050 6 GB laptop is not established.
- **[Hypothesis]** Given the fixed Rs 0 budget, the project should not depend on paid hosted models; a locally scripted positive/negative control or cached, license-cleared logs are more plausible starting points. Whether a suitable public cache exists is a Phase 2/3 check, not yet established.

## 8. Public past-sprint examples (not causal evidence about judging)

- **[Verified fact]** The October 2026 collusion sprint is still upcoming as of this audit date, so no winner or submission for this exact sprint has been verified. [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Verified fact]** At Apart’s July 2026 Secret Loyalties Hackathon, **“Loyal Lies: Auditing Secret Loyalties Under Attack and the False-Positive Problem in Blind Elicitation”** is listed as first place. Its public project report describes clean fine-tune/exposure controls, blind verification, an attack against its own detector, and a counterexample to its initial probe; public reviewer comments praise the controls and self-attack, while also flagging a pre-specified behavior-gate inconsistency on one attack seed and advising narrower claims. [Sprint winner page](https://apartresearch.com/sprints/secret-loyalties-hackathon-2026-07-24-to-2026-07-26); [project report page and reviews](https://apartresearch.com/sprints/projects/loyal-lies-auditing-secret-loyalties-under-attack-and-the-falsepositive-problem-in-blind-elicitation-ezwb)
- **[Verified fact]** At Apart’s March 2026 AI Control Hackathon, **“Omission Attacks: When Doing Nothing Is the Attack”** is listed first place. Its project page reports an explicit attack definition, a taxonomy, attack traces, a baseline-monitor comparison, and a proposed postcondition monitor; public reviews praise the clear operationalization and artifact while asking for larger/repeated runs, false-positive evaluation, and broader validation. [Sprint results](https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22); [project page and reviews](https://apartresearch.com/sprints/projects/omission-attacks-when-doing-nothing-is-the-attack-0y1v)
- **[Statistical interpretation]** These are a small, selectively visible set of projects and reviews, not a causal analysis of judging scores. They support only qualitative design heuristics: operationalize the target, use matched controls, show actual artifacts, make falsification and limitations visible, and avoid claims broader than the tested setting.
- **[Future work]** In later phases, map each planned experiment and report section to the official three-dimension rubric; do not optimize for anecdotes about winners at the expense of valid controls.

## 9. Page-state discrepancy and open items

- **[Verified fact]** The sprint page lists a future October 25 deadline but the retrieved page’s embedded submission form also displays “The submission window has closed.” [Official sprint page](https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25)
- **[Hypothesis]** This may be a pre-event form state, a stale widget, or a retrieval artifact; the inspected page does not explain the contradiction.
- **[Future work]** Recheck the submission page and confirm with the official help desk before the sprint and again well before the deadline; submit with buffer rather than relying on the final hour.
- **[Not verified]** Whether the form will open later, and whether the organizer has any additional unpublished authorship/licensing instructions, remains unverified.

## Phase 1 checklist

- **[Verified fact] Done:** Official tracks, descriptions, dates, AoE deadline, submission format, rubric, authorship/prior-work and AI-use rules, and license-status gap inspected and recorded.
- **[Verified fact] Done:** Organizer-recommended Colosseum and ColludeBench inspected at documentation level; neither was executed.
- **[Verified fact] Done:** Public past Apart project pages/reviews checked for qualitative patterns; causal claims about judging were explicitly avoided.
- **[Not verified] Remaining:** Submission-form availability and any unpublished publication/license terms.
- **[Future work] Next:** Phase 2 novelty audit—compare at least three research directions against the named baselines and assess whether the candidate remains defensible under the zero-paid-API constraint.
