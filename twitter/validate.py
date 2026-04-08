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

    base_tweets = os.listdir()
    if args.only_recent:
        new_tweets = []
        today = datetime.today().date()
        for i in base_tweets:
            ctime = os.path.getctime(i)
            cdate = datetime.fromtimestamp(ctime).date()
            if cdate == today:
                new_tweets.append(i)
        base_tweets = new_tweets

    all_tweets = [Post.from_str(i) for i in base_tweets]
    all_tweets.sort(key=lambda t: (t.id, t.pos))

    for id_, tweet in groupby(all_tweets, lambda t: t.id):
        tweet = list(tweet)  # turns out iterating over this destroys it???
        all_authors = {t.author for t in tweet}
        all_nums = [t.pos for t in tweet]  # sorting taken care of by initial ordering

        if len(all_authors) > 1:
            print(f"tweet {id_} has multiple authors (handle change?): {all_authors}")
        if all_nums != list(range(1, len(all_nums) + 1)):
            print(f"tweet {id_} seems to be missing some photos- i only see {all_nums}")

    all_tweets.sort(key=lambda t: (-t.id, t.pos))

    now = datetime.now()
    epoch = datetime(1970, 1, 1)
    for v, t in enumerate(all_tweets):
        delta = (now - timedelta(seconds=3 * v) - epoch).total_seconds()
        os.utime(str(t), times=(delta, delta))
    
    os.chdir(initial_dir)


for d in args.directory:
    validate_directory(d)
