# Licensing

This repository is **dual-licensed**: code under MIT, documentation and research
outputs under CC-BY-4.0. Third-party material keeps its own notices.

This file explains the split. It is not itself a license — the operative texts
are [`LICENSE`](LICENSE) and [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt),
and the authoritative path→license mapping is [`REUSE.toml`](REUSE.toml).

The [`LICENSE`](LICENSE) file deliberately contains **only** the canonical MIT
text, with no additions, so that GitHub's license detection reports MIT
correctly. Everything that used to be appended there lives here instead.

## Code — MIT

[`LICENSE`](LICENSE) · [`LICENSES/MIT.txt`](LICENSES/MIT.txt)

Copyright (c) 2026 Rohit Singh Rajput.

Covers the software in this repository: the analysis code, tests, scripts,
configuration files, and build/CI metadata.

```
analysis/    configs/    scripts/    tests/
pyproject.toml    REUSE.toml
requirements-analysis.txt    requirements-analysis.lock
requirements-dev.txt    requirements-report.txt
.github/workflows/    .gitignore
```

## Documentation and research outputs — CC-BY-4.0

[`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt)

Copyright (c) 2026 Rohit Singh Rajput. Attribution required on reuse.

Covers the report, research records, figures, and the checked-in result
artifacts. These are research outputs rather than software, so they are
licensed as documentation.

```
README.md    LICENSING.md    analysis/README.md
report/    research/    figures/    results/
```

Attribution for these materials should credit *Rohit Singh Rajput, "What Counts
as Evidence of Coordination?", Apart Research AI Collusion Research Sprint,
October 2026*, with a link to this repository.

## Third-party material — not covered by the grants above

### Vendored upstream code

`experiments/controlled.py` and `experiments/UPSTREAM_LICENSE` are a vendored
snapshot of
[SALT-NLP/agent-collusion](https://github.com/SALT-NLP/agent-collusion) at
upstream blob `b7863603560a736403cf1337aa5909de6e377458`, under the MIT License:

> Copyright (c) 2026 Xinrui Shi, Yanzhe Zhang, and Diyi Yang

The full upstream notice is preserved verbatim in
[`experiments/UPSTREAM_LICENSE`](experiments/UPSTREAM_LICENSE). Because the
vendored file carries one local change (the `_unwrap_json_code_fence()` fenced-JSON
parsing fix and its single call site), **both** copyrights are listed for it in
[`REUSE.toml`](REUSE.toml) — it is a derivative work. See
[`experiments/README.md`](experiments/README.md) for the exact diff and its
rationale.

### The SALT-NLP dataset

The `SALT-NLP/agent-collusion` dataset is **not redistributed** by this
repository and **no rights to it are granted here**. Obtain it separately from
its authors and use it under its own upstream license and terms. Only the
`episodes` Parquet config is needed, downloaded into the git-ignored local
`data/episodes/` folder; see the reproduction instructions in
[`README.md`](README.md).

Checked-in artifacts under `results/` are aggregate statistics and metadata
derived by this project's own analysis. They contain no copied conversation
text.

## Not granted

- **No trademark license.** Nothing here grants rights to any name, logo, or
  mark, including "Apart Research" or any model or dataset name mentioned.
- **No warranty.** Both licenses disclaim all warranties. See their texts.

## Dual-use restriction on interpretation

Scores, flags, and classifier outputs in this repository **must not be used as
evidence of culpability for any agent or deployer.** False accusation of benign
coordination is a central risk this project documents: the headline result is
that a 67-percentage-point "synchronization" gap can be manufactured
arithmetically from a constant, with no coordination present. See the report's
*Limitations and Dual-Use / Ethical Considerations* appendix.

## Verifying compliance

```bash
pipx install "reuse[charset-normalizer]"
reuse lint
```

Expected: compliant with REUSE Specification v3.3, every tracked file carrying
both copyright and license information, and no bad, missing, or unused licenses.
