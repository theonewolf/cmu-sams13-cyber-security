#!/usr/bin/env python



from sys import argv



USAGE = '''%s <pi file> <offset> <length>'''



if __name__ == '__main__':
    if len(argv) < 4:
        print USAGE % argv[0]
        exit(1)

    offset = int(argv[2])
    length = int(argv[3])

    with open(argv[1]) as fd:
        data = fd.read()
        print data[offset : offset + length]
