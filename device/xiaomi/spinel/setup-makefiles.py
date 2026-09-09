#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)


module = ExtractUtilsModule(
    "spinel",
    "xiaomi",
    check_elf=True,
    add_firmware_proprietary_file=False,
)


if __name__ == "__main__":
    utils = ExtractUtils.device(module)
    utils.run()
