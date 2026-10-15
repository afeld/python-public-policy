#!/bin/bash

# Turns the source files into a school's version: removes files that don't belong in it, then renders the templates. Destructive, so run in a throwaway checkout (as CI and preview.sh do).
#
# Usage:
#
#   ./extras/scripts/school_prep.sh <school> [<files>]
#
# With files, only those are rendered, for re-rendering after changes.

set -e
set -x


SCHOOL=$1
shift

# remove irrelevant files, ignoring ones that are already gone or changed (e.g. on re-runs)
git rm -r -q -f --ignore-unmatch \
    .claude/ \
    .vscode/ \
    AGENTS.md \
    nbdime_config.json \
    extras/pandas_crash_course.ipynb \
    extras/terraform/ \
    ':(glob)extras/*/test_*.py'

# match the conditionals in myst.yml
if [ "$SCHOOL" = "columbia" ]; then
    git rm -r -q -f --ignore-unmatch 'meta/adrs*'
else
    git rm -q -f --ignore-unmatch curve.ipynb
fi

# render the files
./extras/scripts/school.sh "$SCHOOL" "$@"
