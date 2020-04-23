#!/bin/bash

set -e

jq '[.cells | .[].metadata.slideshow.slide_type | select(. == "slide" or . == "subslide")] | length' < $1
