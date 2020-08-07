#!/bin/sh -l

echo "entrypoint running"

if
    echo "python validate.py $1"
    echo "python ran"
else
    echo "An error"
    exit 0
fi