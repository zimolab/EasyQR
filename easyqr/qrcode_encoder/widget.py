import dataclasses
from typing import Any, List

from function2widgets.widgets.base import (
    CommonParameterWidget,
    CommonParameterWidgetArgs,
)


@dataclasses.dataclass(frozen=True)
class ColorsGroupArgs(CommonParameterWidgetArgs):
    parameter_name: str
    default: Any = None
    color_labels: List[str] = dataclasses.field(default_factory=list)
