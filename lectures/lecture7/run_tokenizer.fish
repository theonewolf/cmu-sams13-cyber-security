#!/usr/bin/fish

find ham/*.eml -print0 | xargs -0 ./tokenize_files.py > /tmp/log.json
