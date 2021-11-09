#!/bin/bash

set -e
set -x

# https://stackoverflow.com/a/22561483/358804
zip -r "$1.zip" "$1" -x "*.DS_Store" -x "__MACOSX"
