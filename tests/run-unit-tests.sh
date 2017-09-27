#!/bin/bash

cd "$(dirname "$0")/.."

export PYTHONPATH="./python/:$PYTHONPATH"
testfiles=("$@")

if [ -z "$*" ]; then
	testfiles=(tests/test-*.py)
fi

for testfile in "${testfiles[@]}"; do
	python "$testfile"
done
