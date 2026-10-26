# Human edit guide — DELETE THIS FILE'S CONTENTS FROM THE SUBMISSION (guide only)

Goal: make `final-report.md` genuinely yours. "Humanise" here means **understand and rewrite**, not disguising AI use. The LLM Usage Statement stays. Judges reward a report the author can explain; they punish polished text the author cannot defend.

## Must-fix placeholders (search for `[EDIT`)
1. **EDIT 1/2 — name & affiliation.** Real full name; real affiliation or "Independent researcher". Never invent.
2. **EDIT 3 — your true motivation** (1–2 sentences). Why *you* picked audit/evidence standards. If the honest reason is "zero budget + interest in false positives", say that plainly.
3. **EDIT 4 — your real next step.** One sentence you would actually do with a fellowship/month.
4. **EDIT 5 — LLM Usage Statement.** Read every clause; delete anything not true (e.g. only claim you verified numbers you actually re-checked below).

## Rewrite these first (most "generic AI" sounding if left untouched)
- **Abstract** — rewrite fully in your words. Keep every number identical.
- **Introduction paragraphs 1–2** — say the four-questions idea the way *you* would explain it to a friend.
- **Related work** — shorten. One honest sentence per paper; delete any you cannot summarise from memory.
- **Section 5 (Synthesis) and Conclusion** — this is your argument; it must sound like you believe it because you ran the work.

Methods/results paragraphs can stay close to the draft **only after** you check each sentence against code/outputs.

## The 20-minute humanising method (per section)
1. Read the section once.
2. Cover it. Say out loud what it means.
3. Type what you just said. Then compare numbers.
4. Cut any sentence you cannot explain. Shorten sentences over ~25 words.
5. Replace stock transitions ("Together, the results...", "deliberately different testbeds") with your plainer wording where they feel borrowed.

## Numbers you must personally verify before submitting (tick them off)
- [ ] Scripted: 35/500 vs 0/500; +7.0 pp [4.8, 9.2]; CMI 500/500 stochastic, 0/500 deterministic; hidden-common 486/500.
- [ ] SALT: 49 pairs; sequence 22 excluded; 82.24% vs 85.10%; +2.86 pp [-0.41, +7.14]; false approvals 54/72 vs 53/72.
- [ ] Classifiers: action AUC 0.601 (13/49, 8/49); message 1.000 (49/49, 11/49); combined 1.000 (49/49, 14/49).
- [ ] Input manifest hash starts `1db8d18b`.

Sources: `results/observability-v1/summary.json`, `results/metrics.csv`, and your local `outputs/controlled-peer-audit-a3/summary.json`.

## Explain-back test (if you cannot answer, simplify the text until you can)
1. Common cause vs channel in one sentence each?
2. Why is CMI exactly 0 for the deterministic channel?
3. Why did MI flag nothing stochastic at test (threshold vs noise shift)?
4. Why did A1 stop the first SALT run, and what exactly did A3 change?
5. Why does AUC 1.00 *not* mean collusion detection?
6. Why is the primary SALT result inconclusive, not "no effect"?

## Do NOT
- Remove/weaken the AI Usage Statement or the sequence-22 disclosure.
- Claim "significant" for +2.86 pp; claim LLM collusion/intent detection; hide the scripted primary failure.
- Submit with any `[EDIT` text remaining — final search before export.
- Paste the draft unchanged into the template and call it human-written.
