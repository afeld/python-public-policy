#!/bin/bash

set -e
set -x


SCHOOL=$1

# remove irrelevant files
git rm -r \
    .claude/ \
    .vscode/ \
    AGENTS.md \
    nbdime_config.json \
    extras/pandas_crash_course.ipynb \
    extras/terraform/ \
    extras/**/test_*.py

# match the conditionals in myst.yml
if [ "$SCHOOL" = "columbia" ]; then
    git rm -r meta/adrs*
else
    git rm curve.ipynb
fi

# render the files
./extras/scripts/school.sh "$SCHOOL"

# only used for link checking, so served from the root; Read the Docs builds the real site
make site site_url="https://python-public-policy.afeld.me/en/$SCHOOL/"

git diff
