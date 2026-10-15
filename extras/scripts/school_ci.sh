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

# match the path the site is served from on Read the Docs, unless overridden (e.g. for local previews, which serve from the root)
BASE_URL="${BASE_URL-/en/$SCHOOL}" make site

# Generate redirects from old Jupyter Book 1 URLs to Jupyter Book 2 URLs.
uv run --with click --with pyyaml \
    https://raw.githubusercontent.com/jupyter-book/jb1-redirect-generator/d70ce6d7df9f2dfc83bb1d409336c0cc3e20697f/generate_redirects.py \
    --base-url "https://python-public-policy.afeld.me/en/$SCHOOL/" \
    --output-dir _build/html \
    --myst-config myst.yml

git diff
