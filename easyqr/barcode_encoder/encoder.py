import os

from barcode import get_barcode_class
from barcode.writer import SVGWriter, ImageWriter

from easyqr.common import BaseEncoder
from easyqr.utils import safe_pop
from ._constants import TR_ERR_BARCODE_TYPE


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
    ):
        super().check_arguments(
            output_dir=output_dir,
            make_dirs=make_dirs,
            output_filename=output_filename,
            data=data,
            overwrite_behavior=overwrite_behavior,
        )
        if not barcode_type:
            raise ValueError(TR_ERR_BARCODE_TYPE)

    def encode(
        self,
        output_dir: str,
        make_dirs: bool,
        output_filename: str,
        data: str,
        overwrite_behavior: str,
        barcode_type: str = None,
        barcode_extra_args: dict = None,
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
        )
        self.verbose = verbose is True

        if barcode_extra_args is None:
            barcode_extra_args = {}

        safe_pop(barcode_extra_args, "writer")

        output_filepath = os.path.abspath(os.path.join(output_dir, output_filename))
        _, ext = os.path.splitext(output_filepath)
        output_svg_file = ext.lower() == ".svg"

        if output_svg_file:
            writer = SVGWriter()
            writer.set_options({"compressed": True})
        else:
            writer = ImageWriter()
        barcode_class = get_barcode_class(barcode_type)
        with open(output_filepath, "wb") as f:
            ins = barcode_class(data, writer=writer)
            ins.write(f)
        if show_result_img is True:
            self.print_image(output_filepath)


_global_instance = BarCodeEncoder()
make_barcode = _global_instance.encode
