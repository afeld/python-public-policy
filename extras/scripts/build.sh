#!/bin/bash

set -e
set -x

# https://jupyterbook.org/en/stable/content/references.html#check-for-missing-references
jupyter-book build --all -n .
