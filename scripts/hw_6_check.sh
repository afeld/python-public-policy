#!/bin/bash

# requires cloc and jq

set -e
set -o pipefail
# set -x

FILE=$1

LINES_OF_CODE=$(
  jupyter nbconvert --to script --log-level WARN --stdout "$FILE" | \
  cloc --stdin-name=script.py --json - | \
  jq .SUM.code
)
echo "Lines of code: $LINES_OF_CODE"
