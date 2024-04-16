import inspect
import os.path
from decimal import Decimal
from typing import Optional, Type, Union, Dict, List

import qrcode
from PyQt6.QtWidgets import QApplication
from function2widgets.widgets.misc import Color
from pyguiadapter.interact import ulogging as logging
from pyguiadapter.interact import upopup
from pyguiadapter.interact.uprint import uprint
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask, QRColorMask
from qrcode.image.styles.moduledrawers.base import QRModuleDrawer

from easyqr.utils import curdir
from easyqr.common import OverwriteBehavior, get_overwrite_behavior
from .constants import (
    ERR_CORRECTION_LEVELS,
    MODULE_DRAWERS,
    SQUARE_DRAWER,
    CIRCLE_DRAWER,
    SVG_DRAWER_IDX,
    PNG_DRAWER_IDX,
    DEFAULT_SIZE_RATIO,
    DEFAULT_SVG_FACTORY,
    MODULE_DRAWERS_SUPPORT_SIZE_RATIO,
    COLOR_MASKS,
    COLOR_MASK_REQUIRED_COLOR_LABELS,
)


def make_qrcode(
    output_dir: str,
    output_filename: str,
    data: str,
    overwrite_behavior: str,
    optimize: int,
    version: int,
    error_correction: str,
    box_size: int,
    border: int,
    fill_color: Color,
    back_color: Color,
    module_drawer: str,
    size_ratio: float,
    background_image_path: str,
    color_mask: Type[QRColorMask],
    color_mask_colors: dict,
    embeded_image_path: str,
    display_qrcode_img: bool,
):
    """
    为指定文本数据生成二维码图像，并保存到本地文件。可通过多个参数控制二维码生成结果。
    <br>
    <br>
    二维码生成基于<b>python-qrcode</b>，
    请参考：<a href='https://github.com/lincolnloop/python-qrcode'>python-qrcode官方文档</a>，获取详细信息以及各参数作用与取值。
    <br>
    <br>
    Note: 经过测试，在生成SVG格式的图片时，填充色和背景色设置可能无法生效。

    :param output_dir: 输出文件目录，若为空，则将当前工作目录作为输出文件目录
    :param output_filename: 输出文件名称，必须是.png文件或.svg文件
    :param data: 要编码的文本数据（请注意数据长度，数据太长可能会造成编码失败）
    :param overwrite_behavior: 当指定位置下存在同名文件时，是否进行覆盖
    :param optimize: 优化级别
    :param version: 该参数控制生成二维码的尺寸，从1到40，如果设置为None，则在生成图片时自动判断
    :param error_correction: 纠错级别，级别越高，纠错能力越强，但载荷容量越小
    :param box_size: 点块尺寸，即指定每个二维码每个点块在最终图像上的像素大小，即每个点块渲染成多少个像素
    :param border: 边框宽度，即二维码四周的空白边框宽度，边框有助于扫描设备更容易识别二维码
    :param fill_color: 填充颜色，默认为黑色
    :param back_color: 背景颜色，默认为白色
    :param module_drawer: 控制生成二维码内点块元素的形状
    :param size_ratio: 该参数仅在手动指定元素形状后生效，且仅对特定几种形状（Square、GappedSquare、Circle）有效
    :param background_image_path: 背景图片，若指定了该参数，则<b>颜色遮罩参数</b>不会生效
    :param color_mask: 颜色遮罩模式，当指定了背景图片时，该参数不生效
    :param color_mask_colors: 遮罩颜色，不同的遮罩模式所需颜色不同，仅在启用颜色颜色遮罩模式时生效，且当选择了背景图片时，该参数不生效
    :param embeded_image_path: 内嵌图片（logo）路径（当输出文件为svg格式，嵌入图片可能无法生效）
    :param display_qrcode_img: 展示生成的二维码图片
    :return:
    """
    logging.enable_timestamp(True)
    logging.info(QApplication.tr("开始生成二维码..."))

    # 第一阶段，尽可能完成参数校验，及早抛出异常
    # 检查输出目录合法性
    if not output_dir:
        output_dir = curdir()
        logging.warning(
            QApplication.tr(
                "未指定输出目录，将使用当前工作目录作为输出目录，当前工作目录：{}".format(
                    output_dir
                )
            )
        )

    # 检查输出文件名合法性
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

    # 生成.svg格式时存在一些约束条件
    output_svg = output_filename.endswith(".svg")
    if output_svg and embeded_image_path:
        raise ValueError(QApplication.tr("生成.svg文件模式下不支持内嵌图片！"))
    if output_svg and background_image_path:
        raise ValueError(QApplication.tr("生成.svg文件模式下不支持背景图片！"))
    if output_svg and color_mask:
        raise ValueError(QApplication.tr("生成.svg文件模式下不支持颜色遮罩！"))

    # 获取输出文件最终路径
    output_filepath = os.path.abspath(os.path.join(output_dir, output_filename))
    logging.info(QApplication.tr("输出图片文件路径：{}".format(output_filepath)))
    # 在目标文件路径存在文件时，根据用户设置进行覆盖或取消操作
    if os.path.isfile(output_filepath):
        quit_msg = QApplication.tr("目标文件已存在，取消生成！")
        will_be_overwrite_msg = QApplication.tr("{}将被覆盖!".format(output_filepath))
        behavior = get_overwrite_behavior(overwrite_behavior)
        if behavior == OverwriteBehavior.Ask:
            if not _ask_if_overwrite(output_filepath):
                logging.warning(quit_msg)
                return
            else:
                logging.warning(will_be_overwrite_msg)
        elif behavior == OverwriteBehavior.Overwrite:
            logging.warning(will_be_overwrite_msg)
        else:
            logging.warning(quit_msg)
            upopup.warning(quit_msg)
            return
    # 检查待编码的数据是否为空，不允许对空数据进行编码
    if not data:
        raise ValueError(QApplication.tr("待编码数据为空，请输入要编码的数据！"))

    if optimize is None:
        optimize = 0
        logging.info(QApplication.tr("使用默认优化级别"))
    else:
        logging.info(QApplication.tr("当前优化级别为：{}".format(optimize)))
    # 根据version参数决定使用使用fit参数
    if version is None:
        logging.info(QApplication.tr("未指定版本，将自动选择最佳尺寸"))
        fit = True
    else:
        fit = False
    # 检查纠错级别，当其为字符串时，将其转换为对应的值
    if isinstance(error_correction, str):
        error_correction = ERR_CORRECTION_LEVELS.get(error_correction, None)
        if error_correction is None:
            raise ValueError(
                QApplication.tr(
                    "未知纠错级别{}，请重新指定纠错级别！".format(error_correction)
                )
            )
    logging.info(QApplication.tr("当前纠错级别为：{}".format(error_correction)))

    # 检查填充颜色，当其为字符串时，将其转换为对应的值
    if isinstance(fill_color, str):
        fill_color = Color.from_string(fill_color)
    logging.info(
        QApplication.tr(
            "当前填充颜色为：{}".format(fill_color.to_hex_string(with_alpha=False))
        )
    )
    # 检查背景颜色，当其为字符串时，将其转换为对应的值
    if isinstance(back_color, str):
        back_color = Color.from_string(back_color)
    logging.info(
        QApplication.tr(
            "当前背景颜色为：{}".format(back_color.to_hex_string(with_alpha=False))
        )
    )
    # 检查内嵌图片文件，如果指定了，则检查文件是否存在，不存在则抛出异常
    if embeded_image_path is not None and not os.path.isfile(embeded_image_path):
        raise ValueError(
            QApplication.tr(
                "指定的内嵌图片文件{}不存在，请重新选择！".format(embeded_image_path)
            )
        )

    # 检查背景图片路径，如果指定了，则检查文件是否存在，不存在则抛出异常
    if background_image_path is not None and not os.path.isfile(background_image_path):
        raise ValueError(
            QApplication.tr(
                "指定的背景图片文件{}不存在，请重新选择！".format(background_image_path)
            )
        )

    image_factory = _get_img_factory(output_svg)
    module_drawer_class = _get_module_drawer_class(output_svg, module_drawer)
    module_drawer_instance = _create_module_drawer_instance(
        module_drawer_class, size_ratio
    )
    if background_image_path:
        color_mask_instance = _create_img_color_mask(
            back_color=back_color, background_image_path=background_image_path
        )
    elif isinstance(color_mask, QRColorMask):
        color_mask_instance = color_mask
    elif inspect.isclass(color_mask) and issubclass(color_mask, QRColorMask):
        color_mask_instance = _create_color_mask_instance(color_mask, color_mask_colors)
    elif isinstance(color_mask, str):
        color_mask_instance = _create_color_mask_instance(color_mask, color_mask_colors)
    elif color_mask is None:
        color_mask_instance = None
    else:
        raise ValueError(QApplication.tr(f"无效的颜色遮罩类型：{type(color_mask)}"))

    # 第二阶段生成二维码图片
    qr_obj = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr_obj.add_data(data, optimize=optimize)
    qr_obj.make(fit=fit)
    if color_mask_instance is not None:
        img = qr_obj.make_image(
            fill_color=fill_color.to_hex_string(with_alpha=False),
            back_color=back_color.to_hex_string(with_alpha=False),
            image_factory=image_factory,
            module_drawer=module_drawer_instance,
            embeded_image_path=embeded_image_path,
            color_mask=color_mask_instance,
        )
    else:
        img = qr_obj.make_image(
            fill_color=fill_color.to_hex_string(with_alpha=False),
            back_color=back_color.to_hex_string(with_alpha=False),
            image_factory=image_factory,
            module_drawer=module_drawer_instance,
        )
    # 第三阶段保存生成的图片
    img.save(output_filepath)
    logging.info("二维码生成成功！")
    if display_qrcode_img:
        _print_img(output_filepath)


