#!/bin/bash

set -e
set -x

TEMPLATE_DIR=scripts/templates
TEMPLATE=ppp
DEST=public

mkdir -p "$DEST"

rsync -avh --delete img/ public/img/

for notebook in *.ipynb
do
  jupyter nbconvert --to html \
    --TemplateExporter.extra_template_basedirs="$TEMPLATE_DIR" \
    --template "$TEMPLATE" \
    --output-dir="$DEST" \
    "$notebook"
done
