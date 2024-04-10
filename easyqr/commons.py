from PyQt6.QtWidgets import QApplication
from function2widgets.widgets import DirPathEdit, PlainTextEdit


from .utils import curdir, rand_filename

DEFAULT_IMG_EXT = ".png"
DEFAULT_OUTPUT_DIR = curdir()
DEFAULT_OUTPUT_FILENAME = rand_filename(prefix="code_", ext=DEFAULT_IMG_EXT)


UNIVERSAL_CONFIGS = {
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
}
