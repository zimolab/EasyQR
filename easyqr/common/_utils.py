from ._enum import OverwriteBehavior
from ._constants import OVERWRITE_BEHAVIORS, TR_ERR_INVALID_OVERWRITE_BEHAVIOR


def get_overwrite_behavior(tr_value: str) -> OverwriteBehavior:
    behavior = OVERWRITE_BEHAVIORS.get(tr_value, None)
    if behavior is None:
        raise ValueError(TR_ERR_INVALID_OVERWRITE_BEHAVIOR.format(tr_value))
    return behavior
