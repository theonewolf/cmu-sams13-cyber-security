#!/usr/bin/env python



import json
from math import log
from sys import argv



USAGE = '''%s <class 1 counts> <class 2 counts> <query tokens file>'''



if __name__ == '__main__':
    if len(argv) != 4:
        print USAGE % argv[0]
        exit(1)

    with open(argv[1]) as class1f:
        class1counts = json.load(class1f)
    with open(argv[2]) as class2f:
        class2counts = json.load(class2f)
    with open(argv[3]) as queryf:
        queryf_tokens = json.load(queryf)

    class1count = class1counts['total_examples']
    class2count = class2counts['total_examples']

    class1log = log(class1count)
    class2log = log(class2count)

    for token in queryf_tokens:
        class1log += log(float(class1counts.get(token, 1)) / class1count)
        class2log += log(float(class2counts.get(token, 1)) / class2count)

    result = { 'log(p1)' : class1log,
               'log(p2)' : class2log,
               'file'    : argv[3] }

    if class1log > class2log:
        result['chosen_class'] = 1
    else:
        result['chosen_class'] = 2

    print json.dumps(result)
