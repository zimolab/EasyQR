from PyQt6.QtWidgets import QApplication

TR_FUNC_NAME = QApplication.tr("条形码生成器")

TR_LABEL_BARCODE_TYPE = QApplication.tr("条码类型")
TR_LABEL_BARCODE_EXTRA_ARGS = QApplication.tr("额外参数")
TR_LABEL_MODULE_WIDTH = QApplication.tr("条块宽度")
TR_LABEL_MODULE_HEIGHT = QApplication.tr("条块高度")
TR_LABEL_QUIET_ZONE = QApplication.tr("左右边距")
TR_LABEL_FONT_PATH = QApplication.tr("字体路径")
TR_LABEL_FONT_SIZE = QApplication.tr("字体大小")
TR_LABEL_TEXT_DISTANCE = QApplication.tr("文字与条码距离")
TR_LABEL_BACKGROUND = QApplication.tr("背景颜色")
TR_LABEL_FOREGROUND = QApplication.tr("前景颜色")
TR_LABEL_CENTER_TEXT = QApplication.tr("文字居中")

TR_DESC_BARCODE_TYPE = QApplication.tr(
    "选择要生成的条码类型，不同的条码支持的数据容量大小及参数均有所区别，具体参见对应条码类型规范"
)
TR_DESC_BARCODE_EXTRA_ARGS = QApplication.tr(
    "输入条码类型对应的额外参数，不同类型的条码可以有不同的参数，比如Code39条码接受add_checksum参数，UPC-A接受make_ean参数等等,"
    "不同条码类型接受的额外的参数及其含义参见：<a href='https://python-barcode.readthedocs.io/en/stable/supported-formats.html'>"
    "python-barcode supported-formats</a>"
)
TR_DESC_MODULE_WIDTH = QApplication.tr("条码中每个条块所占的宽度（单位mm）")
TR_DESC_MODULE_HEIGHT = QApplication.tr("条码中每个条块所占的高度（单位mm）")
TR_DESC_QUIET_ZONE = QApplication.tr("条码距离左右的边距（单位mm）")
TR_DESC_FONT_PATH = QApplication.tr("文字字体路径")
TR_DESC_FONT_SIZE = QApplication.tr("文字字体大小（单位pt）")
TR_DESC_TEXT_DISTANCE = QApplication.tr("文字与条码距离（单位mm）")
TR_DESC_BACKGROUND = QApplication.tr("背景颜色")
TR_DESC_FOREGROUND = QApplication.tr("前景（文字）颜色")
TR_DESC_CENTER_TEXT = QApplication.tr("文字是否居中")

TR_DEF_DESC_FONT_PATH = QApplication.tr("使用默认字体")
TR_DEF_DESC_EXTRA_ARGS = QApplication.tr("无额外参数")

TR_ERR_EMPTY_BARCODE_TYPE = QApplication.tr("条码类型不可为空，请选择条码类型！")
TR_ERR_EMPTY_FONT_PATH = QApplication.tr("字体文件路径不可为空，请选择字体文件！")
TR_ERR_FONT_NOT_FOUND = QApplication.tr("未找到字体文件：{}！")

TR_WIN_TITLE_EXTRA_ARGS = QApplication.tr("编辑条码额外参数")
TR_DIALOG_TITLE_FONT_PATH = QApplication.tr("选择字体文件")

TR_BTN_TEXT_EXTRA_ARGS = QApplication.tr("查看/编辑")
TR_BTN_TEXT_FONT_PATH = QApplication.tr("选择字体文件")

TR_FILTERS_FONT_FILE = QApplication.tr("字体文件(*.ttf);;字体文件(*.otf);;字体文件(*.ttc);;字体文件(*.otf);;所有文件(*.*)")