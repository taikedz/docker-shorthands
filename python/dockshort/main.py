#!/usr/bin/python

import sys
from dockshort import image, info, container, registry, common

def main():
    if not common.args_check(sys.argv, 2):
        print "Not enough arguments"
        exit(1)

    command = sys.argv[1]
    arguments = sys.argv[2:]

    if command == "run":
        image.run(arguments)
    elif command == "commit":
        image.commit(arguments)

    elif command == "start":
        container.start(arguments)
    elif command == "stop":
        container.stop(arguments)
    elif command == "attach":
        container.attach(arguments)

    elif command == "publish":
        registry.publish(arguments)
    elif command == "pull":
        registry.pull(arguments)
    elif command == "search":
        registry.search(arguments)

    elif command == "info":
        info.info(arguments)
    elif command == "list":
        info.list(arguments)

    #elif command == "":
    #    (arguments)

    else:
        print("Unknown command '%s'" % command)
        sys.exit(1)


if __name__ == "__main__":
    main()
