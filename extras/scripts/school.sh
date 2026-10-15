#!/bin/bash

# Renders the notebook templates (Jinja variables and conditionals, plus school-specific cell tags). Using this custom logic since Jupyter Book 2 (MyST) doesn't have substitutions that work in code blocks, links, or conditionals.
#
# Usage:
#
#   ./extras/scripts/school.sh <school> [<files>]

set -e


SCHOOL=$1
case $SCHOOL in
    nyu)
        REMOVE_TAG=columbia-only
        ;;
    columbia)
        REMOVE_TAG=nyu-only
        ;;
    *)
        echo "Unknown school: $SCHOOL" >&2
        exit 1
        ;;
esac

shift 1
# render the given files (or all of them), with a bunch of exceptions
FILES=$(git ls-files -- "$@" \
    ':!:*.js' ':!:*.py' ':!:*.tf' \
    ':!:**/environment*.yml' \
    ':!:.github/workflows/*' \
    ':!:.github/ISSUE_TEMPLATE/new-term-*.md' \
    ':!:.readthedocs.yaml' \
    ':!:Makefile' \
    ':!:extras/img/*' \
    ':!:extras/pandas_crash_course.ipynb' \
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
