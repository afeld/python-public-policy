#!/bin/bash

# Builds the site on Read the Docs. Kept in a script rather than .readthedocs.yaml, since Read the Docs mangles the quoting of more complex commands there.
#
# https://docs.readthedocs.com/platform/stable/build-customization.html#override-the-build-process

set -e
set -x

# serve assets/links from the version's path, e.g. /en/columbia
BASE_URL=$(echo "$READTHEDOCS_CANONICAL_URL" | sed -E 's|^https?://[^/]+||; s|/$||')
export BASE_URL
make site

# Generate redirects from old Jupyter Book 1 URLs to Jupyter Book 2 URLs. The script only needs its own dependencies, so skip installing the project's.
uv run --no-project --with click --with pyyaml \
    https://raw.githubusercontent.com/jupyter-book/jb1-redirect-generator/d70ce6d7df9f2dfc83bb1d409336c0cc3e20697f/generate_redirects.py \
    --base-url "$READTHEDOCS_CANONICAL_URL" \
    --output-dir _build/html \
    --myst-config myst.yml

mkdir -p "$READTHEDOCS_OUTPUT/html/"
cp -r _build/html/. "$READTHEDOCS_OUTPUT/html"
