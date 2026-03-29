import sys
import os
from datetime import datetime, timedelta
from itertools import groupby

from parse import Post

os.chdir(sys.argv[1])

all_tweets = [Post.from_str(i) for i in os.listdir()]
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
