#!/bin/bash

[[ "$UID" = 0 ]] || {
	echo "You must be root to run this script"
	exit 1
}

cd "$(dirname "$0")"

DOCKS_LIBDIR="/usr/share/docker-shorthands"

mkdir -p "$DOCKS_LIBDIR"
cp -r python/docks python/dockshort "$DOCKS_LIBDIR/"
ln -s "$DOCKS_LIBDIR/docks" /usr/bin/docks
