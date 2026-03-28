import sys
import os
from collections import defaultdict
from datetime import datetime, timedelta
import re

fmt = re.compile(r"(\d+)_(.*)_(\d+)\.")

os.chdir(sys.argv[1])

groups = defaultdict(list)
for i in os.listdir():
    id_, author, num = fmt.match(i).groups()
    id_, num = int(id_), int(num)
    groups[id_].append((author, num, i))

for id_, tweets in sorted(groups.items(), reverse=True):
    tweets.sort(key=lambda t: t[1])
    all_authors = {t[0].lower() for t in tweets}
    all_nums = [t[1] for t in tweets]

    if len(all_authors) > 1:
        print("tweet {id_} has multiple authors: {all_authors}")
    if all_nums != list(range(1, len(all_nums) + 1)):
        print(f"tweet {id_} seems to be missing some photos- i only see {all_nums}")
