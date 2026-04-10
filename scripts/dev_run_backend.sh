#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../backend"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8765
