#!/bin/bash

set -e
set -x


echo "Setting up..."
SOURCE=$1
PRE="tmp/$SOURCE"
POST=${PRE//\./.nbconvert.}
FINAL=${PRE//\./.final.}

mkdir -p tmp
jupyter nbconvert --to notebook --Exporter.preprocessors=scripts.diffable.Diffable --stdout "$SOURCE" > "$PRE"

cp "$PRE" "$POST"
./scripts/update.sh "$POST"

jupyter nbconvert --to notebook --Exporter.preprocessors=scripts.diffable.Diffable --stdout "$POST" > "$FINAL"

echo "Comparing output..."
DIFF=$(nbdiff "$PRE" "$FINAL")
echo "$DIFF"
[ -z "$DIFF" ] || exit 1
