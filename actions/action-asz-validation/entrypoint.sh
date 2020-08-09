#!/bin/bash

echo "entrypoint running"

path-report = "This is the report"
echo "::set-output name=path-report::$path-report"

exit 0