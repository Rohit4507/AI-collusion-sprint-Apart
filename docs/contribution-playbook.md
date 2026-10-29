# From zero to merged — a step-by-step contribution plan

**Built on:** your 28 Oct 2026 opportunities roadmap · **Re-verified live on:** 29 Oct 2026 (Thursday)
**Owner:** Rohit Singh Rajput · **Horizon:** 29 Oct 2026 → 19 Feb 2027 (GSoC org announcement)

Every issue number, label and date below was checked against the GitHub API or the upstream
`CONTRIBUTING` file on **29 Oct 2026**. Where the roadmap and reality now disagree, §0 says so.

---

## 0. Read this first — five corrections to your roadmap

| # | Roadmap said | Reality on 29 Oct 2026 | What to do |
|---|---|---|---|
| 1 | Start with **opencv/opencv** "good first issues" (primary pick) | OpenCV has the `good first issue` label but **0 open issues** carrying it (2,858 issues open in total) | Demote OpenCV to a *long game* (GSoC proposal, Feb 2027). Do **not** spend your first 72 hours there |
| 2 | **huggingface/transformers** "Good Second Issue" queue | `Good First Issue` = **0 open**, `Good First Documentation Issue` = **0 open**, `Good Second Issue` = **9 open** | Only reachable path today: a real docs PR you open directly (allowed by their CONTRIBUTING) or one of the 9 second-issues |
| 3 | Hacktoberfest: "one PR is enough this week" | Ends **Sat 31 Oct**, i.e. **2 days**. HF is opted in (repo topic `hacktoberfest`) | Only worth it if you start **today/tomorrow** in a repo with a live queue (lm-eval / scorecard / transformers docs) |
| 4 | "You are 0 for 2 on merged PRs **and** a public write-up" | **1 of 2 is done.** This repository *is* the write-up: `report/study.md`, a PDF draft, 42 passing tests, REUSE-compliant dual licensing | Stop planning a new 2,500-word essay. Spend 2 hours distributing the artifact you already have (§4) |
| 5 | OpenSSF winter/spring dates were "from the funding issue" | Funding issue [`ossf/tac#671`](https://github.com/ossf/tac/issues/671) is still **open, updated today**, $60k / $6k per mentee, winter-spring '27 pilot | Treat 16–30 Nov as *provisional* until LFX publishes. Prepare now, apply the day it opens |

**The one-line consequence:** your on-ramp repos are now **EleutherAI/lm-evaluation-harness**
(15 open `good first issue`) and **ossf/scorecard** (16 open), not OpenCV.

---

## 1. Pick one track (10-minute decision)

| Track | Goal | Repos | Time to first win | Choose if |
|---|---|---|---|---|
| **A — Merge** | 1–3 merged PRs as evidence | lm-evaluation-harness, transformers (docs), scorecard | 2–14 days | You want the fastest "proof I can do this" |
| **B — Paid** | OpenSSF LFX mentee (apps 16–30 Nov, term 18 Jan – 9 Apr) | scorecard / minder / gittuf | 18 days to application | You want money + mentorship this winter |
| **C — Research** | AISC 2027 team, SPAR Spring | your own repo + AISC projects | 15 days (apps open 13 Nov) | You want the safety-research line |

**Recommended sequence — not a choice, a stack:**

```
Today–31 Oct   Track A, one repo only        → first merged PR
1–12 Nov       Track A, second PR + §4       → public artifact distributed
13–29 Nov      Track C (AISC application)    ← uses the artifact from §4
16–30 Nov      Track B (OpenSSF application) ← uses the PRs from §3
Dec–Feb        SPAR → GSoC → LFX Term 1
```

> **Hard rule from your own roadmap, restated:** 3–6 merged PRs in **one** org beats 20 PRs across
> 20 orgs. Mentors read consistency. Pick **eleutherAI/lm-evaluation-harness** and stay 8–10 weeks.

---

## 2. Phase 0 — one-time setup (≈60 min, do it now)

### Step 2.1 — Toolchain (15 min)

```bash
git config --global user.name  "Rohit Singh Rajput"
git config --global user.email "your-github-email@example.com"
git config --global init.defaultBranch main
gh auth status                     # must show you logged in
ssh -T git@github.com              # "Hi Rohit4507!" = good; add a key if not
```

Use **SSH for pushes to your own repos**, but note: for pull requests to other people's repos you
push to *your fork*, so SSH works everywhere.

### Step 2.2 — Make your own repo look contributable (20 min)

Right now `AI-collusion-sprint-Apart` has **0 stars, 0 forks, no topics, no `CONTRIBUTING.md`**.
That reads as "private research dump", and AISC/SPAR reviewers click through. Fix it with four commands:

```bash
# 1. Topics — how anyone finds a repo at all
gh api -X PUT repos/Rohit4507/AI-collusion-sprint-Apart/topics \
  -f names[]=ai-safety -f names[]=ai-collusion -f names[]=reproducibility \
  -f names[]=evaluation -f names[]=audit -f names[]=research

# 2. Description
gh repo edit Rohit4507/AI-collusion-sprint-Apart \
  --description "Scripted stress tests + a controlled-peer audit of what counts as evidence of coordination between LLM agents" \
  --add-topic mutual-information

# 3. Discussions on (for questions you don't want as issues)
gh api -X PATCH repos/Rohit4507/AI-collusion-sprint-Apart -f has_discussions=true

# 4. A CONTRIBUTING.md is the missing file — see Step 2.3
```

### Step 2.3 — Add `CONTRIBUTING.md` + 3 starter issues (25 min)

A contributor-facing repo needs a stated on-ramp. Create `CONTRIBUTING.md` with: how to run the
42 tests, the ruff commands CI enforces, the dual-license split (code MIT / docs CC-BY-4.0),
and the dual-use rule ("scores are not evidence of culpability"). Then open three real issues on
yourself, labelled `good first issue`:

- one **docs** task (e.g. "Document the A3 amendment rationale in `research/experimental_design.md`")
- one **test** task (e.g. "Add a synthetic-fixture test for a malformed episode manifest")
- one **reproducibility** task (e.g. "Add a `--seed` smoke test to `scripts/reproduce_observability.sh`")

```bash
gh label create "good first issue" -R Rohit4507/AI-collusion-sprint-Apart --color 7057ff
gh issue create -R Rohit4507/AI-collusion-sprint-Apart \
  --title "Docs: explain the A3 amendment in experimental_design.md" \
  --label "good first issue" --body "Cross-link A1/A2/A3 and state why exclusion is whole-pair."
```

**Verified baseline for all three** — I ran this on your branch today, so you can quote it:

```
python -m ruff format --check analysis tests   → 8 files already formatted
python -m ruff check analysis tests            → All checks passed!
python -m unittest discover -s tests           → Ran 42 tests … OK
```

---

## 3. Phase 1 — first merged PR (do before Sat 31 Oct)

### Step 3.1 — Choose the repo, then the issue

| Repo | Queue today | Language | Extras that bite you |
|---|---:|---|---|
| **EleutherAI/lm-evaluation-harness** | **15** open `good first issue` | Python | **CLA required** on first PR (`@CLAassistant` comment) |
| **ossf/scorecard** | **16** open `good first issue` | Go | **DCO**: every commit needs `-s` |
| **gittuf/gittuf** | 4 open | Go | Go + TUF concepts |
| huggingface/transformers | 0 first / 9 second | Python | **Agentic-contribution policy** (§3.6) |
| ultralytics/ultralytics | 0 open | Python | Queue empty; PRs get closed without a linked issue |

**Recommended pick for you:** `EleutherAI/lm-evaluation-harness` **#2552** —
*"Hendrycks Math extraction rule seems too strict"*. It is a self-contained regex/answer-extraction
change with an obvious test, it uses the eval-debugging skill your StyleSim work already proves,
and it is exactly the class of bug maintainers merge without hesitation.

Alternates from the same queue: **#1454** (`log_samples` filename too long → truncation),
**#3224** (long-context benchmark support — bigger, reserve for PR #2).

### Step 3.2 — Claim it before you code (10 min)

Comment on the issue. **Never** write "Hi, I'm a GSoC aspirant, please guide me" — OpenCV has
closed exactly that kind of issue as `not planned`. Claim with a diagnosis, not an introduction.

Shape to copy (**fill in your own repro** — read the code first, then write this; do not post a
diagnosis you have not run):

> I can take this. Reproduced on `<commit>`: `<one command>` prints `<observed>`, expected `<wanted>`.
> Cause looks like `<file>:<line>` — `<one sentence>`. Plan: `<2–3 bullets>`, plus a unit test at
> `<path>`. I'll open a draft PR this week; say if you'd rather `<the shared path>` stay untouched.

Then wait, but don't idle: build the repo (next step) while you wait.

### Step 3.3 — Fork, clone, install (30–60 min, mostly downloads)

```bash
gh repo fork EleutherAI/lm-evaluation-harness --clone --remote
cd lm-evaluation-harness
git remote -v                     # origin = your fork, upstream = EleutherAI
python3 -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
pre-commit install                # ruff is enforced through pre-commit here
python -m pytest -q --ignore=tests/models   # confirm green BEFORE you change anything
```

> A clean baseline is proof, not politeness. If a test is already red, say so in the issue — that
> alone is a useful contribution.

### Step 3.4 — Branch, reproduce, fix

```bash
git checkout -b fix/<short-slug>
# reproduce FIRST, in the smallest possible command — quote it verbatim in the issue and the PR.
# For a scoring/extraction bug that is usually one function call:
python -c "from <module> import <fn>; print(<fn>(<bad input>, <expected>))"   # → False before the fix
```

Find `<module>`/`<fn>` by grepping the repo (`grep -rn "def is_equiv\|boxed" lm_eval/tasks/`),
not by assuming a path — task layouts move between releases.

Rules for the patch itself:

1. **Smallest change that fixes the reported behaviour.** No drive-by refactors, no formatting churn.
2. **One test that fails before and passes after.** Put it where the repo already keeps that kind of test.
3. **No new dependency** unless the issue explicitly asks for one.
4. **Update docs** if behaviour is user-visible (`docs/task_guide.md`).

### Step 3.5 — Test, lint, commit, push

```bash
python -m pytest -q tests/ -k "<your test name or module>"   # your new test + neighbours
pre-commit run --all-files                                    # ruff + hygiene
git add -A
git commit -s -m "fix(<scope>): <what changed, one line>"
git push -u origin fix/<short-slug>
```

`-s` costs nothing and covers you in DCO repos (scorecard **requires** it; LF projects expect it).

### Step 3.6 — Open the PR (5 min, decides everything)

Write the description in four blocks. This exact shape satisfies both HF's agentic policy and
EleutherAI's "scope and intent" requirement. (Numbers below are from the worked example — replace
every one with output you actually ran.)

