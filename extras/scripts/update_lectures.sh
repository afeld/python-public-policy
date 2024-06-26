#!/bin/bash

set -e
set -x


git ls-files lecture_*.ipynb | while IFS=$'\n' read -r notebook; do
  ./extras/scripts/interactive_check.sh "$notebook" || continue
  ./extras/scripts/update.sh "$notebook"
done
