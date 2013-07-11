#!/usr/bin/env python



import json
from sys import argv



USAGE = '''%s <list of file names>'''



if __name__ == '__main__':
    if len(argv) < 2:
        print USAGE % argv[0]
        exit(1)

    total_examples = len(argv) - 1

    counts = {}
    counts['total_examples'] = total_examples
    for i in xrange(1, len(argv), 1):
        with open(argv[i]) as f:
            tokens = json.load(f)
            for token in tokens:
                counts[token] = counts.get(token, 0) + 1
        
    print json.dumps(counts)
