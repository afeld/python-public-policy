#!/bin/bash

set -e
set -x

TEMPLATE_DIR=scripts/templates
TEMPLATE=ppp
DEST=public

rm -r "$DEST"
mkdir "$DEST"

cp -r "$TEMPLATE_DIR/$TEMPLATE/static" public
cp -r img public

for notebook in *.ipynb
do
  jupyter nbconvert --to html \
    --TemplateExporter.extra_template_basedirs="$TEMPLATE_DIR" \
    --template "$TEMPLATE" \
    --output-dir="$DEST" \
    "$notebook"
done
