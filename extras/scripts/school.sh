#!/bin/bash

# Renders the notebook templates. Using this custom logic rather than Jupyter Book substitutions since the latter can't be used in code blocks or for links.
#
# https://jupyterbook.org/en/stable/content/content-blocks.html#substitutions-and-variables-in-markdown
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2
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

if [ $# -eq 1 ]; then
    # render files, with a bunch of exceptions
    FILES=$(git ls-files -- \
        ':!:*.js' ':!:*.py' ':!:*.tf' \
        ':!:**/environment*.yml' \
        ':!:.github/workflows/*' \
        ':!:.github/ISSUE_TEMPLATE/new-term-*.md' \
        ':!:.readthedocs.yaml' \
        ':!:Makefile' \
        ':!:extras/img/*' \
        ':!:extras/pandas_crash_course.ipynb' \
        ':!:extras/scripts/*')
else
    shift 1
    FILES=$*
fi

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
