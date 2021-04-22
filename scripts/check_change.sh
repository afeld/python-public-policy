#!/bin/bash

set -e
set -x


echo "Setting up..."
SOURCE=$1
PRE="tmp/$SOURCE"
POST=${PRE//\./.nbconvert.}
FINAL=${PRE//\./.final.}

function diffable() {
  jupyter nbconvert --to notebook --Exporter.preprocessors=scripts.diffable.Diffable --stdout "$1" > "$2"
}

mkdir -p tmp
diffable "$SOURCE" "$PRE"

cp "$PRE" "$POST"
./scripts/update.sh "$POST"

diffable "$POST" "$FINAL"

echo "Comparing output..."
DIFF=$(nbdiff "$PRE" "$FINAL")
echo "$DIFF"
[ -z "$DIFF" ] || exit 1
