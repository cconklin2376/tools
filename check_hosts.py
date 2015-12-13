#!/usr/bin/python
import os

ips= []
netwk = "192.168.0."
minip = 1
maxip = 23


print("Checking network " + netwk + " hosts(" + str(minip) + " - " + str(maxip))
for val in range(minip, maxip):
	hostname = netwk + str(val)
	ret = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
	if ret == 0:
		print hostname + " : " + str(ret)

