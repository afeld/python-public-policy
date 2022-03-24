#!/bin/bash

set -e
set -x


cd extras

# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#updating-an-environment
mamba env update --file environment.yml --prune

# regenerate lock files
conda run -n base conda-lock lock --conda mamba --kind explicit

cd -
./extras/scripts/update_all.sh
