import os
from ._enum import OverwriteBehavior
from ._constants import OVERWRITE_BEHAVIORS, TR_ERR_INVALID_OVERWRITE_BEHAVIOR


def get_overwrite_behavior(tr_value: str) -> OverwriteBehavior:
    behavior = OVERWRITE_BEHAVIORS.get(tr_value, None)
    if behavior is None:
        raise ValueError(TR_ERR_INVALID_OVERWRITE_BEHAVIOR.format(tr_value))
    return behavior


def get_file_ext(path: str) -> str:
    _, ext = os.path.splitext(path)
    return ext

def is_same_filetype(path: str, file_ext: str, ignore_case: bool = True) -> bool:
    target_ext = get_file_ext(path)
    if ignore_case:
        target_ext = target_ext.lower()
        file_ext = file_ext.lower()
    return target_ext == file_ext