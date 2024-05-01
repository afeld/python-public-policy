#!/bin/bash

set -e
set -x

# for some reason, RISE only works temporarily, so reinstall it to be safe
# https://github.com/jupyterlab-contrib/rise/issues/28
mamba install jupyterlab_rise

jupyter notebook --no-browser
