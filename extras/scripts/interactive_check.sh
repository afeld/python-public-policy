#!/bin/bash
# Used to skip notebooks that are interactive when looping through them. Usage:
#
#   ./extras/scripts/interactive_check.sh [IPYBNB_FILE] || exit 0

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