def _ask_if_overwrite(file_path: str) -> bool:
    msg = QApplication.tr("文件{}已存在，是否覆盖？".format(file_path))
    return upopup.question(msg, title=QApplication.tr("是否覆盖文件？"))


def _print_img(img_path: str):
    img_ele = f'<img src="{img_path}" />'
    uprint()
    uprint(img_ele, html=True)
    uprint()


def _get_img_factory(output_svg: bool) -> Type[StyledPilImage]:
    if output_svg:
        return DEFAULT_SVG_FACTORY
    return StyledPilImage


def _get_module_drawer_class(
    output_svg: bool, module_drawer: Optional[str]
) -> Optional[Type[QRModuleDrawer]]:
    if not module_drawer:
        return None
    if output_svg and module_drawer not in (CIRCLE_DRAWER, SQUARE_DRAWER):
        raise ValueError(
            QApplication.tr(
                "当输出文件为svg格式时，点块形状只能支持{}或{}，请重新指定！".format(
                    CIRCLE_DRAWER, SQUARE_DRAWER
                )
            )
        )

    try:
        module_drawer_classes = MODULE_DRAWERS.get(module_drawer)
    except KeyError:
        raise ValueError(
            QApplication.tr("未知的点块形状{}，请重新指定！".format(module_drawer))
        )
    if not isinstance(module_drawer_classes, tuple):
        return module_drawer_classes
    idx = PNG_DRAWER_IDX
    if output_svg:
        idx = SVG_DRAWER_IDX
    return module_drawer_classes[idx]


