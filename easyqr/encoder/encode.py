import os.path

from PyQt6.QtWidgets import QApplication
from function2widgets.widgets.misc import Color
from pyguiadapter.interact import ulogging as logging
from pyguiadapter.interact import upopup
from pyguiadapter.interact.uprint import uprint
from qrcode.image.svg import SvgPathImage
import qrcode

from easyqr.utils import curdir
from .configs import (
    OVERWRITE_BEHAVIOR_ASK,
    OVERWRITE_BEHAVIOR_OVERWRITE,
    ERR_CORRECTION_LEVELS,
)


def make_qrcode(
    output_dir: str,
    output_filename: str,
    overwrite_behavior: str,
    data: str,
    optimize: int,
    version: int,
    error_correction: str,
    box_size: int,
    border: int,
    fill_color: Color,
    back_color: Color,
    module_drawer: str,
    size_ratio: float,
    color_mask: str,
    color_mask_args: dict,
    embeded_image_path: str,
    display_qrcode_img: bool,
):
    """
    为制定文本数据生成二维码图像，并保存到本地文件。可通过多个参数控制二维码生成结果。


    二维码生成基于**python-qrcode**，请参考：
    [https://github.com/lincolnloop/python-qrcode](https://github.com/lincolnloop/python-qrcode)
    获取该库详细信息以及各参数作用及取值。

    :param output_dir: 输出文件目录，若为空，则将当前工作目录作为输出文件目录
    :param output_filename: 输出文件名称，必须是.png文件或.svg文件
    :param overwrite_behavior: 当指定位置下存在同名文件时，是否进行覆盖
    :param data: 要编码的文本数据（请注意数据长度，数据太长可能会造成编码失败）
    :param optimize: 优化级别
    :param version: 该参数控制生成二维码的尺寸，从1到40，如果设置为None，则在生成图片时自动判断
    :param error_correction: 纠错级别，级别越高，纠错能力越强，但载荷容量越小
    :param box_size: 点块尺寸，即指定每个二维码每个点块在最终图像上的像素大小，即每个点块渲染成多少个像素
    :param border: 边框宽度，即二维码四周的空白边框宽度，边框有助于扫描设备更容易识别二维码
    :param fill_color: 填充颜色，默认为黑色
    :param back_color: 背景颜色，默认为白色
    :param module_drawer: 控制生成二维码内点块元素的形状
    :param size_ratio: 该参数仅在手动指定元素形状后生效
    :param color_mask:
    :param color_mask_args:
    :param embeded_image_path: 内嵌图片（logo）路径
    :param display_qrcode_img: 展示生成的二维码图片
    :return:
    """
    logging.enable_timestamp(True)
    # 第一阶段，尽可能完成参数校验，及早抛出异常
    logging.info(QApplication.tr("开始生成二维码..."))
    if not output_dir:
        output_dir = curdir()
        logging.warning(
            QApplication.tr(
                "未指定输出目录，将使用当前工作目录作为输出目录，当前工作目录：{}".format(
                    output_dir
                )
            )
        )
    if isinstance(output_filename, str):
        output_filename = output_filename.strip()
    if not output_filename:
        raise ValueError(QApplication.tr("输出文件名为空，请指定输出文件名！"))

    if not output_filename.endswith(".png") and not output_filename.endswith(".svg"):
        raise ValueError(
            QApplication.tr(
                "目前仅支持生成png、svg格式图片，输出文件名必须以.png或.svg结尾，请重新指定！"
            )
        )

    output_filepath = os.path.abspath(os.path.join(output_dir, output_filename))
    logging.info(QApplication.tr("输出图片文件路径：{}".format(output_filepath)))
    if os.path.isfile(output_filepath):
        quit_msg = QApplication.tr("目标文件已存在，取消生成！")
        will_be_overwrite_msg = QApplication.tr("{}将被覆盖!".format(output_filepath))
        if overwrite_behavior == OVERWRITE_BEHAVIOR_ASK:
            if not _ask_if_overwrite(output_filepath):
                logging.warning(quit_msg)
                return
            else:
                logging.warning(will_be_overwrite_msg)
        elif overwrite_behavior == OVERWRITE_BEHAVIOR_OVERWRITE:
            logging.warning(will_be_overwrite_msg)
        else:
            logging.warning(quit_msg)
            upopup.warning(quit_msg)
            return

    if not data:
        raise ValueError(QApplication.tr("待编码数据为空，请输入要编码的数据！"))

    if optimize is None:
        optimize = 0
        logging.info(QApplication.tr("使用默认优化级别"))
    else:
        logging.info(QApplication.tr("当前优化级别为：{}".format(optimize)))

    if version is None:
        logging.info(QApplication.tr("未指定版本，将自动选择最佳尺寸"))
        fit = True
    else:
        fit = False

    if isinstance(error_correction, str):
        error_correction = ERR_CORRECTION_LEVELS.get(error_correction, None)
        if error_correction is None:
            raise ValueError(
                QApplication.tr(
                    "未知纠错级别{}，请重新指定纠错级别！".format(error_correction)
                )
            )
    logging.info(QApplication.tr("当前纠错级别为：{}".format(error_correction)))
    if isinstance(fill_color, str):
        fill_color = Color.from_string(fill_color)
    logging.info(
        QApplication.tr(
            "当前填充颜色为：{}".format(fill_color.to_hex_string(with_alpha=False))
        )
    )
    if isinstance(back_color, str):
        back_color = Color.from_string(back_color)
    logging.info(
        QApplication.tr(
            "当前背景颜色为：{}".format(back_color.to_hex_string(with_alpha=False))
        )
    )

    if embeded_image_path is not None and not os.path.isfile(embeded_image_path):
        raise ValueError(
            QApplication.tr(
                "指定的内嵌图片文件{}不存在，请重新选择！".format(embeded_image_path)
            )
        )

    # 开始生成二维码
    svg_format = output_filename.endswith(".svg")
    if svg_format:
        image_factory = SvgPathImage
    else:
        image_factory = None

    qr_obj = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr_obj.add_data(data, optimize=optimize)
    qr_obj.make(fit=fit)
    img = qr_obj.make_image(
        fill_color=fill_color.to_hex_string(with_alpha=False),
        back_color=back_color.to_hex_string(with_alpha=False),
        image_factory=image_factory,
    )
    img.save(output_filepath)
    logging.info("二维码生成成功！")
    if display_qrcode_img:
        _send_qrcode_to_output(output_filepath)


def _embed_image():
    pass


def _ask_if_overwrite(file_path: str) -> bool:
    msg = QApplication.tr("文件{}已存在，是否覆盖？".format(file_path))
    return upopup.question(msg, title=QApplication.tr("是否覆盖文件？"))


def _send_qrcode_to_output(img_path: str):
    img_ele = f'<img src="{img_path}" />'
    uprint()
    uprint(img_ele, html=True)
    uprint()
