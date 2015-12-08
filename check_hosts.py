#!/usr/env/python
import os

ips= []
netwk = "192.168.0."

for val in range(1,30):
	hostname = netwk + str(val)
	ret = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
	if ret == 0:
		print hostname + " : " + str(ret)

