#!/usr/bin/env python



import fileinput
from json import loads
from sys import argv




USAGE = '''%s <results file>'''



if __name__ == '__main__':
    if len(argv) < 2:
        print USAGE % argv[0]
        exit(1)

    total = 0
    true_positives = 0
    true_negatives = 0

    for line in fileinput.input():
        data = loads(line)

        total += 1

        if int(data['chosen_class']) == 2 and \
           'spam' in data['file']:
               true_positives += 1

        if int(data['chosen_class']) == 1 and \
           'ham' in data['file']:
               true_negatives += 1

    accuracy = float(true_positives + true_negatives) / (total)
    print 'Accuracy ((TP + FP) / (TP + FP + FN + TN)) == %0.4f' % accuracy
