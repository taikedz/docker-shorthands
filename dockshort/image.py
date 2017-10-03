from dockshort import common

def set_option_tag(optiontag, value, sep=" "):
    if not value:
        return []
    else:
        return [optiontag +sep+ value]

def run(arguments):
    if not common.args_check(arguments, 1):
        print "Run requires at least one argument, the image name."
        exit(1)

    imagename = [arguments[0]]
    arguments = arguments[1:]

    # Shorthand named options
    containername, arguments = common.extract_after_token("as", arguments)
    containername = set_option_tag("--name", containername, sep="=")

    port_exposures = []
    while True:
        portmap,aruments = common.extract_after_token("-e", arguments)
        if not portmap:
            break

        # There are both "expose" and "publish" which are slightly different - what to choose?
        port_exposures = set_option_tag("--expose", port_exposures, sep="=")

    # Finally split off the end options
    dockeroptions, imageargs = common.split_on_token("--", arguments)
    if imageargs == None:
        imageargs = []

    common.rundocker("run", ["-d"] + containername + dockeroptions + imagename + imageargs)

def commit(arguments):
    # docker commit -m "Commit description" -a "Author name" CONTAINER repo/imagename[:label]
    print("Not implemented")
