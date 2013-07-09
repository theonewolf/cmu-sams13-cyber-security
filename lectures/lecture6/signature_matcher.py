#!/usr/bin/env python



from sys import argv



USAGE = '''%s <signatures file> <target file to scan>'''



def read_signature_file(sig_fname):
    signatures = []
    for line in open(sig_fname).readlines():
        if (line.strip()):
            signatures.append(line.strip().split(','))
    return signatures

def read_target(target_fname):
    return open(target_fname).read()

def bytes_to_string(array):
    byte_string = ''
    for b in array:
        byte_string += '%0.2x' % ord(b)
    return byte_string

def scan_target(signatures, target):
    found = True

    for signature in signatures:
        position = int(signature[0])
        hex_sig = signature[1]
        size = len(hex_sig) / 2
        
        if position + size > len(target):
            return False

        query = target[position : position + size]
        hex_query = bytes_to_string(query)

        if hex_query != hex_sig:
            found = False

    return found 



if __name__ == '__main__':
    if len(argv) < 3:
        print USAGE % argv[0]
        exit(1)

    sig_fname = argv[1]
    target_fname = argv[2]

    signatures = read_signature_file(sig_fname)
    target = read_target(target_fname)

    if scan_target(signatures, target):
        print '+ MATCH FOUND "%s"' % target_fname
    else:
        print '- NO MATCH FOUND "%s"' % target_fname
