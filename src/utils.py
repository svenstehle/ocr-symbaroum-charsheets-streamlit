# License: APACHE LICENSE, VERSION 2.0

import numpy as np

from process_image import ImageProcessor, accepted_image_types


def get_processed_image_file(image_file: accepted_image_types, factor: float) -> np.ndarray:
    """Loads and processes an image either from an uploaded image by the streamlit file_uploader
    or an image loaded from disk with the path provided as str.

    Args:
        image_file (accepted_image_types): the accepted image types, either from the streamlit file_uploader
        or a path-like str.
        factor (float): the rescale factor provided by the user to the streamlit slider.

    Returns:
        np.ndarray: the processed image.
    """
    IP = ImageProcessor(factor)
    image = IP.get_processed_image(image_file)
    return image
