#!/usr/bin/python
import os
import json


def get_online_hosts_str(minip, maxip, netwk='192.168.0.'):	
	hostinfo = {}
	for val in range(minip, maxip):
		host = netwk + str(val)
		if check_host(host):
			hostinfo[host] = 'online'
	return json.dumps(hostinfo)

def check_host(ip):
	ret = os.system("ping -c 1 " + ip + " > /dev/null 2>&1")
	if ret == 0:
		return 1
	else:
		return 0

def main():
	print(get_online_hosts_str(2,10))



if __name__ == "__main__":
	main()

