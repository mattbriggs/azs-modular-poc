#!/bin/bash
set -e

echo "entrypoint running"
echo "$GITHUB_REPOSITORY"
python /usr/local/bin/val_ki_dockeraction.py
ls