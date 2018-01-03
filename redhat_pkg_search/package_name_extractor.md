


Provided a list of packages with version numbers, extract the package name

For example:

	gnome-vfs2-2.24.4-14.el7.x86_64 => gnome-vfs2


Passed as a single string argument, this will work:

```python
import re
import sys

def getname(pkg):
    for x in range(1, len(pkg)):
        if not re.search('\d+', pkg[x]):
            continue        
        else:
            if pkg[x-1] == '-':
                print pkg[:x-1]
                break
            else:
                continue

def main(arg):
    getname(arg)

if __name__ == "__main__":
    main(sys.argv[1])
```

### Working with a list contained in a file

The same tool can be used as follows

```python
import re
import sys

def getname(pkg):
    for x in range(1, len(pkg)):
        if not re.search('\d+', pkg[x]):
            continue        
        else:
            if pkg[x-1] == '-':
                print pkg[:x-1]
                break
            else:
                continue

def main(path):
    with open(path, 'r') as fin:
        for line in fin.readlines():
            getname(line)

if __name__ == "__main__":
    main(sys.argv[1])
```


### Example List

gnome-vfs2-2.24.4-14.el7.x86_64
gnome-video-effects-0.4.3-1.el7.noarch
gnome-weather-3.20.2-1.el7.noarch
gnote-3.22.1-1.el7.x86_64
gnu-free-fonts-common-20120503-8.el7.noarch
gnu-free-mono-fonts-20120503-8.el7.noarch
gnu-free-sans-fonts-20120503-8.el7.noarch
gnu-free-serif-fonts-20120503-8.el7.noarch
gnutls-dane-3.3.26-9.el7.x86_64
gnutls-utils-3.3.26-9.el7.x86_64
gom-0.3.2-1.el7.x86_64
google-chrome-stable-63.0.3239.108-1.x86_64



