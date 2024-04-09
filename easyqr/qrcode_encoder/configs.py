from PyQt6.QtWidgets import QApplication
from function2widgets.widgets.misc import Color
from function2widgets.widgets.numberinput import IntSpinBox, FloatSpinBox
from function2widgets.widgets.numberinput import Slider
from function2widgets.widgets.pathedit import DirPathEdit, FilePathEdit
from function2widgets.widgets.selectwidget import ComboBox, RadioButtonGroup
from function2widgets.widgets.textedit import PlainTextEdit
from qrcode.image.svg import SvgPathImage
from qrcode.image.styles.moduledrawers.pil import (
    SquareModuleDrawer,
    GappedSquareModuleDrawer,
    CircleModuleDrawer,
    RoundedModuleDrawer,
    VerticalBarsDrawer,
    HorizontalBarsDrawer,
)
from qrcode.image.styles.moduledrawers.svg import (
    SvgPathSquareDrawer,
    SvgPathCircleDrawer,
)
from qrcode.constants import (
    ERROR_CORRECT_L,
    ERROR_CORRECT_M,
    ERROR_CORRECT_Q,
    ERROR_CORRECT_H,
)

from easyqr.utils import curdir, rand_filename

SQUARE_DRAWER = QApplication.tr("Square")
CIRCLE_DRAWER = QApplication.tr("Circle")
ROUNDED_DRAWER = QApplication.tr("Rounded")
GAPPED_DRAWER = QApplication.tr("Gapped")
VERTICAL_BARS_DRAWER = QApplication.tr("Vertical Bars")
HORIZONTAL_BARS_DRAWER = QApplication.tr("Horizontal Bars")

MODULE_DRAWERS = {
    SQUARE_DRAWER: (SquareModuleDrawer, SvgPathSquareDrawer),
    CIRCLE_DRAWER: (CircleModuleDrawer, SvgPathCircleDrawer),
    ROUNDED_DRAWER: RoundedModuleDrawer,
    GAPPED_DRAWER: GappedSquareModuleDrawer,
    VERTICAL_BARS_DRAWER: VerticalBarsDrawer,
    HORIZONTAL_BARS_DRAWER: HorizontalBarsDrawer,
}
PNG_DRAWER_IDX = 0
SVG_DRAWER_IDX = 1
MODULE_DRAWERS_SUPPORT_SIZE_RATIO = (
    SquareModuleDrawer,
    SvgPathSquareDrawer,
    CircleModuleDrawer,
    SvgPathCircleDrawer,
    GappedSquareModuleDrawer,
)

ERR_CORRECTION_LEVELS = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H,
}

DEFAULT_IMG_EXT = ".png"
DEFAULT_OUTPUT_DIR = curdir()
DEFAULT_OUTPUT_FILENAME = rand_filename(prefix="qrcode_", ext=DEFAULT_IMG_EXT)
DEFAULT_VERSION = None
DEFAULT_ERROR_CORRECTION = "M"
DEFAULT_BG_COLOR = Color.from_color_name("white")
DEFAULT_FILL_COLOR = Color.from_color_name("black")
DEFAULT_BOX_SIZE = 8
DEFAULT_BORDER = 2

DEFAULT_SIZE_RATIO = 1.0
DEFAULT_MODULE_DRAWER = None
DEFAULT_COLOR_MASK = None
DEFAULT_SVG_FACTORY = SvgPathImage

OVERWRITE_BEHAVIOR_ASK = QApplication.tr("询问")
OVERWRITE_BEHAVIOR_NOT_OVERWRITE = QApplication.tr("不覆盖")
OVERWRITE_BEHAVIOR_OVERWRITE = QApplication.tr("覆盖")
OVERWRITE_BEHAVIORS = (
    OVERWRITE_BEHAVIOR_ASK,
    OVERWRITE_BEHAVIOR_NOT_OVERWRITE,
    OVERWRITE_BEHAVIOR_OVERWRITE,
)
DEFAULT_OVERWRITE_BEHAVIOR = OVERWRITE_BEHAVIORS[0]

COLOR_MASK_SOLID_FILL = QApplication.tr("")
COLOR_MASKS = {}

