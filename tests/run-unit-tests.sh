#!/bin/bash

cd "$(dirname "$0")/.."

export PYTHONPATH="./:$PYTHONPATH"
testfiles=("$@")

if [ -z "$*" ]; then
	testfiles=(tests/test-*.py)
fi

for testfile in "${testfiles[@]}"; do
	if [ -f "$testfile" ]; then
		python "$testfile"
	else
		echo "No such file [$testfile]"
	fi
done
