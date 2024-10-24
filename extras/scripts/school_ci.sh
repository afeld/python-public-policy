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

if [ "$SCHOOL" = "nyu" ]; then
    git rm curve.ipynb
fi

# render the files
./extras/scripts/school.sh "$SCHOOL"

./extras/scripts/build.sh

git diff
