import os.path

from easyqr.utils import curdir, rand_filename
from ._enum import OverwriteBehavior
from ._trs import *

DEFAULT_IMG_EXT = ".png"
DEFAULT_OUTPUT_DIR = curdir()
DEFAULT_OUTPUT_FILENAME = rand_filename(prefix="code_", ext=DEFAULT_IMG_EXT)
DEFAULT_START_PATH = os.path.abspath("./")

OVERWRITE_BEHAVIORS = {
    TR_OVERWRITE_ASK: OverwriteBehavior.Ask,
    TR_OVERWRITE_OVERWRITE: OverwriteBehavior.Overwrite,
    TR_OVERWRITE_NOT_OVERWRITE: OverwriteBehavior.NotOverwrite,
}

DEFAULT_OVERWRITE_BEHAVIOR = TR_OVERWRITE_ASK
