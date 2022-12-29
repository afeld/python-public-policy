#!/bin/bash

set -e

# confirm there's exactly one argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 SCHOOL" >&2
  exit 1
fi

SCHOOL=$1

jupyter nbconvert \
    --to notebook --inplace \
    --Exporter.preprocessors=extras.lib.school.SchoolTemplate \
    --SchoolTemplate.school_slug="$SCHOOL" \
    ./*.ipynb
