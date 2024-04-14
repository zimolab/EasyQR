from barcode import PROVIDED_BARCODES
from function2widgets.widgets import ComboBox, DictEditor


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
        "button_text": TR_BARCODE_EXTRA_ARGS_BUTTON_TEXT,
        "default_value_description": TR_BARCODE_EXTRA_ARGS_DEFAULT_DESC,
        "window_title": TR_BARCODE_EXTRA_ARGS_WINDOW_TITLE,
    },
    "module_width": {
        
    },
    "module_height": {},
    "quiet_zone": {},
    "font_size": {},
    "text_distance": {},
    "background": {},
    "foreground": {},
    "write_text": {},
    "text": {},
    "compressed": {},
}
