from dockshort import common

def list(arguments):
    target = "containers"

    if len(arguments) > 0:
        target = arguments[0]

    if target == "images":
        common.rundocker("images", [])
    elif target == "containers":
        common.rundocker("ps", ["-a"])
    elif target == "running":
        common.rundocker("ps", [])

def info(arguments):
    containername = arguments[0]
    arguments = arguments[1:]

    if len(arguments) < 1:
        common.rundocker("inspect", [])
    else:
        # --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
