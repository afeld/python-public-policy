#!/bin/bash

set -e

NOTEBOOK="$1"

echo "Executing notebook..."
jupyter nbconvert \
  --to notebook --inplace --execute --no-prompt \
  --ExecutePreprocessor.kernel_name=python3 \
  --ExecutePreprocessor.timeout=120 \
  "$NOTEBOOK"

make format file="$NOTEBOOK"
