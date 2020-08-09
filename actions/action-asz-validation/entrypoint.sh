#!/bin/bash
set -e

echo "entrypoint running"
echo "$GITHUB_REPOSITORY"
python /usr/local/bin/val_ki_dockeraction.py
echo "/usr/local/bin/"
cd /usr/local/bin/
ls
echo "/usr/local/"
cd /usr/local
ls