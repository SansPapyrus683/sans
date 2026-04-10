import argparse
import os
import shutil
from collections import defaultdict
from pathlib import Path

import imagehash
from parse import Post
from PIL import Image

cmd_args = argparse.ArgumentParser(prog="post validator")
cmd_args.add_argument("directory")
cmd_args.add_argument(
    "-r",
    "--only-recent",
    action="store_true",
    help="only check if retweets created today have any duplicates",
)
cmd_args.add_argument(
    "-t",
    "--test-run",
    action="store_true",
    help="copy them into a new directory called dupes to check if they actually are (doesn't delete anything)",
)
args = cmd_args.parse_args()
os.chdir(args.directory)

tweets = defaultdict(lambda: defaultdict(list))
for i in os.listdir():
    # i... idk how to compare mp4s i'm not even gonna lie
    if i.endswith(".mp4"):
        continue
    post = Post.from_str(i)
    hash_ = imagehash.average_hash(Image.open(i))
    tweets[post.author][post.id].append((post, hash_))


to_del = []
duped = []
for author, g in tweets.items():
    # we wanna removes dupes with the lower id
    ids = sorted(g.keys())
    # and on each id the images should be in order
    for i in ids:
        g[i].sort(key=lambda p: p[0].pos)

    for i in range(len(ids)):
        g1 = g[ids[i]]
        for j in range(i + 1, len(ids)):
            g2 = g[ids[j]]

            if len(g1) != len(g2):
                continue

            for a, b in zip(g1, g2):
                if a[1] - b[1] >= 3:
                    break
            else:
                to_del.extend(g1)
                duped.append((g1, g2))
                break


if args.test_run:
    Path("dupes").mkdir(exist_ok=True)
    for v, (g1, g2) in enumerate(duped):
        for u, (a, b) in enumerate(zip(g1, g2)):
            a_name = str(a[0])
            b_name = str(b[0])
            shutil.copy(a_name, f"dupes/{v}_{u}_0.{a[0].ext}")
            shutil.copy(b_name, f"dupes/{v}_{u}_1.{b[0].ext}")
else:
    for d in to_del:
        os.remove(str(d[0]))
