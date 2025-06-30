#!/bin/bash

set -e
set -x


SCHOOL=$1

# remove irrelevant files

git rm -r \
    .vscode/ \
    nbdime_config.json \
    extras/pandas_crash_course.ipynb \
    extras/terraform/ \
    extras/**/test_*.py

# match the conditionals in _toc.yml
if [ "$SCHOOL" = "columbia" ]; then
    git rm -r meta/adrs*
else
    git rm curve.ipynb
fi

# render the files
./extras/scripts/school.sh "$SCHOOL"

make site

git diff
