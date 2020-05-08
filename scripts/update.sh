#!/bin/bash

set -e

echo "Re-running notebook..."
jupyter nbconvert \
  --to notebook --inplace --execute --no-prompt \
  --ExecutePreprocessor.kernel_name=python3 \
  --ExecutePreprocessor.timeout=120 \
  $@
