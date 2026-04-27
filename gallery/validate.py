"""
given a list of directories, this script does a couple of things

for each directory, it checks the following:
1. each post's numbers are a prefix of the natural numbers (so no missing images)
2. a single post id doesn't correspond to multiple authors
   (not really relevant for me anymore since i use gallery-dl,
    but might still be useful as a sanity check)

it also modifies mtime of files s.t. sorting by last modified will
give you an order as if you were scrolling through your actual timeline

this script assumes that all posts meet the regex described in parse.py
"""

import argparse
import os
from datetime import datetime, timedelta
from itertools import groupby

from parse import Post

cmd_args = argparse.ArgumentParser(prog="post validator")
cmd_args.add_argument("directory", nargs="+")
cmd_args.add_argument("-r", "--only-recent", action="store_true")
args = cmd_args.parse_args()


def validate_directory(dir_: str):
    print(f"Validating {dir_}")

    initial_dir = os.getcwd()
    os.chdir(dir_)

    all_tweets = [Post.from_str(i) for i in os.listdir()]
    all_tweets.sort(key=lambda t: (t.id, t.pos))

    for id_, tweet in groupby(all_tweets, lambda t: t.id):
        tweet = list(tweet)  # turns out iterating over this destroys it???
        all_authors = {t.author for t in tweet}
        all_nums = [t.pos for t in tweet]  # sorting taken care of by initial ordering

        if len(all_authors) > 1:
            # this error shouldn't get hit anymore since i've switched to gallery-dl
            # but ig it's still nice as a sanity check
            print(f"tweet {id_} has multiple authors (handle change?): {all_authors}")
        if all_nums != list(range(1, len(all_nums) + 1)):
            print(f"tweet {id_} seems to be missing some photos- i only see {all_nums}")

    if args.only_recent:
        new_tweets = []
        today = datetime.today().date()
        for i in os.listdir():
            ctime = os.path.getctime(i)
            cdate = datetime.fromtimestamp(ctime).date()
            if cdate == today:
                new_tweets.append(i)
    else:
        new_tweets = os.listdir()
    new_tweets = [Post.from_str(i) for i in new_tweets]
    new_tweets.sort(key=lambda t: (-t.id, t.pos))

    now = datetime.now()
    epoch = datetime(1970, 1, 1)
    for v, t in enumerate(new_tweets):
        delta = (now - timedelta(seconds=3 * v) - epoch).total_seconds()
        os.utime(str(t), times=(delta, delta))

    os.chdir(initial_dir)


for d in args.directory:
    validate_directory(d)
