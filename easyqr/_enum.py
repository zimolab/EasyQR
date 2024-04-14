import enum
from typing import Any, Optional


class _Enum(enum.Enum):
    @classmethod
    def value_of(
        cls, value: Any, default: Optional["_Enum"] = None, raise_error: bool = True
    ) -> Optional["_Enum"]:
        member_found = None
        for _, member in cls.__members__.items():
            if member.value == value:
                member_found = member
                break
        if member_found is not None:
            return member_found
        if raise_error:
            raise ValueError(f"{value} is not a valid {cls.__name__}")
        return default

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value
