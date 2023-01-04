#!/bin/bash

set -e
set -x

# confirm there's exactly one argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 SCHOOL" >&2
  exit 1
fi

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

# render notebooks
jupyter nbconvert \
    --to notebook --inplace \
    --TagRemovePreprocessor.enabled=True \
    --TagRemovePreprocessor.remove_cell_tags $REMOVE_TAG \
    --Exporter.preprocessors=extras.lib.school.SchoolTemplate \
    --SchoolTemplate.school_id="$SCHOOL" \
    ./*.ipynb

# render additional files
OTHER_FILES=$(git ls-files -- ':!:*.ipynb' ':!:*.py' ':!:.github/workflows/*' ':!:extras/img/*')
for f in $OTHER_FILES; do
    python -m extras.scripts.school_template --inplace "$f" "$SCHOOL"
done
