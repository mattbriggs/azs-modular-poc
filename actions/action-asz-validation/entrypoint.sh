#!/bin/bash
set -e

echo "entrypoint running"
echo "$GITHUB_REPOSITORY"
echo "$WORKDIR"
python /usr/local/bin/val_ki_dockeraction.py
echo "/usr/local/bin/"
cd /usr/local/bin/
ls
echo "/"
cd /
ls