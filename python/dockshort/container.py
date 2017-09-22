from dockshort import common

def start(arguments):
    """ Start the container
    """
    common.rundocker("start", [arguments[0]])

def stop(arguments):
    """ Stop the container
    """
    common.rundocker("stop", [arguments[0]])

def attach(arguments):
    """ Attach to the container in such a way as it stays running when we leave

    """
    containername = arguments[0]
    shell = "sh"
    if len(arguments) > 1:
        shell = arguments[1]

    common.rundocker("exec", ["-it", arguments[0], shell])