```markdown
## What
`is_equiv` rejects `\boxed{\frac{1}{2}}`; only a trailing-period form matched.

## Why
Breaks `hendrycks_math` scoring on models that follow the paper's boxed-answer format (#2552).

## How
Relaxed the extraction regex to accept balanced-brace `\boxed{...}`. `minerva_math` untouched;
added `test_boxed_nested_braces` (fails on `main`, passes here).

## Verification
- `python -m pytest -q tests/ -k "math"` → 14 passed
- `is_equiv(r'\frac{1}{2}', r'\boxed{\frac{1}{2}}')` → True
- Upstream behaviour unchanged for period-form answers (existing tests pass)

## AI assistance
Drafted with AI tooling; every line reviewed and all commands above run locally by me.
Fixes #2552.
```

**Then:** draft PR if the issue is still under discussion, ready-for-review when the maintainer
replies. Respond within 24 h. Never force-push after review starts — add commits, or ask before
squashing. One reviewer request, no @-everyone.

### Step 3.7 — If nothing happens in 7 days

```markdown
Gentle ping — is the approach in the description the one you want, or should the fix live in
`minerva_math`'s shared util instead? Happy to rework; no rush on review.
```

One ping at day 7, one at day 14. Then move on and leave the PR open. A polite, rebased PR that
sits is not a failure; chasing reviewers is.

