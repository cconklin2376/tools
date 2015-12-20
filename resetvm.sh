#!/bin/bash
# places virtualbox vm in specified snapshot state
# and starts the vm. Assumes the vm is not running.

if [[ $# < 2 ]]; then
	echo "Usage: resetvm <vm-name> <snapshot-name>"
else 

	VM=$1
	SShot=$2

	vboxmanage snapshot "${VM}" restore "${SShot}"

	sleep 2 

	vboxmanage startvm "${VM}"

fi


