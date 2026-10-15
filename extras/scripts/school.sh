#!/bin/bash

# Turns the source files into a school's version: removes files that don't belong in it, then renders the templates (Jinja variables and conditionals, plus school-specific cell tags). Using this custom logic since Jupyter Book 2 (MyST) doesn't have substitutions that work in code blocks, links, or conditionals. Destructive, so run in a throwaway checkout (as CI and preview.sh do).
#
# Usage:
#
#   ./extras/scripts/school.sh <school> [<files>]
#
# With files, only those are rendered, for re-rendering after changes.

set -e


SCHOOL=$1
# the other school's files need removing even though myst.yml leaves them out of the site, since they'd fail the check for mentions of the other school. Keep these matching the conditionals in myst.yml.
case $SCHOOL in
    nyu)
        REMOVE_TAG=columbia-only
        REMOVE_FILES=(curve.ipynb lecture_2_exercise_2_solution.ipynb)
        ;;
    columbia)
        REMOVE_TAG=nyu-only
        REMOVE_FILES=(meta/adrs/)
        ;;
    *)
        echo "Unknown school: $SCHOOL" >&2
        exit 1
        ;;
esac

# remove irrelevant files, ignoring ones that are already gone or changed (e.g. on re-runs)
git rm -r -q -f --ignore-unmatch -- \
    .claude/ \
    .vscode/ \
    AGENTS.md \
    nbdime_config.json \
    extras/pandas_crash_course.ipynb \
    extras/terraform/ \
    ':(glob)extras/*/test_*.py' \
    "${REMOVE_FILES[@]}"

shift 1
# render the given files (or all of them), with a bunch of exceptions
FILES=$(git ls-files -- "$@" \
    ':!:*.js' ':!:*.py' \
    ':!:**/environment*.yml' \
    ':!:.github/workflows/*' \
    ':!:.github/ISSUE_TEMPLATE/new-term-*.md' \
    ':!:.readthedocs.yaml' \
    ':!:Makefile' \
    ':!:extras/img/*' \
    ':!:extras/scripts/*')

# allow this script to be run from other directories
PYTHONPATH=$(dirname "$0")/../..
export PYTHONPATH

for f in $FILES; do
    echo "Rendering $f, even if not used..."
    # https://stackoverflow.com/a/965072/358804
    extension="${f##*.}"
    if [ "$extension" = "ipynb" ]; then
        jupyter nbconvert \
            --to notebook --inplace \
            --TagRemovePreprocessor.enabled=True \
            --TagRemovePreprocessor.remove_cell_tags $REMOVE_TAG \
            --TagRemovePreprocessor.remove_cell_tags remove \
            --Exporter.preprocessors=extras.lib.school_template.SchoolTemplate \
            --SchoolTemplate.school_id="$SCHOOL" \
            "$f"
    else
        python -m extras.scripts.school_template --inplace "$f" "$SCHOOL"
    fi
done
