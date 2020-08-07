#!/bin/bash

set -ex

if
    python validate.py "$1"
else
    echo "An error"
    exit 0
fi

echo Done :B