### Step 3.8 — Repo-specific traps

| Repo | Trap | What you must do |
|---|---|---|
| **lm-evaluation-harness** | First PR triggers `@CLAassistant` | Reply to that comment to sign the CLA, or it never merges |
| **ossf/scorecard** | DCO enforced by CI | `git commit -s` on **every** commit; run `make all` (unit tests + lint + fmt + mod tidy) |
| **transformers** | **"Do not submit 'pure agent' PRs."** AI-assisted is welcome but must be coordinated, scoped, verified; disclose AI use, add a coordination link, and differentiate from existing PRs. "Avoid one-off 'busywork' PRs (single typo, isolated style cleanup)." | Read `AGENTS.md` + `CONTRIBUTING.md` first, get maintainer ack on the issue, then PR. Your 0-issue docs PR will be closed |
| **opencv/opencv** | Queue empty; "please guide me" issues get closed | Only PR against a real bug you can reproduce, or wait for the Feb 2027 GSoC window |
| **ultralytics** | Template-driven, PR without linked issue closed | Search issues for the exact bug, comment first |

---

## 4. Phase 2 (1–12 Nov) — distribute the artifact you already own

You do not need a new research project. You need a **public landing page** for this repo.
Two hours, four steps:

1. **Extract** a 900-word post from what exists: `README.md` §"In 30 seconds" + the two results
   tables + `report/study.md` limitations. Do not add new claims.
