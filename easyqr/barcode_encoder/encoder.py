import os

from barcode import get_barcode_class
from barcode.writer import SVGWriter, ImageWriter
from function2widgets.widgets.misc import Color

from easyqr.common import BaseEncoder, is_same_filetype
from easyqr.utils import safe_pop
from ._constants import TR_ERR_EMPTY_BARCODE_TYPE, TR_ERR_EMPTY_FONT_PATH, TR_ERR_FONT_NOT_FOUND, DEFAULT_BACKGROUND, \
    DEFAULT_FOREGROUND


class BarCodeEncoder(BaseEncoder):

    def __init__(self):
        super().__init__()

    def check_arguments(
            self,
            output_dir: str,
            make_dirs: bool,
            output_filename: str,
            data: str,
            overwrite_behavior: str,
            barcode_type: str = None,
            font_path: str = None
    ):
        super().check_arguments(
            output_dir=output_dir,
            make_dirs=make_dirs,
            output_filename=output_filename,
            data=data,
            overwrite_behavior=overwrite_behavior,
        )

        if not barcode_type:
            raise ValueError(TR_ERR_EMPTY_BARCODE_TYPE)

        if font_path is not None:
            font_path = font_path.strip()
            if font_path == "":
                raise ValueError(TR_ERR_EMPTY_FONT_PATH)
            if not os.path.isfile(font_path):
                raise ValueError(TR_ERR_FONT_NOT_FOUND.format(font_path))

    def encode(
            self,
            output_dir: str,
            make_dirs: bool,
            output_filename: str,
            data: str,
            overwrite_behavior: str,
            barcode_type: str = None,
            barcode_extra_args: dict = None,
            module_width: float = None,
            module_height: float = None,
            quiet_zone: int = None,
            font_path: str = None,
            font_size: int = None,
            text_distance: float = None,
            background: Color = None,
            foreground: Color = None,
            center_text: bool = None,
            verbose: bool = None,
            show_result_img: bool = None,
    ):
        super().encode(
            output_dir=output_dir,
            make_dirs=make_dirs,
            output_filename=output_filename,
            data=data,
            overwrite_behavior=overwrite_behavior,
            barcode_type=barcode_type,
            font_path=font_path,
        )
        self.verbose = verbose is True

        if barcode_extra_args is None:
            barcode_extra_args = {}
        safe_pop(barcode_extra_args, "writer")

        if background is None:
            background = DEFAULT_BACKGROUND
        if foreground is None:
            foreground = DEFAULT_FOREGROUND
        options = {}
        self._add_options_to(options,
                             module_width=module_width,
                             module_height=module_height,
                             quiet_zone=quiet_zone,
                             font_path=font_path,
                             font_size=font_size,
                             text_distance=text_distance,
                             background=background.to_hex_string(with_alpha=False),
                             foreground=foreground.to_hex_string(with_alpha=False),
                             center_text=center_text)

        output_filepath = os.path.abspath(os.path.join(output_dir, output_filename))
        is_svg_file = is_same_filetype(path=output_filepath, file_ext=".svg")

        if is_svg_file:
            writer = SVGWriter()
        else:
            writer = ImageWriter()

        barcode_class = get_barcode_class(barcode_type)
        with open(output_filepath, "wb") as f:
            ins = barcode_class(data, writer=writer, **barcode_extra_args)
            ins.write(f, options=options)

        if show_result_img is True:
            self.print_image(output_filepath)

    @staticmethod
    def _add_options_to(options: dict, **kvs):
        for k, v in kvs.items():
            if v is not None:
                options[k] = v


_global_instance = BarCodeEncoder()
make_barcode = _global_instance.encode
