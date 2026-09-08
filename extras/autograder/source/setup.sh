#!/usr/bin/env bash

set -ex

apt-get install -y python3 python3-pip

pip3 install -r /autograder/source/requirements.txt
