#!/bin/bash
set -e

echo "entrypoint running"
echo "$GITHUB_REPOSITORY"

cd /usr/local
git clone https://github.com/mattbriggs/azs-modular-poc.git
cd azs-modular-poc
git checkout master

python /usr/local/bin/val_ki_dockeraction.py
