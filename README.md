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
