#!/usr/bin/env bash

set -ex

apt-get install -y python3 curl
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

uv pip install --system -r /autograder/source/requirements.txt
