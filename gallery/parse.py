import os
import re
from dataclasses import dataclass

# the format i use for both tumblr ad twitter posts
POST_FMT = re.compile(r"^([-\w]+)_(\d+)_(\d+)")


@dataclass
class Post:
    author: str
    id: int
    pos: int
    ext: str  # HAS THE PERIOD!!!!

    def __repr__(self):
        return f"{self.author}_{self.id}_{self.pos}{self.ext}"

    @classmethod
    def from_str(cls, file: str) -> Post | None:
        name, ext = os.path.splitext(file)
        if (parsed := POST_FMT.match(name)) is None:
            return None

        author, id_, pos = parsed.groups()
        return cls(author, int(id_), int(pos), ext)
