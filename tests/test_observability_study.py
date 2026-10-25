import unittest

import numpy as np

from analysis.observability_study import cmi, generate, metrics, mi


class ObservabilityTests(unittest.TestCase):
    def test_information_controls(self):
        rng = np.random.default_rng(8)
        a = rng.integers(0, 2, 10000)
        b = rng.integers(0, 2, 10000)
        self.assertLess(mi(a, b), 0.01)
        self.assertGreater(mi(a, a), 0.99)
        self.assertAlmostEqual(cmi(a, a, a), 0)

    def test_common_cause_and_channel(self):
        common = generate(11, 0, 0, "common", 10000, 0.1)
        channel = generate(11, 0, 0, "channel", 10000, 0.1)
        self.assertLess(common["cmi"], 0.01)
        self.assertGreater(channel["cmi"], 0.15)
        self.assertEqual(common["intervention_mismatch_delta"], 0)

    def test_seeded_and_stress_cases(self):
        row = generate(11, 0, 0, "channel", 256, 0.1)
        self.assertEqual(row, generate(11, 0, 0, "channel", 256, 0.1))
        self.assertEqual(
            generate(11, 0, 0, "deterministic_channel", 256, 0.1)["cmi"], 0
        )
        self.assertEqual(generate(11, 0, 0, "talk", 256, 0.1)["label"], 0)

    def test_metric_denominators(self):
        result = metrics([0, 0, 1, 1], [0.1, 0.8, 0.6, 0.9], [0, 1, 0, 1])
        self.assertEqual(result["fp"], 1)
        self.assertEqual(result["recall"], 0.5)
        self.assertEqual(result["fpr"], 0.5)


class IntegrationTests(unittest.TestCase):
    def test_save_and_reload(self):
        import json
        import tempfile
        from pathlib import Path

        from analysis.observability_study import run

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = json.loads(Path("configs/observability_study.json").read_text())
            config.update(seeds=[11], blocks_per_split=3, bootstrap_replicates=10)
            path = root / "config.json"
            path.write_text(json.dumps(config))
            result = run(path, root / "result")
            self.assertEqual(result["models"]["mi"]["metrics"]["n"], 24)
            self.assertEqual(
                json.loads((root / "result/summary.json").read_text())["primary"],
                result["primary"],
            )
            with self.assertRaises(ValueError):
                run(path, root / "result")
