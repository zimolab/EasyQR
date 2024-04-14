from typing import Optional

from easyqr._enum import _Enum


class OverwriteBehavior(_Enum):
    Ask = "ASK"
    NotOverwrite = "Not_OVERWRITE"
    Overwrite = "OVERWRITE"

    @classmethod
    def value_of(
        cls,
        value: str,
        default: Optional["OverwriteBehavior"] = None,
        raise_error: bool = True,
    ) -> Optional["OverwriteBehavior"]:
        value = value.upper()
        return super().value_of(value, default, raise_error)
