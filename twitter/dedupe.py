import os
import sys
from collections import defaultdict

from PIL import Image
import imagehash

from parse import Post

os.chdir(sys.argv[1])

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
    for i in ids:
        g[i].sort()  # and on each id the images should be in order

    for i in range(len(ids)):
        g1 = g[ids[i]]
        for j in range(i + 1, len(ids)):
            g2 = g[ids[j]]

            if len(g1) != len(g2):
                continue

            for a, b in zip(g1, g2):
                if a[2] - b[2] >= 3:
                    break
            else:
                to_del.extend(g1)
                duped.append((g1, g2))
                break

"""
for v, (g1, g2) in enumerate(duped):
    for u, (a, b) in enumerate(zip(g1, g2)):
        ext1 = os.path.splitext(a[1])[1]
        ext2 = os.path.splitext(b[1])[1]
        shutil.copy(a[1], f"dupes/{v}_{u}_0.{ext1}")
        shutil.copy(b[1], f"dupes/{v}_{u}_1.{ext2}")
"""

for d in to_del:
    os.remove(d[1])
