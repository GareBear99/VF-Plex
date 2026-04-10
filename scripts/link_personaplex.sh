#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-third_party/personaplex}"
if [ -d "$TARGET_DIR/.git" ] || [ -f "$TARGET_DIR/README.md" ]; then
  echo "PersonaPlex path looks present at: $TARGET_DIR"
else
  echo "PersonaPlex not found at: $TARGET_DIR"
  echo "Clone upstream or your fork there first."
  exit 1
fi
