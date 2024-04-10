from PyQt6.QtWidgets import QApplication
from qrcode.image.svg import SvgPathImage
from qrcode.constants import (
    ERROR_CORRECT_L,
    ERROR_CORRECT_M,
    ERROR_CORRECT_Q,
    ERROR_CORRECT_H,
)
from qrcode.image.styles.moduledrawers.pil import (
    SquareModuleDrawer,
    GappedSquareModuleDrawer,
    CircleModuleDrawer,
    RoundedModuleDrawer,
    VerticalBarsDrawer,
    HorizontalBarsDrawer,
)
from qrcode.image.styles.moduledrawers.svg import (
    SvgPathSquareDrawer,
    SvgPathCircleDrawer,
)
from qrcode.image.styles.colormasks import (
    SolidFillColorMask,
    RadialGradiantColorMask,
    SquareGradiantColorMask,
    HorizontalGradiantColorMask,
    VerticalGradiantColorMask,
)
from function2widgets.widgets.misc import Color

FUNC_NAME = QApplication.tr("二维码生成器")

DEFAULT_VERSION = None
DEFAULT_ERROR_CORRECTION = "M"
DEFAULT_BG_COLOR = Color.from_color_name("white")
DEFAULT_FILL_COLOR = Color.from_color_name("black")
DEFAULT_BOX_SIZE = 8
DEFAULT_BORDER = 2
DEFAULT_SIZE_RATIO = 1.0
DEFAULT_MODULE_DRAWER = None
DEFAULT_COLOR_MASK = None
DEFAULT_SVG_FACTORY = SvgPathImage


# --error correction---
ERR_CORRECTION_LEVELS = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H,
}
# -----------------------


# -----module drawer-----
SQUARE_DRAWER = QApplication.tr("Square")
CIRCLE_DRAWER = QApplication.tr("Circle")
ROUNDED_DRAWER = QApplication.tr("Rounded")
GAPPED_DRAWER = QApplication.tr("Gapped")
VERTICAL_BARS_DRAWER = QApplication.tr("Vertical Bars")
HORIZONTAL_BARS_DRAWER = QApplication.tr("Horizontal Bars")

MODULE_DRAWERS = {
    SQUARE_DRAWER: (SquareModuleDrawer, SvgPathSquareDrawer),
    CIRCLE_DRAWER: (CircleModuleDrawer, SvgPathCircleDrawer),
    ROUNDED_DRAWER: RoundedModuleDrawer,
    GAPPED_DRAWER: GappedSquareModuleDrawer,
    VERTICAL_BARS_DRAWER: VerticalBarsDrawer,
    HORIZONTAL_BARS_DRAWER: HorizontalBarsDrawer,
}
PNG_DRAWER_IDX = 0
SVG_DRAWER_IDX = 1

MODULE_DRAWERS_SUPPORT_SIZE_RATIO = (
    SquareModuleDrawer,
    SvgPathSquareDrawer,
    CircleModuleDrawer,
    SvgPathCircleDrawer,
    GappedSquareModuleDrawer,
)
# -------------------------


# ---overwrite behavior----
OVERWRITE_BEHAVIOR_ASK = QApplication.tr("询问")
OVERWRITE_BEHAVIOR_NOT_OVERWRITE = QApplication.tr("不覆盖")
OVERWRITE_BEHAVIOR_OVERWRITE = QApplication.tr("覆盖")
OVERWRITE_BEHAVIORS = (
    OVERWRITE_BEHAVIOR_ASK,
    OVERWRITE_BEHAVIOR_NOT_OVERWRITE,
    OVERWRITE_BEHAVIOR_OVERWRITE,
)
DEFAULT_OVERWRITE_BEHAVIOR = OVERWRITE_BEHAVIORS[0]
# -------------------------


