# breakdown of a package line:
# <string>-[<string>-]*#[.#]*-#.(x86_64|noarch|i686).rpm

infile = "target_rpms"
outfile = "test_out"

inf = open(infile, 'r')
outf = open(outfile, 'w')


# python-gevent-websocket-0.9.5-1.noarch.rpm
for line in inf.readlines():
        
    pkgname = ''
    tokens = line.split('-')
    # ['python', 'gevent', 'websocket','0.9.5', '1.noarch.rpm']
    for t in tokens:
        # ascii numbers 48 - 57
        if not (48 <= ord(t[0]) <= 57):
            #t.join(pkgname)
            pkgname += (t + '-')
        else:
            if pkgname[-1] == '-':
                pkgname = pkgname[:-1]
    print pkgname

