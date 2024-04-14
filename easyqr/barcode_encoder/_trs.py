from PyQt6.QtWidgets import QApplication

TR_FUNC_NAME = QApplication.tr("条形码生成器")

TR_LABEL_BARCODE_TYPE = QApplication.tr("条码类型")
TR_LABEL_BARCODE_EXTRA_ARGS = QApplication.tr("额外参数")


TR_DESC_BARCODE_TYPE = QApplication.tr(
    "选择要生成的条码类型，不同的条码支持的数据容量大小及参数均有所区别，具体参见对应条码类型规范"
)
TR_DESC_BARCODE_EXTRA_ARGS = QApplication.tr(
    "输入条码类型对应的额外参数，不同类型的条码可以有不同的参数，比如Code39条码接受add_checksum参数，UPC-A接受make_ean参数等等,"
    "不同条码类型接受的额外的参数及其含义参见：<a href='https://python-barcode.readthedocs.io/en/stable/supported-formats.html'>"
    "python-barcode supported-formats</a>"
)

TR_ERR_BARCODE_TYPE = QApplication.tr("请选择条码类型")
TR_BARCODE_EXTRA_ARGS_BUTTON_TEXT = QApplication.tr("查看/编辑")
TR_BARCODE_EXTRA_ARGS_DEFAULT_DESC = QApplication.tr("无额外参数")
TR_BARCODE_EXTRA_ARGS_WINDOW_TITLE = QApplication.tr("编辑条码额外参数")
