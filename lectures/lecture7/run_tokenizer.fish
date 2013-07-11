#!/usr/bin/fish

for f in ham_extracted/*.eml
    ./tokenize_file.py $f > ham_extracted/(basename $f).json
end
