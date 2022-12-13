#!/bin/bash

set -e
set -x


htmlproofer \
  --ignore-missing-alt --allow-missing-href --no-check-external-hash --only-4xx \
  --ignore-files _build/html/_static/webpack-macros.html,_build/html/_static/sbt-webpack-macros.html \
  _build/html/
