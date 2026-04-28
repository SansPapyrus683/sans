"""
when downloading tumblr images, gallery-dl does this weird thing where
it'll have image 1, image 2, image 3, and image 4 even though
the original post only has two images
then 3 & 4 will just be carbon copies of 1 & 2, idk why
this script just removes 3 & 4
"""
import argparse
import os
import shutil
from collections import defaultdict
from datetime import datetime
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

new_posts = os.listdir()
if args.only_recent:
    new_posts = []
    today = datetime.today().date()
    for i in os.listdir():
        ctime = os.path.getctime(i)
        cdate = datetime.fromtimestamp(ctime).date()
        if cdate == today:
            new_posts.append(i)

posts = defaultdict(list)
bad_ids = set()
for i in new_posts:
    post = Post.from_str(i)
    if post.ext == ".mp4":
        bad_ids.add(post.id)
        continue
    hash_ = imagehash.average_hash(Image.open(i))
    posts[post.id].append((post, hash_))

to_del = []
duped = []
for id_, imgs in posts.items():
    if len(imgs) % 2 == 1 or id_ in bad_ids:
        continue

    imgs.sort(key=lambda i: i[0].pos)
    half = len(imgs) // 2
    for i in range(half):
        j = half + i
        if imgs[i][1] - imgs[j][1] >= 3:
            break
    else:
        duped.extend(imgs)
        to_del.extend(imgs[half:])

if args.test_run:
    Path("dupes").mkdir(exist_ok=True)
    for i in duped:
        shutil.copy(str(i[0]), f"dupes/{i[0]}")
else:
    for d in to_del:
        name = str(d[0])
        print(f"deleting {name}")
        os.remove(name)
