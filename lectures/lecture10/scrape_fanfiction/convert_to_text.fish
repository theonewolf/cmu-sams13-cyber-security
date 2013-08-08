#!/usr/bin/fish

echo '#!/bin/bash'

for story in (seq 1 1 $argv[2])
    echo "grep \"<div class='storytext xcontrast_txt' id='storytext'>\" $argv[1]/story_$story.html | ./strip_html_tags.py > $argv[1]/story_$story.txt"
end
