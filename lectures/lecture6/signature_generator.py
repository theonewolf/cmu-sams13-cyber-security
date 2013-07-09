#!/usr/bin/env python



from random import randint
from sys import argv




USAGE='''%s <signature size in bytes> <input file>'''




def read_file(fname):
    return bytes(open(fname).read())

def random_bytes(num, fdata):
    position = randint(0,len(fdata) - num)
    return (position, fdata[position : position + num])

def bytes_to_string(array):
    byte_string = ''
    for b in array:
        byte_string += '%0.2x' % ord(b)
    return byte_string




if __name__ == '__main__':
    if len(argv) < 3:
        print USAGE % argv[0]
        exit(1)

    num = int(argv[1])
    fname = argv[2]
    position, signature = random_bytes(num, read_file(fname))
    print '%d,%s' % (position, bytes_to_string(signature))
