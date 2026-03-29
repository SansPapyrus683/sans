import os
import re
from dataclasses import dataclass

TWITTER_FMT = re.compile(r"^(\d+)_(\w+)_(\d+)")


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
        if (parsed := TWITTER_FMT.match(name)) is None:
            return None

        id_, author, pos = parsed.groups()
        return cls(author, int(id_), int(pos), ext)