# --------color mask-------
COLOR_MASK_SOLID_FILL = QApplication.tr("纯色填充")
COLOR_MASK_RADIAL_GRADIENT = QApplication.tr("径向渐变(圆形)")
COLOR_MASK_SQUARE_RADIAL_GRADIENT = QApplication.tr("径向渐变(方形)")
COLOR_MASK_HORIZONTAL_GRADIENT = QApplication.tr("水平渐变")
COLOR_MASK_VERTICAL_GRADIENT = QApplication.tr("垂直渐变")

_RADIAL_GRADIENT = QApplication.tr("径向渐变")
BACK_COLOR_LABEL = QApplication.tr("背景颜色(全部)")
FRONT_COLOR_LABEL = QApplication.tr("前景颜色({})".format(COLOR_MASK_SOLID_FILL))
CENTER_COLOR_LABEL = QApplication.tr("中心颜色({})".format(_RADIAL_GRADIENT))
EDGE_COLOR_LABEL = QApplication.tr("边缘颜色({})".format(_RADIAL_GRADIENT))
LEFT_COLOR_LABEL = QApplication.tr(
    "左侧颜色({})".format(COLOR_MASK_HORIZONTAL_GRADIENT)
)
RIGHT_COLOR_LABEL = QApplication.tr(
    "右侧颜色({})".format(COLOR_MASK_HORIZONTAL_GRADIENT)
)
TOP_COLOR_LABEL = QApplication.tr("上侧颜色({})".format(COLOR_MASK_VERTICAL_GRADIENT))
BOTTOM_COLOR_LABEL = QApplication.tr(
    "下侧颜色({})".format(COLOR_MASK_VERTICAL_GRADIENT)
)

DEFAULT_COLOR_MASK_COLORS = {
    BACK_COLOR_LABEL: Color(255, 255, 255),
    FRONT_COLOR_LABEL: Color(0, 0, 0),
    CENTER_COLOR_LABEL: Color(0, 0, 0),
    EDGE_COLOR_LABEL: Color(0, 0, 255),
    LEFT_COLOR_LABEL: Color(0, 0, 0),
    RIGHT_COLOR_LABEL: Color(0, 0, 255),
    TOP_COLOR_LABEL: Color(0, 0, 0),
    BOTTOM_COLOR_LABEL: Color(0, 0, 255),
}

COLOR_MASKS = {
    COLOR_MASK_SOLID_FILL: SolidFillColorMask,
    COLOR_MASK_RADIAL_GRADIENT: RadialGradiantColorMask,
    COLOR_MASK_SQUARE_RADIAL_GRADIENT: SquareGradiantColorMask,
    COLOR_MASK_HORIZONTAL_GRADIENT: HorizontalGradiantColorMask,
    COLOR_MASK_VERTICAL_GRADIENT: VerticalGradiantColorMask,
}
COLOR_MASK_REQUIRED_COLOR_LABELS = {
    SolidFillColorMask: (
        BACK_COLOR_LABEL,
        FRONT_COLOR_LABEL,
    ),
    RadialGradiantColorMask: (
        BACK_COLOR_LABEL,
        CENTER_COLOR_LABEL,
        EDGE_COLOR_LABEL,
    ),
    SquareGradiantColorMask: (
        BACK_COLOR_LABEL,
        CENTER_COLOR_LABEL,
        EDGE_COLOR_LABEL,
    ),
    HorizontalGradiantColorMask: (
        BACK_COLOR_LABEL,
        LEFT_COLOR_LABEL,
        RIGHT_COLOR_LABEL,
    ),
    VerticalGradiantColorMask: (
        BACK_COLOR_LABEL,
        TOP_COLOR_LABEL,
        BOTTOM_COLOR_LABEL,
    ),
}
# ------------------------


# -----file filters-------
EMBED_IMG_FILE_FILTERS = QApplication.tr(
    "PNG文件(*.png);;JPG文件(*.jpg);;JPEG文件(*.jpeg);;所有文件(*.*)"
)

BACKGROUND_IMAGE_FILE_FILTERS = QApplication.tr(
    "PNG文件(*.png);;JPG文件(*.jpg);;JPEG文件(*.jpeg);;GIF文件(*.gif);;所有文件(*.*)"
)
# ------------------------