2. **Publish** it as a GitHub *Discussion* or a `blog/` markdown file, then cross-post to LessWrong
   with a single link back to the repo and the PDF.
3. **Point the resume at it**: one line — repo + PR link + "67-pp apparent coordination gap shown
   to be arithmetic; +2.86 pp paired effect, not significant".
4. **Re-tell it once** in the AISC lead email (§6.1) and once in the OpenSSF application. Same
   story, three audiences.

> Why this beats a new essay: reviewers check *does the artifact exist and can I verify a claim in
> 60 seconds*. Your repo passes that test today; it just has zero distribution. Distribution is
> the whole gap.

---

## 5. Phase 3 — the two applications

### 5.1 AISC 2027 (opens **Fri 13 Nov**, closes **Sun 29 Nov**)

- **13 Nov:** project list appears → shortlist exactly **2** teams whose projects touch
  multi-agent behaviour, detection, or evaluation.
- **14–16 Nov:** email both leads (§6.2). Attach nothing; link the repo and one result.
- **Before 29 Nov:** submit the team-member application. Review is rolling — day-one matters.
- Your ticket: this repo (scripted stress test + controlled-peer audit) is unusual for an
  undergraduate applicant. Lead with the negative result, not the tooling.

### 5.2 OpenSSF LFX winter/spring '27 (apps **16–30 Nov**, term 18 Jan – 9 Apr)

- **Provisional** until LFX publishes — the dates come from funding issue `ossf/tac#671`
  (still open, updated 29 Oct). Re-check the portal on 16 Nov.
- Pick **one** project: `scorecard` (Go, 16 open good-first-issues, DCO) or `gittuf`.
- Before 16 Nov: one merged PR or one substantive issue comment in that exact repo. §3 is your
  playbook; substitute the repo.

---

## 6. Phase 4 (Dec → Feb) — the long game

| When | What | What must already exist |
|---|---|---|
| ~1 Dec | SPAR Spring 2027 opens — apply day one (rolling review) | Published write-up (§4) |
| Dec–Jan | 2 more merged PRs in **lm-evaluation-harness** | Track A discipline |
| ~mid/late Feb | GSoC 2027 org list; proposals mid/late Mar | 3–6 merged PRs in the org you apply to |
| ~Feb | LFX Term 1 (`~3–16 Feb`, **proposed**, CNCF issue) | One PR in that project's repo |
| ~Apr | C4GT DMP apps (₹1,00,000) | Prior C4GT/Badal issue work |