MAKE_QRCODE_CONFIGS = {
    "output_dir": {
        "widget_class": DirPathEdit.__name__,
        "default": DEFAULT_OUTPUT_DIR,
        "label": QApplication.tr("保存路径"),
        "start_path": "./",
        "button_text": QApplication.tr("选择"),
    },
    "output_filename": {
        "default": DEFAULT_OUTPUT_FILENAME,
        "label": QApplication.tr("输出文件名"),
    },
    "data": {
        "widget_class": PlainTextEdit.__name__,
        "label": QApplication.tr("待编码数据"),
        "line_wrap_mode": True,
    },
    "optimize": {
        "widget_class": Slider.__name__,
        "label": QApplication.tr("优化级别"),
        "default": None,
        "min_value": 0,
        "max_value": 100,
        "step": 1,
        "tick_position": "Above",
        "tick_interval": 2,
        "tracking": True,
        "show_value_label": True,
        "value_prefix": QApplication.tr("当前级别："),
        "default_value_description": QApplication.tr("使用默认配置"),
    },
    "overwrite_behavior": {
        "widget_class": RadioButtonGroup.__name__,
        "label": QApplication.tr("覆盖行为"),
        "items": OVERWRITE_BEHAVIORS,
        "default": DEFAULT_OVERWRITE_BEHAVIOR,
    },
    "version": {
        "widget_class": Slider.__name__,
        "default": DEFAULT_VERSION,
        "label": QApplication.tr("版本"),
        "min_value": 1,
        "max_value": 40,
        "step": 1,
        "tick_position": "Above",
        "tick_interval": 2,
        "tracking": True,
        "show_value_label": True,
        "default_value_description": QApplication.tr("使用默认值（{}）"),
    },
    "error_correction": {
        "widget_class": ComboBox.__name__,
        "label": QApplication.tr("纠错级别"),
        "default": DEFAULT_ERROR_CORRECTION,
        "items": [(k, v) for k, v in ERR_CORRECTION_LEVELS.items()],
    },
    "box_size": {
        "widget_class": IntSpinBox.__name__,
        "default": DEFAULT_BOX_SIZE,
        "label": QApplication.tr("点块尺寸（像素数）"),
        "min_value": 1,
        "max_value": 9999,
        "step": 1,
    },
    "border": {
        "widget_class": IntSpinBox.__name__,
        "default": DEFAULT_BORDER,
        "label": QApplication.tr("边框宽度"),
        "min_value": 1,
        "max_value": 99,
        "step": 1,
    },
    "fill_color": {
        "label": QApplication.tr("填充颜色"),
        "default": DEFAULT_FILL_COLOR,
        "with_alpha": False,
        "color_picker_title": QApplication.tr("选择填充颜色"),
    },
    "back_color": {
        "label": QApplication.tr("背景颜色"),
        "default": DEFAULT_BG_COLOR,
        "with_alpha": False,
        "color_picker_title": QApplication.tr("选择背景颜色"),
    },
    "module_drawer": {
        "widget_class": ComboBox.__name__,
        "label": QApplication.tr("元素形状"),
        "default": None,
        "items": list(MODULE_DRAWERS.keys()),
        "default_value_description": QApplication.tr("使用默认配置"),
    },
    "size_ratio": {
        "widget_class": FloatSpinBox.__name__,
        "label": QApplication.tr("大小比例"),
        "default": DEFAULT_SIZE_RATIO,
        "hide_default_value_widget": False,
        "decimals": 5,
        "step": 0.00001,
        "min_value": 0.00001,
        "max_value": 1.00000,
        "default_value_description": QApplication.tr("使用默认值({})"),
    },
    "color_mask": {
        "label": QApplication.tr("颜色遮罩"),
        "default": None,
        "default_value_description": QApplication.tr("不使用颜色遮罩"),
    },
    "color_mask_args": {
        "label": QApplication.tr("颜色遮罩参数"),
        "default": None,
        "default_value_description": QApplication.tr("不使用颜色遮罩"),
    },
    "embeded_image_path": {
        "widget_class": FilePathEdit.__name__,
        "label": QApplication.tr("内嵌图片路径"),
        "default": None,
        "filters": "PNG文件(*.png)",
        "button_text": QApplication.tr("选择文件"),
        "default_value_description": QApplication.tr("不使用内嵌图片"),
    },
    "display_qrcode_img": {
        "label": QApplication.tr("展示结果"),
        "default": True,
        "text": "是否展示生成的二维码图片？",
    },
}

DOCUMENT = """"""