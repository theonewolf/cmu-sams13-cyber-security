#!/usr/bin/env python



import math
import sys



__USAGE__ = '''%s <file to hash>'''



def long_to_bytearray(l):
    return bytearray.fromhex(hex(l)[2:-1])

def SAMS_hash(data):
    pass



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print __USAGE__ % sys.argv[0]
        exit(1)

    with open(sys.argv[1]) as f:
        data = f.read()
        print SAMS_hash(data)
