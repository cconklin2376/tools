#!/usr/bin/python
import os
import datetime

ips= []
netwk = "192.168.0."
minip = 1
maxip = 25
now = datetime.datetime.now().strftime("%h %d")

print("Checking network " + netwk + " hosts(" + str(minip) + " - " + str(maxip) + ") on " + now + " \n\n")
for val in range(minip, maxip):
	hostname = netwk + str(val)
	ret = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
	if ret == 0:
		print hostname + " is online.\n"

