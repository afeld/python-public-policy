#!/bin/bash

set -e
set -x


echo "Setting up..."
SOURCE=$1
PRE="tmp/$SOURCE"
POST=${PRE//\./.nbconvert.}
FINAL=${PRE//\./.final.}

function diffable() {
  jupyter nbconvert --to notebook --Exporter.preprocessors=extras.lib.diffable.Diffable --stdout "$1" > "$2"
}

# allow this script to be run from other directories
PYTHONPATH=$(dirname "$0")/../..
export PYTHONPATH

mkdir -p tmp/extras
diffable "$SOURCE" "$PRE"

# https://mywiki.wooledge.org/BashFAQ/028#Using_BASH_SOURCE
"${BASH_SOURCE%/*}/interactive_check.sh" "$SOURCE" || exit 0

cp "$PRE" "$POST"
"${BASH_SOURCE%/*}/update.sh" "$POST"

diffable "$POST" "$FINAL"

case "$SOURCE" in

  "lecture_1.ipynb")
    # uses sample()
    exit
    ;;

  "lecture_3.ipynb")
    # https://github.com/jupyter/nbdime/issues/473#issuecomment-831682930
    exit
    ;;

  "lecture_6.ipynb")
    # calls APIs with data that could change
    exit
    ;;

  "curve.ipynb")
    # loads data locally
    exit
    ;;

esac

echo "Comparing output..."
DIFF=$(nbdiff "$PRE" "$FINAL")
echo "$DIFF"
[ -z "$DIFF" ] || exit 1
