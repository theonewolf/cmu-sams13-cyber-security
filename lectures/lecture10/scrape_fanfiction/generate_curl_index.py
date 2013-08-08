#!/usr/bin/env python

from math import ceil
from sys import argv


TOTAL_PER_PAGE = 25
URL_STRING = '''curl --retry 10 \
"http://www.fanfiction.net/movie/%s/?&srt=1&lan=1&r=103&p=%d" \
> %s/index_%d.html'''

if __name__ == '__main__':
    category = argv[1]
    count = argv[2]

    pages_to_scrape = int(ceil(float(count) / TOTAL_PER_PAGE))

    print '#!/bin/bash'

    for i in xrange(1,pages_to_scrape + 1,1):
        print URL_STRING % (category, i, category, i) 
