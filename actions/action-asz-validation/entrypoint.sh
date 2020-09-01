#!/bin/bash
set -e

echo "entrypoint running"
echo "$GITHUB_REPOSITORY"
echo "$GITHUB_WORKSPACE"

cd "$GITHUB_WORKSPACE"
git clone https://github.com/mattbriggs/azs-modular-poc.git
cd azs-modular-poc
git checkout "$GITHUB_WORKSPACE"

python /usr/local/bin/val_ki_dockeraction.py
