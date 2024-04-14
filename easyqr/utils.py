import os.path
import random
import string


def curdir() -> str:
    return os.path.abspath(os.getcwd())


def rand_str(length: int = 8) -> str:
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def rand_filename(prefix: str = "", ext: str = ".png") -> str:
    return f"{prefix}{rand_str()}{ext}"


def safe_pop(d: dict, key: str) -> bool:
    try:
        d.pop(key)
        return True
    except KeyError:
        return False
