from function2widgets.widgets.numberinput import IntSpinBox, FloatSpinBox
from function2widgets.widgets.numberinput import Slider
from function2widgets.widgets.pathedit import FilePathEdit
from function2widgets.widgets.selectwidget import ComboBox
from pyguiadapter.commons import get_param_widget_factory

from easyqr.common import UNIVERSAL_CONFIGS
from .constants import *
from .widget import ColorsGroupWidget

# 注册自定义控件
_param_widget_factory = get_param_widget_factory()
if not _param_widget_factory.is_registered(ColorsGroupWidget.__name__):
    _param_widget_factory.register(ColorsGroupWidget.__name__, ColorsGroupWidget)


MAKE_QRCODE_CONFIGS = {
    **UNIVERSAL_CONFIGS,
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
    "background_image_path": {
        "widget_class": FilePathEdit.__name__,
        "label": QApplication.tr("背景图片路径"),
        "default": None,
        "filters": BACKGROUND_IMAGE_FILE_FILTERS,
        "button_text": QApplication.tr("选择文件"),
        "default_value_description": QApplication.tr("不使用背景图片"),
    },
    "color_mask": {
        "widget_class": ComboBox.__name__,
        "label": QApplication.tr("颜色遮罩"),
        "default": None,
        "items": {name: date for name, date in COLOR_MASKS.items()},
        "default_value_description": QApplication.tr("不使用颜色遮罩"),
    },
    "color_mask_colors": {
        "widget_class": ColorsGroupWidget.__name__,
        "label": QApplication.tr("颜色遮罩参数"),
        "default": {},
        "colors": DEFAULT_COLOR_MASK_COLORS,
        "columns": 2,
    },
    "embeded_image_path": {
        "widget_class": FilePathEdit.__name__,
        "label": QApplication.tr("内嵌图片路径"),
        "default": None,
        "filters": EMBED_IMG_FILE_FILTERS,
        "button_text": QApplication.tr("选择文件"),
        "default_value_description": QApplication.tr("不使用内嵌图片"),
    },
    "display_qrcode_img": {
        "label": QApplication.tr("展示结果"),
        "default": True,
        "text": "是否展示生成的二维码图片？",
    },
}
