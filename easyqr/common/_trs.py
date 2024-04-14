from PyQt6.QtWidgets import QApplication

TR_LABEL_OUTPUT_DIR = QApplication.tr("目标文件夹")
TR_LABEL_MAKE_DIRS = QApplication.tr("创建文件夹")
TR_LABEL_OUTPUT_FILENAME = QApplication.tr("生成文件名")
TR_LABEL_DATA = QApplication.tr("待编码数据")
TR_LABEL_OVERWRITE_BEHAVIOR = QApplication.tr("覆盖行为")
TR_LABEL_VERBOSE = QApplication.tr("详细模式")
TR_LABEL_SHOW_RESULT_IMG = QApplication.tr("显示结果图片")

TR_OVERWRITE_ASK = QApplication.tr("询问")
TR_OVERWRITE_NOT_OVERWRITE = QApplication.tr("不覆盖")
TR_OVERWRITE_OVERWRITE = QApplication.tr("覆盖")

TR_DESC_OUTPUT_DIR = QApplication.tr("生成文件保存的默认，如果置空，则使用当前工作目录")
TR_DESC_MAKE_DIRS = QApplication.tr("目标文件夹不存在时是否自动创建文件夹")
TR_DESC_OUTPUT_FILENAME = QApplication.tr(
    "生成文件名称，支持生成SVG或PNG格式文件，请以.svg或.png作为文件名后缀"
)
TR_DESC_OVERWRITE_BEHAVIOR = QApplication.tr("文件已存在时的行为")
TR_DESC_DATA = QApplication.tr(
    "待编码数据的长度需符合相应限制条件，否则可能造成编码失败"
)
TR_DESC_VERBOSE = QApplication.tr("是否打印详细日志")
TR_DESC_SHOW_RESULT_IMG = QApplication.tr(
    "是否在输出区显示生成的结果图片用以快速预览。<br><br>"
    "<b>注意：</b> 输出区域显示的图片仅作参考，对于某些svg文件，可能会出现显示异常的情况，"
    "生成图片的具体效果请使用图片查看软件打开生文件进行查看！<br>"
)

TR_SELECT_BUTTON_TEXT = QApplication.tr("选择")
TR_MAKE_DIRS_TEXT = QApplication.tr("自动创建文件夹")
TR_VERBOSE_TEXT = QApplication.tr("启用详细模式")
TR_SHOW_RESULT_IMG_TEXT = QApplication.tr("是否显示结果图片")


TR_ERR_INVALID_OVERWRITE_BEHAVIOR = QApplication.tr("无效的覆盖行为！({})")
TR_ERR_OUTPUT_DIR_NOT_EXIST = QApplication.tr("目标文件夹不存在！（{}）")
TR_ERR_EMPTY_OUTPUT_FILENAME = QApplication.tr("生成文件名不能为空！")
TR_ERR_INVALID_OUTPUT_FILENAME = QApplication.tr(
    "只支持生成SVG或PNG格式文件，文件名必须以.svg或.png作为后缀！"
)
TR_ERR_EMPTY_DATA = QApplication.tr("待编码数据不能为空！")
TR_ERR_OVERWRITE_NOT_ALLOWED = QApplication.tr("目标文件已存在，且不允许覆盖！")

TR_MSG_MKDIRS = QApplication.tr("创建文件夹: {}")
TR_MSG_WILL_BE_OVERWRITTEN = QApplication.tr("目标文件已存在，将覆盖该文件")
TR_MSG_ASK_FOR_OVERWRITE = QApplication.tr("目标文件已存在，是否该覆盖？")
