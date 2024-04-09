import dataclasses
from typing import Any, Dict, Union, cast, Optional, Literal

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QPushButton, QColorDialog, QGridLayout
from function2widgets.widget import InvalidValueError
from function2widgets.widgets.base import (
    CommonParameterWidget,
    CommonParameterWidgetArgs,
)
from function2widgets.widgets.misc import Color


@dataclasses.dataclass(frozen=True)
class ColorsGroupWidgetArgs(CommonParameterWidgetArgs):
    parameter_name: str
    default: Any = None
    with_alpha: bool = False
    display_format: Literal["hex", "rgb"] = "hex"
    colors: Dict[str, Union[str, Color]] = dataclasses.field(default_factory=dict)
    color_picker_title: Optional[str] = None
    columns: int = 1


class ColorPickButton(QPushButton):
    DEFAULT_COLOR = Color.from_string("#ffffff")
    DEFAULT_STYLESHEET = "QPushButton{font-weight:bold;}"

    def __init__(
        self,
        init_color: Union[str, Color, None] = None,
        with_alpha: bool = True,
        display_format: Literal["hex", "rgb"] = "hex",
        color_picker_title: Optional[str] = None,
        color_label: str = "",
        parent=None,
    ):
        super().__init__(parent)
        if init_color is None:
            init_color = self.DEFAULT_COLOR
        if isinstance(init_color, str):
            init_color = Color.from_string(init_color)

        self._init_color = init_color
        self._with_alpha = with_alpha
        self._display_format = display_format
        self._color_picker_title = color_picker_title
        self._color_label = color_label

        self._setup_ui()

    def set_color_label(self, label: str):
        self._color_label = label

    def get_color(self) -> Color:
        palette = self.palette().button()
        qt_color = palette.color()
        return Color.from_qt_color(qt_color)

    def set_color(self, color: Union[str, Color, QColor]):
        self._set_bg_color(color)
        self._update_color_text(color)

    def _setup_ui(self):
        self.setStyleSheet(self.DEFAULT_STYLESHEET)
        self.setAutoFillBackground(True)
        self.setFlat(True)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setCheckable(False)
        self.setAutoDefault(False)
        self.setDefault(False)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # noinspection PyUnresolvedReferences
        self.clicked.connect(self._on_pick_color)

        self.set_color(color=self._init_color)

    def _update_color_text(self, bg_color: Union[str, Color, QColor]):
        if isinstance(bg_color, str):
            bg_color = Color.from_string(bg_color)
        if isinstance(bg_color, QColor):
            bg_color = Color.from_qt_color(bg_color)

        invert_color = bg_color.get_invert_color()
        invert_color.a = 255
        invert_color = invert_color.to_qt_color()
        if self._display_format.lower() == "hex":
            color_text = bg_color.to_hex_string(with_alpha=self._with_alpha)
        else:
            color_text = bg_color.to_rgb_string(with_alpha=self._with_alpha)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.ButtonText, invert_color)
        self.setPalette(palette)
        if self._color_label:
            color_text = f"{self._color_label}\n{color_text}"
        self.setText(color_text)

    def _set_bg_color(self, color: Union[str, Color, QColor]):
        if isinstance(color, str):
            color = QColor.fromString(color)
        if isinstance(color, Color):
            color = color.to_qt_color()
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Button, color)
        self.setPalette(palette)

    def _on_pick_color(self):
        dialog_title = self._color_picker_title
        options = QColorDialog.ColorDialogOption.DontUseNativeDialog
        if self._with_alpha:
            options = options | QColorDialog.ColorDialogOption.ShowAlphaChannel
        color = QColorDialog.getColor(
            self.get_color().to_qt_color(),
            self,
            dialog_title,
            options,
        )
        if not color or not color.isValid():
            return
        self.set_color(color)


class ColorsGroupWidget(CommonParameterWidget):
    SET_DEFAULT_ON_INIT = True
    HIDE_DEFAULT_VALUE_WIDGET = True
    _WidgetArgsClass = ColorsGroupWidgetArgs

    def __init__(self, args: ColorsGroupWidgetArgs, parent=None):
        colors = args.colors
        if colors is None or len(colors) == 0:
            raise InvalidValueError("args.colors should contain at least one color")
        colors = {
            name: Color.from_string(color) if isinstance(color, str) else color
            for name, color in colors.items()
        }
        args = dataclasses.replace(args, colors=colors)
        self._color_buttons = {}
        super().__init__(args=args, parent=parent)

        if self._args.set_default_on_init:
            self.set_value(self._args.default)

    @property
    def _args(self) -> ColorsGroupWidgetArgs:
        return cast(ColorsGroupWidgetArgs, super()._args)

    def setup_center_widget(self, center_widget: QWidget):
        center_widget_layout = QGridLayout(center_widget)
        center_widget_layout.setContentsMargins(0, 0, 0, 0)
        center_widget.setLayout(center_widget_layout)
        column_count = self._args.columns
        for i, color_label in enumerate(self._args.colors.keys()):
            btn = ColorPickButton(
                init_color=self._args.colors[color_label],
                with_alpha=self._args.with_alpha,
                display_format=self._args.display_format,
                color_picker_title=self._args.color_picker_title,
                color_label=color_label,
                parent=center_widget,
            )
            self._color_buttons[color_label] = btn
            if i % column_count == 0:
                center_widget_layout.addWidget(btn, i // column_count, 0)
            else:
                center_widget_layout.addWidget(btn, i // column_count, i % column_count)

    def set_value(self, value: Optional[Dict[str, Union[str, Color]]]):
        if value is not None and not isinstance(value, dict):
            raise InvalidValueError(f"value should be a dict, but got {type(value)}")
        if isinstance(value, dict):
            value = {
                name: Color.from_string(color) if isinstance(color, str) else color
                for name, color in value.items()
            }
        super().set_value(value)

    def get_value(self) -> Dict[str, Color]:
        return super().get_value()

    def set_value_to_widget(self, value: Dict[str, Union[str, Color]]):
        for color_label, color in value.items():
            if color_label not in self._args.colors:
                continue
            btn = self._color_buttons.get(color_label)
            if isinstance(color, str):
                color = Color.from_string(color)
            btn.set_color(color)

    def get_value_from_widget(self) -> Dict[str, Color]:
        return {
            color_label: btn.get_color()
            for color_label, btn in self._color_buttons.items()
        }
