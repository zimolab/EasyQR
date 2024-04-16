import os

from barcode import get_barcode_class
from barcode.writer import SVGWriter, ImageWriter

from easyqr.common import BaseEncoder, is_same_filetype
from easyqr.utils import safe_pop
from ._constants import *


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
        font_path: str = None,
        dpi: int = None,
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

        if dpi is not None:
            if dpi <= 0:
                raise ValueError(TR_ERR_INVALID_DPI)

    def encode(
        self,
        output_dir: str,
        make_dirs: bool,
        output_filename: str,
        data: str,
        text: str,
        overwrite_behavior: str,
        barcode_type: str = None,
        barcode_extra_args: dict = None,
        dpi: int = None,
        compress: bool = None,
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
        if barcode_extra_args is None:
            barcode_extra_args = {}
        safe_pop(barcode_extra_args, "writer")
        if background is None:
            background = DEFAULT_BACKGROUND
        if foreground is None:
            foreground = DEFAULT_FOREGROUND

        super().encode(
            output_dir=output_dir,
            make_dirs=make_dirs,
            output_filename=output_filename,
            data=data,
            overwrite_behavior=overwrite_behavior,
            verbose=verbose,
            barcode_type=barcode_type,
            font_path=font_path,
            dpi=dpi,
        )

        output_filepath = os.path.abspath(os.path.join(output_dir, output_filename))
        is_svg_file = is_same_filetype(path=output_filepath, file_ext=".svg")

        if is_svg_file and dpi is not None:
            self.warning(TR_WARN_SVG_DPI_IGNORED)
            dpi = None

        if not is_svg_file and compress:
            self.warning(TR_WARN_PNG_COMPRESS_IGNORED)
            compress = None

        if is_svg_file:
            writer = SVGWriter()
        else:
            writer = ImageWriter()

        barcode_class = get_barcode_class(barcode_type)
        with open(output_filepath, "wb") as f:
            options = {}
            self._add_options_to(
                options,
                dpi=dpi,
                compress=compress,
                module_width=module_width,
                module_height=module_height,
                quiet_zone=quiet_zone,
                font_path=font_path,
                font_size=font_size,
                text_distance=text_distance,
                background=background.to_hex_string(with_alpha=False),
                foreground=foreground.to_hex_string(with_alpha=False),
                center_text=center_text,
            )
            ins = barcode_class(data, writer=writer, **barcode_extra_args)
            ins.write(f, text=text, options=options)

        if show_result_img is True:
            self.print_image(output_filepath)

    @staticmethod
    def _add_options_to(options: dict, **kvs):
        for k, v in kvs.items():
            if v is not None:
                options[k] = v


_global_instance = BarCodeEncoder()
make_barcode = _global_instance.encode
