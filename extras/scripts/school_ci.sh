#!/bin/bash

set -e
set -x


SCHOOL=$1

# render the files
./extras/scripts/school.sh "$SCHOOL"

# https://lannonbr.com/blog/2019-12-09-git-commit-in-actions/
# https://github.com/orgs/community/discussions/26560#discussioncomment-3252339
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

TARGET_BRANCH=$SCHOOL-auto
# create a fresh branch
git switch -c "$TARGET_BRANCH"
git add .
git commit -am "CI: render for school"
git push -f origin "$TARGET_BRANCH"

# show diff from the target
# https://github.com/afeld/python-public-policy/pull/71/files

if [ "$SCHOOL" = "columbia" ]; then
    COMPARE_BRANCH=columbia
else
    COMPARE_BRANCH=main
fi

git fetch origin $COMPARE_BRANCH
git diff --color-words origin/$COMPARE_BRANCH syllabus.md README.md
