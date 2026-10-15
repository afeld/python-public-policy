#!/bin/bash

set -e
set -x


SCHOOL=$1

./extras/scripts/school.sh "$SCHOOL"

# only used for link checking, so served from the root; Read the Docs builds the real site
make site site_url="https://python-public-policy.afeld.me/en/$SCHOOL/"

git diff
