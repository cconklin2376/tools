
# Purpose:

- This was written to produce a list of package names
that appear in the documentation as needing an install
candidate and have a candidate on the existing OS release,
but do not have a candidate for the new release.


Ubuntu-14.04 cfengine space scan and combine:

Sources:
	/common/cfengine/ws/masterfiles/Ubuntu-14.04
	/common/cfengine/ws/masterfiles/Ubuntu-14.04/sw
	/common/cfengine/ws/repository/Ubuntu-14.04/etc/castle


- comb through the masterfiles softare to create raw_masterfile_pkgs
- cat castle_software, department_software, host_software into raw files for each file
- clean the raw files to remove duplicates, "ignore" packages and "remove" packages entries, 
  blank lines and combine into a single file:

cat raw* | grep -v -e '^$' | grep -v ^# | grep -v ^remove | grep -v ^ignore > combined_raw

Now run the python uniq tool to create a list of package names that are unique
 

python make_uniq_pkg_list.py combined_raw
->> nodupes


Now feed that list into package_search.py and save the outout
python package_search.py -i <infile> -o <outile> 

