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

# render markdown files
for f in ./*.md; do
    python -m extras.scripts.school_md --inplace "$f" "$SCHOOL"
done

# render notebooks
jupyter nbconvert \
    --to notebook --inplace \
    --TagRemovePreprocessor.enabled=True \
    --TagRemovePreprocessor.remove_cell_tags $REMOVE_TAG \
    --Exporter.preprocessors=extras.lib.school.SchoolTemplate \
    --SchoolTemplate.school_slug="$SCHOOL" \
    ./*.ipynb
