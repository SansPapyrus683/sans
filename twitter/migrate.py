import os
import sys

from parse import Post

migrate_dir = "/home/sanspapyrus683/Downloads/gallery-dl/isitp2w"

old_handle = sys.argv[1].lower()
new_handle = sys.argv[2]
print(f"{old_handle} -> {new_handle}. yes?")
if input().lower() not in ["y", "yes"]:
    sys.exit()

os.chdir(migrate_dir)

for i in os.listdir():
    post = Post.from_str(i)
    if post.author.lower() != old_handle:
        continue
    post.author = new_handle
    os.rename(i, str(post))
