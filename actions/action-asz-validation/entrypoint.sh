#!/bin/bash
set -e

echo "entrypoint running"
echo "$GITHUB_REPOSITORY"
echo "$GITHUB_WORKSPACE"

cd /usr/local
git clone https://github.com/mattbriggs/azs-modular-poc.git
cd azs-modular-poc
git checkout master

python /usr/local/azs-modular-poc/python/val_ki_dockeraction.py

