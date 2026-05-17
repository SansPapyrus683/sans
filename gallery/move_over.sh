#!/usr/bin/env bash

if [ "$#" -ne 2 ]; then
    echo "how to use: $0 <from> <to>"
    exit 1
fi

from="$1"
to="$2"

if [[ ! -d $from ]]; then
    echo "$from isn't a directory"
    exit 1
fi

if [[ ! -d $to ]]; then
    echo "$to isn't a directory"
    exit 1
fi

for dir in "$from"/*/; do
    [ -d "$dir" ] || continue

    dest="$to/$(basename $dir)"
    echo "$dir -> $dest"

    find $dir \
        -type f -cmin -10 \
        -exec cp -np {} $dest \;
done
