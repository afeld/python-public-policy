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

# match the conditionals in myst.yml
if [ "$SCHOOL" = "columbia" ]; then
    git rm -r meta/adrs*
else
    git rm curve.ipynb
fi

# render the files
./extras/scripts/school.sh "$SCHOOL"

make site

# Generate redirects from old Jupyter Book 1 URLs to Jupyter Book 2 URLs.
uv run --with click --with pyyaml \
    https://raw.githubusercontent.com/jupyter-book/jb1-redirect-generator/main/generate_redirects.py \
    --base-url "https://python-public-policy.afeld.me/en/$SCHOOL/" \
    --output-dir _build/html \
    --myst-config myst.yml

git diff