OpenCV is only worth revisiting for GSoC: by then you need a *reproduced* bug or a Model-Zoo
benchmark PR, not a good-first-issue queue that isn't there.

---

## 7. Copy-paste templates

### 7.1 Claim an issue (works in every repo)

```markdown
I'd like to take this. Reproduced on <commit>: <one-line repro command + observed vs expected>.

Plan: <2–3 bullets, files touched, test you'll add>.

Anything you'd rather I keep untouched? Otherwise I'll open a draft PR in <n> days.
```

### 7.2 PR description

Use the four-block skeleton in §3.6, plus:

```markdown
<!-- If the repo has an agentic/AI policy (e.g. transformers): -->
## AI assistance
Drafted with AI tooling. I reviewed every changed line, ran the tests below locally, and I am the
human submitter responsible for this change. Related/differing PRs: #<n> (open) covers <x>; this
one deliberately does not.
```

### 7.3 AISC lead email (≤120 words)

```markdown
Subject: AISC 2027 — <Project title> — undergrad with a completed audit project

Hi <Name>,

I'm applying to <project> for AISC 2027 (12th ed.). I've already built and run the thing your
project would extend: a controlled-peer audit of real LLM traces where the peer-policy effect was
+2.86 pp [−0.41, +7.14] across 49 matched pairs — inconclusive, and the interesting part is why the
obvious detector still showed a 67-point gap. Repo: <link> (report + tests).

For your project I'd bring <one concrete skill>. Would you be open to a 15-minute call before
applications close on 29 Nov?

— Rohit Singh Rajput, B.Tech NIT Agartala
```

---

## 8. What decides merge vs closed

| Do | Never |
|---|---|
| One repo, 8–10 weeks, 3–6 merged PRs | 20 forks × 1 PR each |
| Claim the issue with a diagnosis | "Please guide me, I'm a GSoC aspirant" |
| Smallest patch + one failing-then-passing test | Drive-by refactor inside a bugfix |
| `git commit -s`, run the repo's own `make`/`pytest` | Push untested code and let CI find it |
| Disclose AI use *and* verify every line yourself | Submit a pure-agent PR (explicitly disallowed in transformers) |
| Docs PRs that fix something real | Single-typo "busywork" PRs (may be marked invalid in Hacktoberfest) |
| Add commits after review starts | Force-push a branch under review |
| One polite ping at day 7 | @-mentioning maintainers repeatedly |
| Read `CONTRIBUTING.md` + `AGENTS.md` first | Inferring workflow from other repos |

---

## 9. Tracker — fill this in as you go

| # | Repo | Issue | PR | Status | Opened | Merged | Notes |
|---|---|---|---|---|---|---|---|
| 1 | EleutherAI/lm-evaluation-harness | #2552 | | claimed | 29 Oct | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

**Definition of done for PR #1:** linked issue · tests added · repo's lint/test commands run and
quoted · CI green · reviewer replied · merged or explicitly declined with a reason you understood.

---

## Appendix A — verified queues on 29 Oct 2026

### EleutherAI/lm-evaluation-harness — `good first issue` (15 open)

