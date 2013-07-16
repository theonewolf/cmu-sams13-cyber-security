#!/usr/bin/env python



from sys import stdout,argv



USAGE = '''%s <key file> <ciphertext or plaintext file>'''



def vernam_cipher(key, data):
    return bytearray([db ^ key[i] for i,db in enumerate(data)])

def file_blocks(f):
    data = bytearray(f.read(4096))
    while data:
        yield data
        data = bytearray(f.read(4096))



if __name__ == '__main__':
    if len(argv) < 3:
        print USAGE % argv[0]
        exit(1)

    with open(argv[1], 'r') as keyfile:
        with open(argv[2], 'r') as datafile:
            for block in file_blocks(datafile):
                key = bytearray(keyfile.read(len(block)))
                stdout.write(vernam_cipher(key, block))
