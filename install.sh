#!/bin/bash

[[ "$UID" = 0 ]] || {
	echo "You must be root to run this script"
	exit 1
}

cd "$(dirname "$0")"

cp -r python/docker-shorthands /usr/share/
ln -s /usr/share/docker-shorthands/dck.py /usr/bin/dck
