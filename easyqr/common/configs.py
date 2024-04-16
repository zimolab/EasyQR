from function2widgets.widgets import (
    DirPathEdit,
    PlainTextEdit,
    RadioButtonGroup,
    CheckBox,
)

from ._constants import *

UNIVERSAL_CONFIGS = {
    "output_dir": {
        "widget_class": DirPathEdit.__name__,
        "default": DEFAULT_OUTPUT_DIR,
        "label": TR_LABEL_OUTPUT_DIR,
        "description": TR_DESC_OUTPUT_DIR,
        "start_path": DEFAULT_START_PATH,
        "button_text": TR_BTN_TEXT_SELECT_DIR,
    },
    "make_dirs": {
        "widget_class": CheckBox.__name__,
        "label": TR_LABEL_MAKE_DIRS,
        "description": TR_DESC_MAKE_DIRS,
        "text": TR_CHECKBOX_TEXT_MAKE_DIRS,
        "default": True,
    },
    "output_filename": {
        "default": DEFAULT_OUTPUT_FILENAME,
        "description": TR_DESC_OUTPUT_FILENAME,
        "label": TR_LABEL_OUTPUT_FILENAME,
    },
    "data": {
        "widget_class": PlainTextEdit.__name__,
        "label": TR_LABEL_DATA,
        "description": TR_DESC_DATA,
        "line_wrap_mode": True,
    },
    "overwrite_behavior": {
        "widget_class": RadioButtonGroup.__name__,
        "label": TR_LABEL_OVERWRITE_BEHAVIOR,
        "description": TR_DESC_OVERWRITE_BEHAVIOR,
        "items": OVERWRITE_BEHAVIORS,
        "default": DEFAULT_OVERWRITE_BEHAVIOR,
    },
    "verbose": {
        "widget_class": CheckBox.__name__,
        "label": TR_LABEL_VERBOSE,
        "description": TR_DESC_VERBOSE,
        "default": True,
        "text": TR_CHECKBOX_TEXT_VERBOSE,
    },
    "show_result_img": {
        "widget_class": CheckBox.__name__,
        "label": TR_LABEL_SHOW_RESULT_IMG,
        "description": TR_DESC_SHOW_RESULT_IMG,
        "default": True,
        "text": TR_CHECKBOX_TEXT_SHOW_RESULT_IMG,
    },
}
