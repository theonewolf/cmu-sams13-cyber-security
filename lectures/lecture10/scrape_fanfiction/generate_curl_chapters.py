#!/usr/bin/env python

from sys import argv
import re
import fileinput

STORY_COUNTER = 1
URL_RE = '''.*<a class=stitle href="/s/(\d+)/1/([^"]+)">.*'''
URL_RE_COMPILED = re.compile(URL_RE, flags=re.UNICODE)
CHAPTERS_RE = '''.*Chapters: (\d+).*'''
CHAPTERS_RE_COMPILED = re.compile(CHAPTERS_RE)
URL_STRING = '''curl --retry 10 "http://www.fanfiction.net/s/%s/%d/%s" \
>> %s/story_%d.html'''


def generate_story_links(special_num, story_title, chapters, category):
    global STORY_COUNTER
    for chapter in xrange(1, chapters + 1, 1):
        print URL_STRING % (special_num, chapter, story_title, category,
                            STORY_COUNTER)
    STORY_COUNTER += 1

if __name__ == '__main__':
    special_num = None
    story_title = None
    chapters = None
    category = argv[1]

    print '#!/bin/bash'

    for line in fileinput.input(argv[2:]):
        stitle_match = URL_RE_COMPILED.match(line)
        chapters_match = CHAPTERS_RE_COMPILED.match(line)

        if stitle_match:
            special_num = stitle_match.group(1)
            story_title = stitle_match.group(2)
        
        if chapters_match:
            chapters = int(chapters_match.group(1))

        if special_num and story_title and chapters:
            generate_story_links(special_num, story_title, chapters, category)
            special_num = None
            story_title = None
            chapters = None
