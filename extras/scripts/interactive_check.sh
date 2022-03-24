#!/bin/bash

set -e
set -x


case "$1" in

  "hw_0.ipynb")
    # uses input()s
    exit 1
    ;;

  "hw_3.ipynb")
    # has incomplete code
    exit 1
    ;;

esac
