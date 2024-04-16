import abc
import os.path
from typing import Optional

from pyguiadapter.interact import ulogging, uprint
from pyguiadapter.interact.upopup import question

from ._constants import (
    TR_ERR_OUTPUT_DIR_NOT_EXIST,
    TR_ERR_EMPTY_OUTPUT_FILENAME,
    TR_ERR_INVALID_OUTPUT_FILENAME,
    TR_ERR_EMPTY_DATA,
    TR_ERR_OVERWRITE_NOT_ALLOWED,
    TR_MSG_MKDIRS,
    TR_MSG_WILL_BE_OVERWRITTEN,
    TR_MSG_ASK_FOR_OVERWRITE,
)
from ._enum import OverwriteBehavior
from ._utils import get_overwrite_behavior


class BaseEncoder(abc.ABC):

    def __init__(
        self, enable_timestamp: bool = True, timestamp_pattern: str = None, verbose=True
    ):
        self.enable_timestamp: bool = enable_timestamp
        self.timestamp_pattern: Optional[str] = timestamp_pattern
        self.verbose: bool = verbose

    def debug(self, message: str):
        if self.verbose:
            ulogging.debug(
                message,
                timestamp=self.enable_timestamp,
                timestamp_pattern=self.timestamp_pattern,
            )

    def info(self, message: str):
        if self.verbose:
            ulogging.info(
                message,
                timestamp=self.enable_timestamp,
                timestamp_pattern=self.timestamp_pattern,
            )

    def warning(self, message: str):
        if self.verbose:
            ulogging.warning(
                message,
                timestamp=self.enable_timestamp,
                timestamp_pattern=self.timestamp_pattern,
            )

    def error(self, message: str):
        if self.verbose:
            ulogging.critical(
                message,
                timestamp=self.enable_timestamp,
                timestamp_pattern=self.timestamp_pattern,
            )

    # noinspection PyMethodMayBeStatic
    def print(self, message: str = "", html: bool = False):
        uprint.uprint(message, html=html)

    def print_image(self, image_filepath: str, blank_lines: bool = True):
        if blank_lines:
            self.print()
        img_tag = f"<img src='{os.path.abspath(image_filepath)}' />"
        self.print(img_tag, html=True)
        if blank_lines:
            self.print()

    def _check_overwrite(self, filepath: str, behavior: OverwriteBehavior):
        if not os.path.isfile(filepath):
            return
        if behavior == OverwriteBehavior.NotOverwrite:
            raise ValueError(TR_ERR_OVERWRITE_NOT_ALLOWED)
        elif behavior == OverwriteBehavior.Overwrite:
            self.warning(TR_MSG_WILL_BE_OVERWRITTEN)
            return
        else:
            if question(TR_MSG_ASK_FOR_OVERWRITE):
                self.warning(TR_MSG_WILL_BE_OVERWRITTEN)
            else:
                raise ValueError(TR_ERR_OVERWRITE_NOT_ALLOWED)

    def check_arguments(
        self,
        output_dir: str,
        make_dirs: bool,
        output_filename: str,
        data: str,
        overwrite_behavior: str,
        **kwargs,
    ):
        if not output_dir:
            output_dir = "./"
        output_dir_exists = os.path.isdir(output_dir)
        if not output_dir_exists and not make_dirs:
            raise ValueError(TR_ERR_OUTPUT_DIR_NOT_EXIST.format(output_dir))

        if not output_dir_exists and make_dirs:
            self.info(TR_MSG_MKDIRS.format(output_dir))
            os.makedirs(output_dir, exist_ok=True)

        # 文件名不可为空
        if not output_filename:
            raise ValueError(TR_ERR_EMPTY_OUTPUT_FILENAME)
        # 文件格式限制为svg或png
        if not (output_filename.endswith(".svg") or output_filename.endswith(".png")):
            raise ValueError(TR_ERR_INVALID_OUTPUT_FILENAME)
        # 文件存在性检测
        output_filepath = os.path.join(output_dir, output_filename)
        behavior = get_overwrite_behavior(overwrite_behavior)
        self._check_overwrite(output_filepath, behavior)
        # 确保待编码数据不为空
        if not data:
            raise ValueError(TR_ERR_EMPTY_DATA)

    @abc.abstractmethod
    def encode(
        self,
        output_dir: str,
        make_dirs: bool,
        output_filename: str,
        data: str,
        overwrite_behavior: str,
        verbose: bool,
        **kwargs,
    ):
        if verbose is not None:
            self.verbose = verbose is True
        self.check_arguments(
            output_dir=output_dir,
            make_dirs=make_dirs,
            output_filename=output_filename,
            data=data,
            overwrite_behavior=overwrite_behavior,
            **kwargs,
        )
