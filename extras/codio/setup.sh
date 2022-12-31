#!/bin/bash

set -e
set -x


# add dependencies for PDF export
# https://nbconvert.readthedocs.io/en/latest/install.html#installing-pandoc
# https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex
sudo apt-get update -y
sudo apt-get install -y \
    pandoc \
    texlive-xetex texlive-fonts-recommended texlive-plain-generic

sudo pip install --upgrade pip
pip install --upgrade --user -r extras/requirements.txt
