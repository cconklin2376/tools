#!/usr/bin/env python

# desired changes:
# add parm for lower or upper case
# add parm for dot qualifier in row name
# add export for v_variable_name, list

import sys

usage = '''
Banner Insert Variables Generator
cconklin 4/16/15

USAGE:

$ python ban_insert_vars.py <file>

Where <file> is a raw plain-text file containing a dump
from a toad db table script file:

example 

PEREHIS_PIDM                    NUMBER(8)     NOT NULL,
...etc
  
OUTPUT (2 files): 
variables.txt output:

v_PEREHIS_PIDM                      PEREHIS_PIDM%TYPE;
etc...

justnames.txt output:

PEREHIS_PIDM,
...etc
'''

outfile = open('type_variables.txt', 'w')
justnames = open('justnames.txt', 'w')
varfile = open('v_variables.txt', 'w')

ender = '%TYPE;'
starter = 'v_'
fields = []

def main():
    
    if len(sys.argv) < 2:
        print usage
        sys.exit()
    
    with open(sys.argv[1], 'r') as infile:
        for x in infile.readlines():
            line = x.split()
            fields.append(line[0])
    
        for k in fields:
            justnames.write(k + ',\n')
	    varfile.write(('v_' + k + ',\n')) 
            vardef = starter + k
            if len(vardef) > 30:
                print("\nWarning: generated variable name exceeds 30 char max (len=" + str(len(vardef)) + ") for var " + vardef + "\n")
            outfile.write('\t' + starter + k.ljust(34) + k[:7] + '.' + k + ender + '\n')
        



if __name__ == '__main__':
    main()
