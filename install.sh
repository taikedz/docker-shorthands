#!/bin/bash

[[ "$UID" = 0 ]] || {
	echo "You must be root to run this script"
	exit 1
}

cd "$(dirname "$0")"

DOCKS_LIBDIR="/usr/share/docker-shorthands"

mkdir -p "$DOCKS_LIBDIR"
cp -r dockshort "$DOCKS_LIBDIR/"

if [ ! -e "/usr/bin/docks" ]; then
	ln -s "$DOCKS_LIBDIR/dockshort/main.py" /usr/bin/docks
else
	ls -l "/usr/bin/docks"
fi
