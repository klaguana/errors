#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys, os

def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision\n")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    assert 1/1 == 0 
    print 1/1
elif error_type == "io":
    open('bruh.py')
elif error_type == "import":
    from astropy import lel 
elif error_type == "index":
    pup = [ 0, 1, 2, 3, 4, 5 ]
    print pup[10] 
elif error_type == "key":
    bun_names = { 'Apollo':1, 'Bunbun':2, 'Butthole':3}
    print bun_names['bun']
elif error_type == "name":
    print(bruh)
elif error_type == "os":
    os.rmdir("breh")
elif error_type == "type":
    bunbun = "bun" + 2
    print bunbun
elif error_type == "value":
    print(float("bunbun"))
elif error_type == "zerodivision":
    print(5/0) 
elif error_type == "eof":
    while True:
        the_goodz = raw_input('Gimme yo digits gurl:')
        print 'AWWW YISSS', the_goodz
elif error_type == "syntax":
    print('∠( ᐛ 」∠)＿')
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
