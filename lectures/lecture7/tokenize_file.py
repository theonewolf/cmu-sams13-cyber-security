#!/usr/bin/env python



import fileinput
import json
from sys import argv
from base64 import b64encode



USAGE = '''%s <file to tokenize>'''



if __name__ == '__main__':
    if len(argv) != 2:
        print USAGE % argv[0]
        exit(1)

    bag_of_words = set() 
    for line in fileinput.input():
        bag_of_words.update(set([b64encode(token) for token in line.split()]))

    print json.dumps(list(bag_of_words))
