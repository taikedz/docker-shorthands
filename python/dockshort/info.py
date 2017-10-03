from dockshort import common

fstrings = {}
fstrings['ip'] = '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'

def list(arguments):
    target = "containers"

    if len(arguments) > 0:
        target = arguments[0]

    if target == "images":
        common.rundocker("images", [])
    elif target == "containers":
        common.rundocker("ps", ["-a"])
    elif target == "volumes":
        common.rundocker("volume", ["ls"])
    elif target == "running":
        common.rundocker("ps", [])

def info(arguments):
    containername = arguments[0]
    arguments = arguments[1:]

    if len(arguments) < 1:
        # Print everything
        common.rundocker("inspect", [containername])
    else:
        for label in arguments:
            try:
                formatstring = fstrings[label]
                common.rundocker("inspect", [ "--format='%s'" % formatstring , containername ])
            except KeyError as e:
                print "Unknown info label '%s'" % label
        # --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
