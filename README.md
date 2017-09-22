# Docker Shorthands

A wrapper for Docker to allow use of shorthand commands to start and stop containers, get relevant info, attach and detach without interruptions, etc.

(totally, unfinished)

## Usage

	docks run IMAGE [as CONTAINER] [DOCKEROPTIONS] -- [IMAGEARGS ...]
	docks commit CONTAINER as IMAGE

	docks publish IMAGE as IMAGENAME [in REGISTRY]
	docks pull IMAGE [in REGISTRY]
	docks search IMAGE [in REGISTRY]

	docks start CONTAINER
	docks stop CONTAINER
	docks attach CONTAINER [SHELL]

	docks info CONTAINER [LABELS ...]

	docks list [images | containers | running]

--- obsolete set ---

	docks {i|image} run IMAGE [as CONTAINER] [networks NETNAMES] [exposing PORTMAPS] [DOCKEROPTIONS ...] [-- IMAGE OPTIONS ...]
	docks {i|image} create IMAGE from CONTAINER [{mount MOUNTDEF} ...]
	docks {i|image} list

	# attach to a container such that it keeps running after disconnecting
	docks {c|container} attach CONTAINER

	docks {c|container} start CONTAINER [in foreground]
	docks {c|container} stop CONTAINER
	docks {c|container} list [running|stopped|all]

	docks {r|registry} [in REGISTRY] search SEARCHTERMS ...
	docks {r|registry} [in REGISTRY] push IMAGE [as IMAGENAME]
	docks {r|registry} [in REGISRTY] pull IMAGE

	# Map short names to long queries
	docks {x|extract} {ip,uptime} of CONTAINER

	docks {v|volume} create VOLUMENAME

	docks {d|dockerfile} build [DOCKEROPTIONS ...]
