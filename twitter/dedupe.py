import os
from collections import defaultdict
import re
import shutil

from PIL import Image
import imagehash

fmt = re.compile(r"(\d+)_(.*)_(\d+)\.")

path = os.path.expanduser("/run/media/sanspapyrus683/PHILIPS/twitter")

os.chdir(path)

tweets = defaultdict(lambda: defaultdict(list))
for i in os.listdir():
    if i.endswith(".mp4"):
        continue

    match = fmt.match(i)
    id_ = int(match.group(1))
    author = match.group(2)
    pos = int(match.group(3))
    tweets[author][id_].append((pos, i, imagehash.average_hash(Image.open(i))))

to_del = []
duped = []
for author, g in tweets.items():
    ids = sorted(g.keys())
    for i in ids:
        g[i].sort()

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
        shutil.copy(a[1], f"../asdf/{v}_{u}_0.{ext1}")
        shutil.copy(b[1], f"../asdf/{v}_{u}_1.{ext2}")
"""

for d in to_del:
    os.remove(d[1])
