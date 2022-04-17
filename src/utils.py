# License: APACHE LICENSE, VERSION 2.0

from typing import List


def is_filename_supported_image(filename: str, supported_image_types: List[str]) -> bool:
    file_extension = filename.split(".")[-1]
    return file_extension in supported_image_types
