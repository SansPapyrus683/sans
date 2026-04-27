#!/usr/bin/env bash

DIR="${1:-.}" # defaults to current directory

# i'm ngl i have gpt write all my bash scripts
for file in "$DIR"/*.webp; do
    [ -e "$file" ] || continue

    output="${file%.webp}.png"
    if dwebp "$file" -o "$output" -quiet; then
        rm -- "$file"
        echo "$file -> $output"
    else
        echo "Failed to convert $file" >&2
    fi
done
