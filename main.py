from PyQt6.QtWidgets import QApplication
from pyguiadapter.adapter import GUIAdapter
from pyguiadapter.commons import DocumentFormat

from easyqr import make_qrcode, MAKE_QRCODE_CONFIGS

APP_NAME = "Easy QR Code"
VERSION = "0.1.0"
AUTHOR = "zimolab"


def set_window_configs(adapter: GUIAdapter):
    adapter.selection_window_config.title = APP_NAME
    adapter.execution_window_config.title = APP_NAME
    adapter.execution_window_config.show_func_result_dialog = False
    adapter.execution_window_config.print_func_result = False
    adapter.execution_window_config.print_func_start_msg = False
    adapter.execution_window_config.print_func_finish_msg = False
    adapter.execution_window_config.func_error_msg = "{}"
    adapter.execution_window_config.func_error_dialog_msg = "{}"
    adapter.execution_window_config.timestamp = True
    adapter.execution_window_config.execute_button_text = QApplication.tr("生成")
    adapter.execution_window_config.autoclear_checkbox_text = QApplication.tr(
        "自动清除上次输出"
    )
    adapter.execution_window_config.func_error_dialog_title = QApplication.tr("错误")
    adapter.execution_window_config.param_groupbox_title = QApplication.tr("参数")
    adapter.execution_window_config.clear_button_text = QApplication.tr("清除输出")
    adapter.execution_window_config.document_dock_config.title = QApplication.tr("文档")
    adapter.execution_window_config.output_dock_config.title = QApplication.tr("输出")


def add_functions(adapter: GUIAdapter):
    adapter.add(
        make_qrcode,
        document_format=DocumentFormat.MARKDOWN,
        widget_configs=MAKE_QRCODE_CONFIGS,
    )


def main():
    gui_adapter = GUIAdapter()
    set_window_configs(adapter=gui_adapter)
    add_functions(adapter=gui_adapter)
    gui_adapter.run()


if __name__ == "__main__":
    main()
