import os.path
import random
import string
from typing import Literal


def curdir() -> str:
    return os.path.abspath(os.getcwd())


def rand_str(length: int = 8) -> str:
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def rand_filename(prefix: str = "", ext: Literal[".png", ".svg"] = ".png") -> str:
    return f"{prefix}{rand_str()}{ext}"
