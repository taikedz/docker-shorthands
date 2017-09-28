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

    # Finally split off the end options
    dockeroptions, imageargs = common.split_on_token("--", arguments)

    common.rundocker("run", containername + dockeroptions + imagename + imageargs)

def commit(arguments):
    # docker commit -m "Commit description" -a "Author name" CONTAINER repo/imagename[:label]
    print("Not implemented")
