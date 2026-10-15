#!/bin/bash

# Builds the site on Read the Docs. Kept in a script rather than .readthedocs.yaml, since Read the Docs mangles the quoting of more complex commands there.
#
# https://docs.readthedocs.com/platform/stable/build-customization.html#override-the-build-process

set -e
set -x

# serve assets/links from the version's path, e.g. /en/columbia
BASE_URL=$(echo "$READTHEDOCS_CANONICAL_URL" | sed -E 's|^https?://[^/]+||; s|/$||')
export BASE_URL
make site site_url="$READTHEDOCS_CANONICAL_URL"

mkdir -p "$READTHEDOCS_OUTPUT/html/"
cp -r _build/html/. "$READTHEDOCS_OUTPUT/html"
# Read the Docs fails the build if it finds files in this old output path
rm -rf _build/html