| Issue | Title | Comments |
|---|---|---:|
| [#2552](https://github.com/EleutherAI/lm-evaluation-harness/issues/2552) | Hendrycks Math extraction rule seems too strict | 4 |
| [#1454](https://github.com/EleutherAI/lm-evaluation-harness/issues/1454) | `log_samples` File name too long. Need truncation or override | 1 |
| [#1457](https://github.com/EleutherAI/lm-evaluation-harness/issues/1457) | Allow `--include_path` to import an externally-defined LM subclass | 1 |
| [#1231](https://github.com/EleutherAI/lm-evaluation-harness/issues/1231) | CoQA implementation only predicts the last answer of each text | 2 |
| [#1613](https://github.com/EleutherAI/lm-evaluation-harness/issues/1613) | Add better test coverage for models | 7 |
| [#1883](https://github.com/EleutherAI/lm-evaluation-harness/issues/1883) | Add Regression Testing | 11 |
| [#1558](https://github.com/EleutherAI/lm-evaluation-harness/issues/1558) | Allow Task objects to defer dataset download | 3 |
| [#3224](https://github.com/EleutherAI/lm-evaluation-harness/issues/3224) | Long-context benchmarks (LongBench v2, Babilong, InfiniteBench)? | 7 |
| [#1083](https://github.com/EleutherAI/lm-evaluation-harness/issues/1083) | Add ZeroScrolls Benchmark | 3 |
| [#1013](https://github.com/EleutherAI/lm-evaluation-harness/issues/1013) | [New Task] COLLIE | 1 |
| [#191](https://github.com/EleutherAI/lm-evaluation-harness/issues/191) | Implement XQuAD | 4 |
| [#827](https://github.com/EleutherAI/lm-evaluation-harness/issues/827) | Quac Dataset | 9 |
| [#2557](https://github.com/EleutherAI/lm-evaluation-harness/issues/2557) | Reproduce llama 3 evals | 8 |
| [#1501](https://github.com/EleutherAI/lm-evaluation-harness/issues/1501) | Add New Lambada Translations *(already assigned)* | 3 |
| [#518](https://github.com/EleutherAI/lm-evaluation-harness/issues/518) | Add TheoremQA *(already assigned)* | 5 |

### huggingface/transformers — `Good Second Issue` (9 open; `Good First Issue` = 0)

| Issue | Title | Fit for you |
|---|---|---|
| [#34571](https://github.com/huggingface/transformers/issues/34571) | Configure `stop_strings` in `generation_config.json` | **Best**: small, config-level, testable |
| [#33664](https://github.com/huggingface/transformers/issues/33664) | Object-detection training for OwlViT/OwlV2 | Ties to RoadGuard, but heavy |
| [#35308](https://github.com/huggingface/transformers/issues/35308) | Multi-GPU crash with `IterableDataset` (21 comments) | Contested; read the thread first |
| [#40042](https://github.com/huggingface/transformers/issues/40042) | Support loading `glm4moe` GGUF | Needs GGUF expertise |
| [#42758](https://github.com/huggingface/transformers/issues/42758) | Support Microsoft VibeVoice | Roadmap-sized |
| [#36119](https://github.com/huggingface/transformers/issues/36119) | Whisper `loss_function` migration | Audio, not your stack |
| [#33260](https://github.com/huggingface/transformers/issues/33260) | GGUF for more architectures (52 comments) | Crowded |
| [#17339](https://github.com/huggingface/transformers/issues/17339) | Trillson audio classification | Not your stack |
| [#24295](https://github.com/huggingface/transformers/issues/24295) | EnCodec training support *(assigned)* | Skip |

### Other verified counts

- **ossf/scorecard** — 16 open `good first issue` (Go, DCO required)
- **gittuf/gittuf** — 4 open (`#1220`, `#1219`, `#880`, `#158`)
- **opencv/opencv** — 0 open `good first issue` (label exists)
- **ultralytics/ultralytics** — 0 open `good first issue`
- **deepchem/deepchem** — 0 open `Good First Contribution`

---

## Appendix B — key dates

| Date | Event | Days from 29 Oct |
|---|---|---:|
| **Sat 31 Oct 2026** | Hacktoberfest 2026 closes | 2 |
| **Fri 13 Nov 2026** | AISC 2027 project list + applications open | 15 |
| **Mon 16 Nov 2026** | OpenSSF mentee applications open (provisional) | 18 |
| **Sun 29 Nov 2026** | AISC applications close | 31 |
| **Mon 30 Nov 2026** | OpenSSF applications close (provisional) | 32 |
| ~Dec 2026 | SPAR Spring 2027 opens | ~33 |
| ~3–16 Feb 2027 | LFX Term 1 mentee apps (proposed) | ~100 |
| ~19 Feb 2027 | GSoC 2027 org list | 113 |

---

*This plan supersedes §4 of the 28 Oct roadmap. Re-verify counts with:*
`gh api -X GET search/issues -f q='repo:<org>/<repo> is:issue is:open label:"good first issue"' --jq '.total_count'`
