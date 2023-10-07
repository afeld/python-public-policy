#!/bin/bash

set -e

NOTEBOOK="$1"

echo "Executing notebook..."
jupyter nbconvert \
  --to notebook --inplace --execute --no-prompt \
  --ExecutePreprocessor.kernel_name=python3 \
  --ExecutePreprocessor.timeout=120 \
  "$NOTEBOOK"

nbqa black "$NOTEBOOK"
# https://github.com/nbQA-dev/nbQA/issues/555#issuecomment-974651504
nbqa mdformat "$NOTEBOOK" --nbqa-md
