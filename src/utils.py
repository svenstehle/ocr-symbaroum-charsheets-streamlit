# License: APACHE LICENSE, VERSION 2.0

from typing import List


def is_filename_supported_image(filename: str, supported_image_types: List[str]) -> bool:
    """Check if the provided filename is a supported image type.
    Extension of the filename is used to determine this.

    Args:
        filename (str): filename to check
        supported_image_types (List[str]): list of filename extensions that are supported

    Returns:
        bool: True if the filename is supported, False otherwise
    """
    file_extension = filename.split(".")[-1]
    return file_extension in supported_image_types
