"""CPU-only scripted channel-identifiability stress test; not an intent detector."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import time
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

CONDITIONS = (
    "independent",
    "common",
    "talk",
    "channel",
    "hidden_common",
    "deterministic_channel",
    "equivalent_common",
    "equivalent_channel",
)
POSITIVE = {"channel", "deterministic_channel", "equivalent_channel"}


def mi(a, b):
    counts = np.zeros((2, 2), dtype=float)
    np.add.at(counts, (a, b), 1)
    p = counts / len(a)
    q = p.sum(axis=1)[:, None] * p.sum(axis=0)[None, :]
    mask = p > 0
    return float(np.sum(p[mask] * np.log2(p[mask] / q[mask])))


def cmi(a, b, z):
    return sum(
        float(np.mean(z == k)) * mi(a[z == k], b[z == k])
        for k in (0, 1)
        if np.any(z == k)
    )


def generate(seed, split, block, condition, steps, noise):
    # Explicit independent child streams; matching exogenous randomness across conditions is intentional.
    children = np.random.SeedSequence([seed, split, block]).spawn(5)
    rz, ra, rb, rw, rcut = [np.random.default_rng(s) for s in children]
    z = rz.integers(0, 2, steps)
    a = z ^ (ra.random(steps) < noise)
    b = z ^ (rb.random(steps) < noise)
    observed = z
    if condition == "independent":
        a = ra.integers(0, 2, steps)
        b = rb.integers(0, 2, steps)
    elif condition == "channel":
        b = a ^ (rb.random(steps) < noise)
    elif condition == "hidden_common":
        observed = rw.integers(0, 2, steps)
    elif condition == "deterministic_channel":
        a, b = z.copy(), z.copy()
    elif condition in ("equivalent_common", "equivalent_channel"):
        observed = rw.integers(0, 2, steps)
        a = z.copy() if condition == "equivalent_common" else ra.integers(0, 2, steps)
        b = a.copy()
    cut = rcut.integers(0, 2, steps) if condition in POSITIVE else b.copy()
    return {
        "seed": seed,
        "split": split,
        "block": block,
        "condition": condition,
        "label": int(condition in POSITIVE),
        "keyword": int(condition == "talk"),
        "agreement": float(np.mean(a == b)),
        "mi": mi(a, b),
        "cmi": cmi(a, b, observed),
        "a_mean": float(a.mean()),
        "b_mean": float(b.mean()),
        "harm_proxy": float(np.mean((a == 1) & (b == 1))),
        "intervention_mismatch_delta": float(np.mean(a != cut) - np.mean(a != b)),
    }


def metrics(y, score, flag, probability=False):
    y, flag = np.asarray(y), np.asarray(flag, dtype=bool)
    tp, fp = int(np.sum(flag & (y == 1))), int(np.sum(flag & (y == 0)))
    pos, neg = int(np.sum(y == 1)), int(np.sum(y == 0))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / pos
    return {
        "n": len(y),
        "positives": pos,
        "negatives": neg,
        "prevalence": pos / len(y),
        "tp": tp,
        "fp": fp,
        "fn": pos - tp,
        "tn": neg - fp,
        "precision": precision,
        "recall": recall,
        "f1": 2 * precision * recall / (precision + recall)
        if precision + recall
        else 0.0,
        "fpr": fp / neg,
        "average_precision": float(average_precision_score(y, score)),
        "roc_auc": float(roc_auc_score(y, score)),
        "brier": float(np.mean((np.asarray(score) - y) ** 2)) if probability else None,
    }


def write_csv(path, rows):
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def run(config_path, output):
    started = time.perf_counter()
    config = json.loads(Path(config_path).read_text())
    if config["steps"] < 16 or config["blocks_per_split"] < 2 or not config["seeds"]:
        raise ValueError("Insufficient steps, blocks or seeds")
    output = Path(output)
    if output.exists() and any(output.iterdir()):
        raise ValueError("Output must be fresh")
    output.mkdir(parents=True, exist_ok=True)
    rows = []
    for split in range(3):
        noise = config["families"]["held_out" if split == 2 else "development"]
        for seed in config["seeds"]:
            for block in range(config["blocks_per_split"]):
                for condition in CONDITIONS:
                    rows.append(
                        generate(seed, split, block, condition, config["steps"], noise)
                    )
    train = [r for r in rows if r["split"] == 0]
    cal = [r for r in rows if r["split"] == 1]
    test = [r for r in rows if r["split"] == 2]
    views = {
        "action_classifier": ["agreement", "mi", "a_mean", "b_mean"],
        "combined_classifier": ["agreement", "mi", "a_mean", "b_mean", "keyword"],
    }
    scores = {}
    for name, fields in views.items():
        model = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
        model.fit([[r[k] for k in fields] for r in train], [r["label"] for r in train])
        scores[name] = [
            model.predict_proba([[r[k] for k in fields] for r in subset])[:, 1]
            for subset in (cal, test)
        ]
    for name in ("agreement", "mi", "cmi", "keyword"):
        scores[name] = [np.array([r[name] for r in subset]) for subset in (cal, test)]
    prevalence = float(np.mean([r["label"] for r in train]))
    scores["prevalence"] = [np.full(len(s), prevalence) for s in (cal, test)]
    predictions = []
    summaries = {}
    eligible = np.array(
        [r["condition"] in ("independent", "common", "talk") for r in cal]
    )
    for name, (cs, ts) in scores.items():
        if not np.isfinite(ts).all():
            raise ValueError("Nonfinite scores")
        threshold = (
            0.5
            if name == "keyword"
            else float(
                np.quantile(
                    cs[eligible], 1 - config["target_calibration_fpr"], method="higher"
                )
            )
        )
        flags = ts > threshold
        summaries[name] = {
            "threshold": threshold,
            "threshold_rule": "keyword rule"
            if name == "keyword"
            else "calibrated strict greater",
            "metrics": metrics(
                [r["label"] for r in test],
                ts,
                flags,
                name.endswith("classifier") or name == "prevalence",
            ),
            "conditions": {},
        }
        for condition in CONDITIONS:
            ix = np.array([r["condition"] == condition for r in test])
            summaries[name]["conditions"][condition] = {
                "n": int(ix.sum()),
                "flag_count": int(flags[ix].sum()),
                "flag_rate": float(flags[ix].mean()),
            }
        for r, s, f in zip(test, ts, flags):
            predictions.append(
                {
                    "seed": r["seed"],
                    "block": r["block"],
                    "condition": r["condition"],
                    "label": r["label"],
                    "model": name,
                    "score": float(s),
                    "flagged": int(f),
                }
            )
    # Paired block bootstrap: all mechanisms share one resampling unit.
    differences = []
    for seed in config["seeds"]:
        for block in range(config["blocks_per_split"]):
            subset = [
                p
                for p in predictions
                if p["seed"] == seed
                and p["block"] == block
                and p["condition"] == "common"
            ]
            d = {p["model"]: p["flagged"] for p in subset}
            differences.append(d["cmi"] - d["mi"])
    rng = np.random.default_rng(20261025)
    boot = np.mean(
        rng.choice(differences, (config["bootstrap_replicates"], len(differences))),
        axis=1,
    )
    primary = {
        "contrast": "CMI minus MI FPR on common-cause negatives",
        "difference": float(np.mean(differences)),
        "ci95": np.quantile(boot, [0.025, 0.975]).tolist(),
        "channel_recall": summaries["cmi"]["conditions"]["channel"]["flag_rate"],
    }
    primary["criterion_met"] = bool(
        primary["ci95"][1] < 0 and primary["channel_recall"] >= 0.8
    )
    summary = {
        "scope": "scripted mechanism detection, not LLM intent",
        "primary": primary,
        "models": summaries,
        "runtime_seconds": time.perf_counter() - started,
        "python": platform.python_version(),
        "config_sha256": hashlib.sha256(Path(config_path).read_bytes()).hexdigest(),
        "seedwise_primary_difference": {
            str(seed): float(
                np.mean(
                    differences[
                        i * config["blocks_per_split"] : (i + 1)
                        * config["blocks_per_split"]
                    ]
                )
            )
            for i, seed in enumerate(config["seeds"])
        },
    }
    write_csv(output / "trajectories.csv", rows)
    write_csv(output / "predictions.csv", predictions)
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (output / "config.json").write_text(json.dumps(config, indent=2) + "\n")
    import importlib.metadata

    (output / "versions.json").write_text(
        json.dumps(
            {
                p: importlib.metadata.version(p)
                for p in ("numpy", "scipy", "scikit-learn")
            },
            indent=2,
        )
        + "\n"
    )
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/observability_study.json")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.config, args.output)["primary"], indent=2))
