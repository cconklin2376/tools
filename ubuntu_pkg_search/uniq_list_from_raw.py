#!/usr/bin/python

# extend this to allow passing filenames

outfilename = "uniq_pkg_list"
infilename = "combined_raw"

itemcnt = 0
collisions = 0

lines_seen = set()

with open(outfilename, "w") as fout:
	with open(infilename, "r") as fin:
		lines = [x.strip() for x in fin.readlines()]
		for line in lines:
			tokens = line.split()
			if tokens:
				itemcnt += 1
				pkgname = tokens[-1]
				if pkgname not in lines_seen:
					print("+++ Adding package: " + pkgname)
					fout.write(pkgname + "\n")
					lines_seen.add(pkgname)
				else:
					collisions += 1
					print("--- Package " + pkgname + " already exists.")

print("Items: " + str(itemcnt) + " Collisions: " + str(collisions))
