from PyQt6.QtWidgets import QApplication
from pyguiadapter import DocumentFormat, GUIAdapter

from easyqr.qrcode_encoder import FUNC_NAME as MAKE_QRCODE_FUNC_NAME
from easyqr.qrcode_encoder import MAKE_QRCODE_CONFIGS, make_qrcode
from easyqr.barcode_encoder import FUNC_NAME as MAKE_BARCODE_FUNC_NAME
from easyqr.barcode_encoder import MAKE_BARCODE_CONFIGS, make_barcode

APP_NAME = "Easy QR Code"
VERSION = "0.1.0"
AUTHOR = "zimolab"


def set_window_configs(adapter: GUIAdapter):
    # 设置Selection Window
    adapter.selection_window_config.title = APP_NAME
    adapter.selection_window_config.icon_mode = False
    adapter.selection_window_config.func_list_label_text = QApplication.tr("功能列表")
    adapter.selection_window_config.document_label_text = QApplication.tr("说明文档")
    adapter.selection_window_config.select_button_text = QApplication.tr("选择功能")
    # 设置 Execution Window
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
        widget_configs=MAKE_QRCODE_CONFIGS,
        display_name=MAKE_QRCODE_FUNC_NAME,
        document_format=DocumentFormat.HTML,
    )
    adapter.add(
        make_barcode,
        display_name=MAKE_BARCODE_FUNC_NAME,
        widget_configs=MAKE_BARCODE_CONFIGS,
        document_format=DocumentFormat.HTML,
    )


def main():
    gui_adapter = GUIAdapter()
    set_window_configs(adapter=gui_adapter)
    add_functions(adapter=gui_adapter)
    gui_adapter.run()


if __name__ == "__main__":
    main()
