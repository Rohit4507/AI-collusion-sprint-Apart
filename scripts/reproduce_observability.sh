#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHON="${PYTHON:-python}"
"$PYTHON" -m unittest discover -s tests -v
"$PYTHON" -m analysis.observability_study --config configs/observability_study.json --output "${1:-outputs/observability-reproduction}"
