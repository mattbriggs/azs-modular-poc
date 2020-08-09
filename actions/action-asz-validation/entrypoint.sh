#!/bin/bash
set -e

echo "entrypoint running"
echo "$GITHUB_REPOSITORY"
python val_ki_dockeraction.py