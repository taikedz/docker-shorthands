from dockshort import common

def search(arguments):
    common.rundocker("search", arguments)

def pull(arguments):
    common.rundocker("pull", arguments)

def publish(arguments):
    print("Not implemented")
