import os
import sys

from parse import Post

if len(sys.argv) < 4:
    print("args are directory, old name, and new handle")

os.chdir(sys.argv[1])

old_handle = sys.argv[2].lower()
new_handle = sys.argv[3]
print(f"{old_handle} -> {new_handle}. yes?")
if input().lower() not in ["y", "yes"]:
    sys.exit()

for i in os.listdir():
    post = Post.from_str(i)
    if post.author.lower() != old_handle:
        continue
    post.author = new_handle
    print(f"{i} -> {post}")
    # os.rename(i, str(post))