def _create_module_drawer_instance(
    clazz: Type[QRModuleDrawer], size_ratio: float
) -> Optional[QRModuleDrawer]:
    if clazz is None:
        return None
    # 创建点块形状绘制器实例
    if size_ratio is None or size_ratio <= 0:
        size_ratio = DEFAULT_SIZE_RATIO
    size_ratio = Decimal(size_ratio)
    support_size_ration = clazz in MODULE_DRAWERS_SUPPORT_SIZE_RATIO
    if support_size_ration:
        return clazz(size_ratio=size_ratio)
    return clazz()


def _get_required_colors(
    color_mask_class: Type[QRColorMask], color_mask_colors: Dict[str, Color]
) -> List:
    if color_mask_class is None:
        raise ValueError(QApplication.tr(f"未指定颜色遮罩类型！"))
    required_color_labels = COLOR_MASK_REQUIRED_COLOR_LABELS.get(color_mask_class, None)
    if not required_color_labels:
        raise ValueError(
            QApplication.tr(f"无法获取颜色遮罩类型'{color_mask_class}'的必要颜色")
        )
    return [
        color_mask_colors.get(color_label).to_rgb_tuple(with_alpha=False)
        for color_label in required_color_labels
    ]


def _create_color_mask_instance(
    color_mask: Union[Type[QRColorMask], str], color_mask_colors: Dict[str, Color]
) -> Optional[QRColorMask]:
    if not color_mask:
        return None
    color_mask_class = color_mask
    if isinstance(color_mask, str):
        color_mask_class = COLOR_MASKS.get(color_mask, None)
        if not color_mask_class:
            raise ValueError(
                QApplication.tr("未知的颜色遮罩类型：{}".format(color_mask))
            )
    init_args = _get_required_colors(color_mask_class, color_mask_colors)
    return color_mask_class(*init_args)


def _create_img_color_mask(
    background_image_path: str, back_color: Color
) -> ImageColorMask:
    return ImageColorMask(
        back_color=back_color.to_rgb_tuple(with_alpha=False),
        color_mask_path=background_image_path,
    )
