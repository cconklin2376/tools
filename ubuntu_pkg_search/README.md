
# Purpose:

### Usage

$ python package_search.py -i inputfile -o resultsfile

Where 

- inputfile is a list of packages, one per line, to be searched

-  resultsfile is an output file containing the list of packages that were not found.

The tool also writes to stdout as each package is searched

```
+++ package: libplot2c2 has install candidate
+++ package: libplymouth2:amd64 has install candidate
+++ package: libpng12-0:amd64 has install candidate
--- Package libpng12-0:i386 has no install candidate.
+++ package: libpng12-dev has install candidate
+++ package: libpod-latex-perl has install candidate
+++ package: libpolkit-agent-1-0:amd64 has install candidate
```

Once execution is completed a status line displays the number of packages
searched, the number found and the number not found.

### Creating a list

A list of installed software on a client can be obtained in several ways. 
The simplest is probably running:

```
$ dpkg -l | awk '{ print $2 }' > inputfile
```

