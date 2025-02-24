#!/bin/bash

set -e
set -x


# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#updating-an-environment
mamba env update --file extras/environment.yml --prune

./extras/scripts/update_lectures.sh

echo "Please update homework notebooks separately, in python-public-policy-assignments"
