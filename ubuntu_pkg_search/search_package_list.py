#!/usr/bin/python
###########################################################
# given a plaintext file with package names, one per line
# check to see if the package has an install candidate 
# and report status to screen as well as write the package
# not found to the outfile
###########################################################

import subprocess
import sys
import getopt


def parselines(pkgnamesfile, failfilename):

	searched = 0   # not using len as there are potentially  blanks
	success = 0
	failure = 0
	unknown = 0
	
	failfile = open(failfilename, "w")
	
	with open(pkgnamesfile, "r") as fin:
		lines = [x.strip() for x in fin.readlines()]
		for line in lines:
			tokens = line.split()
			if tokens:
				pkgname = tokens[-1]
				p = subprocess.Popen(['aptitude', 'search', pkgname], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				out, err = p.communicate()
				if out:
					print("+++ package: " + pkgname + " has install candidate")
					success += 1
				else:
					failfile.write(pkgname + "\n")
					print("--- Package " + pkgname + " has no install candidate.")
					failure += 1
				searched += 1

		print("Packages Searched: " + str(searched) + " Success: " + str(success) + " Failed: " + str(failure))


def main(argv):
	inputfile = ""
	outputfile = ""

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print("search_package_list.py -i <packagelist> -o <outputfile>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("search_package_list.py -i <packagelist> -o <outputfile>")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	
	parselines(inputfile, outputfile)


if __name__ == '__main__':
	main(sys.argv[1:])


