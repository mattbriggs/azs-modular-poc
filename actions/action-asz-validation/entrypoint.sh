#!/bin/bash
set -e

state="True"

cd /usr/local
git clone https://github.com/mattbriggs/azs-modular-poc.git
cd azs-modular-poc
git checkout master

python /usr/local/azs-modular-poc/python/val_ki_dockeraction.py


if [ $state == "True" ] ; then
  echo "All is well."
  exit 1
fi

if [ $state == "False" ]; then
  echo "Game over!"
  exit 1
fi