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

# create a fresh branch locally
git switch -c "$SCHOOL"
git add .
git commit -am "CI: render for school"
git push -f origin "$SCHOOL"

# show diff from the target

# https://gist.github.com/labynocle/93b151672585b8511ecd
# https://stackoverflow.com/questions/5326008/highlight-changed-lines-and-changed-bytes-in-each-changed-line/15149253#comment76619242_15149253
wget https://raw.githubusercontent.com/git/git/fd99e2bda0ca6a361ef03c04d6d7fdc7a9c40b78/contrib/diff-highlight/diff-highlight
chmod +x diff-highlight

if [ "$SCHOOL" = "columbia" ]; then
    # https://github.com/afeld/python-public-policy/pull/71/files
    git fetch origin columbia
    git diff --color origin/columbia syllabus.md README.md | ./diff-highlight
else
    git fetch origin main
    git diff --color origin/main ./*.md ./*.ipynb | ./diff-highlight
fi
