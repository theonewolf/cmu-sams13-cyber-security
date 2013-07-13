#!/usr/bin/env python



from random import shuffle
from sys import argv



USAGE = '''%s <list of files to pick splits>'''




if __name__ == '__main__':
    if len(argv) < 2:
        print USAGE % argv[0]
        exit(1)

    files = argv[1:]
    shuffle(files)

    print './nbayes_counter.py ',
    for fname in files[1:int(len(files)*0.90)]:
        print '%s ' % fname,

    print ''
    for fname in files[int(len(files)*0.90):]:
        print './nbayes_decider.py ham_counts.json spam_counts.json %s' % fname
