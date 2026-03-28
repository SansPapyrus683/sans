import sys
import os
import re

migrate_dir = "<RELEVANT DIRECTORY>"
fmt = re.compile(r"(\d+)_(.*)_(\d+)\.")

old_handle = sys.argv[1].lower()
new_handle = sys.argv[2]
print(f"{old_handle} -> {new_handle}. yes?")
if input().lower() not in ["y", "yes"]:
    sys.exit()

os.chdir(migrate_dir)
to_rename = []
for i in os.listdir():
    match = fmt.match(i)
    id_ = int(match.group(1))
    author = match.group(2)
    pos = int(match.group(3))
    ext = os.path.splitext(i)[1]

    if author.lower() == old_handle:
        to_rename.append((i, f"{id_}_{new_handle}_{pos}{ext}"))

for old, new in to_rename:
    print(old, new)
    os.rename(old, new)
