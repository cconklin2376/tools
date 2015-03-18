import urllib
import re


# look at http://stackoverflow.com/questions/1949318/checking-if-a-website-is-up-via-python
# and
# http://stackoverflow.com/questions/839994/extracting-a-url-in-python

inf = open('bookmarks.html', 'r')
onf = open('status.txt', 'w')

baddies = []
goodies = []

for line in inf.readlines():
	k = re.search("(?P<url>https?://[^\s>\"]+)", line)
	if k is not None:
		url = k.group("url")	
		status = urllib.urlopen(url).getcode()
		if status == '200':
			goodies.append(url)
		else:
			baddies.append(url)

onf.write("Good Urls:\n")
for x in goodies:
	onf.write(x + "\n")

onf.write("Broken Urls:\n")
for y in baddies:
	onf.write(y + "\n")
