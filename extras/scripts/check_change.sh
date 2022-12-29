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

mkdir -p tmp/extras
diffable "$SOURCE" "$PRE"

./extras/scripts/interactive_check.sh "$SOURCE" || exit 0

cp "$PRE" "$POST"
./extras/scripts/update.sh "$POST"

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

  "lecture_5.ipynb")
    # calls APIs with data that could change
    exit
    ;;

esac

echo "Comparing output..."
DIFF=$(nbdiff "$PRE" "$FINAL")
echo "$DIFF"
[ -z "$DIFF" ] || exit 1
