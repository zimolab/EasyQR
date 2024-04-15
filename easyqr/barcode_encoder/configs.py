from barcode import PROVIDED_BARCODES
from function2widgets.widgets import ComboBox, DictEditor, IntSpinBox, FloatSpinBox, FilePathEdit


from easyqr.common import UNIVERSAL_CONFIGS
from ._constants import *

MAKE_BARCODE_CONFIGS = {
    **UNIVERSAL_CONFIGS,
    "barcode_type": {
        "widget_class": ComboBox.__name__,
        "label": TR_LABEL_BARCODE_TYPE,
        "description": TR_DESC_BARCODE_TYPE,
        "items": PROVIDED_BARCODES,
        "default": DEFAULT_BARCODE_TYPE,
    },
    "barcode_extra_args": {
        "widget_class": DictEditor.__name__,
        "label": TR_LABEL_BARCODE_EXTRA_ARGS,
        "description": TR_DESC_BARCODE_EXTRA_ARGS,
        "default": DEFAULT_BARCODE_EXTRA_ARGS,
        "display_current_value": False,
        "button_text": TR_BTN_TEXT_EXTRA_ARGS,
        "default_value_description": TR_DEF_DESC_EXTRA_ARGS,
        "window_title": TR_WIN_TITLE_EXTRA_ARGS,
    },
    "module_width": {
        "widget_class": FloatSpinBox.__name__,
        "label": TR_LABEL_MODULE_WIDTH,
        "description": TR_DESC_MODULE_WIDTH,
        "default": DEFAULT_MODULE_WIDTH,
        "min_value": 0.10,
        "max_value": 2.00,
        "step": 0.01,
        "decimals": 2,
    },
    "module_height": {
        "widget_class": FloatSpinBox.__name__,
        "label": TR_LABEL_MODULE_HEIGHT,
        "description": TR_DESC_MODULE_HEIGHT,
        "default": DEFAULT_MODULE_HEIGHT,
        "min_value": 10.00,
        "max_value": 50.00,
        "step": 0.05,
        "decimals": 2,
    },
    "quiet_zone": {
        "widget_class": FloatSpinBox.__name__,
        "label": TR_LABEL_QUIET_ZONE,
        "description": TR_DESC_QUIET_ZONE,
        "default": DEFAULT_QUIET_ZONE,
        "min_value": 1.00,
        "max_value": 50.00,
        "step": 0.05,
        "decimals": 2,

    },
    "font_path": {
        "widget_class": FilePathEdit.__name__,
        "label": TR_LABEL_FONT_PATH,
        "description": TR_DESC_FONT_PATH,
        "default": DEFAULT_FONT_PATH,
        "button_text": TR_BTN_TEXT_FONT_PATH,
        "default_value_description": TR_DEF_DESC_FONT_PATH,
        "dialog_title": TR_DIALOG_TITLE_FONT_PATH,
        "filters": TR_FILTERS_FONT_FILE,
    },
    "font_size": {
        "widget_class": IntSpinBox.__name__,
        "label": TR_LABEL_FONT_SIZE,
        "description": TR_DESC_FONT_SIZE,
        "default": DEFAULT_FONT_SIZE,
        "min_value": 5,
        "max_value": 50,
    },
    "text_distance": {
        "widget_class": FloatSpinBox.__name__,
        "label": TR_LABEL_TEXT_DISTANCE,
        "description": TR_DESC_TEXT_DISTANCE,
        "default": DEFAULT_TEXT_DISTANCE,
        "min_value": 1.00,
        "max_value": 50.00,
        "step": 0.05,
        "decimals": 2,
    },
    "background": {
        "label": TR_LABEL_BACKGROUND,
        "description": TR_DESC_BACKGROUND,
        "default": DEFAULT_BACKGROUND,   
    },
    "foreground": {
        "label": TR_LABEL_FOREGROUND,
        "description": TR_DESC_FOREGROUND,
        "default": DEFAULT_FOREGROUND,   
    },
    "write_text": {},
    "text": {},
    "compressed": {},
}
