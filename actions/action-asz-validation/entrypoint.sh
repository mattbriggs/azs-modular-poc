#!/bin/bash
set -e

cd /usr/local
git clone https://github.com/mattbriggs/azs-modular-poc.git
cd azs-modular-poc
git checkout master

state=`python /usr/local/azs-modular-poc/python/val_ki_dockeraction.py | state -n 1`

echo $state

if [ $state=="True" ] ; then
  echo "All is well."
fi

if [ $state=="False" ]; then
  echo "Game over!"
  exit 1
fi