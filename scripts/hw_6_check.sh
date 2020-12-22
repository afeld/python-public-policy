#!/bin/bash

# requires cloc and jq

set -e
set -o pipefail
# set -x

NOTEBOOK=$1

SCRIPT=$(jupyter nbconvert --to script --log-level WARN --stdout "$NOTEBOOK")

LINES_OF_CODE=$(
  echo "$SCRIPT" | \
  cloc --stdin-name=script.py --json - | \
  jq .SUM.code
)
echo "Lines of code: $LINES_OF_CODE"

LINK_IN_MARKDOWN=$(jq '[.cells | .[] | select(.cell_type == "markdown") | .source] | flatten | any(. | test("https?://"))' "$NOTEBOOK") #| grep -E 'https?://'
LINK_IN_COMMENT=$(jq '[.cells | .[] | select(.cell_type == "code") | .source] | flatten | any(. | test("^\s*#.*https?://"))' "$NOTEBOOK")

# if echo "$SCRIPT" | grep -E '^\s*#.*https?://'; then
if echo "$LINK_IN_MARKDOWN" == "true"; then
  echo "Has link in Markdown"
elif echo "$LINK_IN_COMMENT" == "true"; then
  echo "Has link in comment"
else
  echo "Doesn't have link"
fi
