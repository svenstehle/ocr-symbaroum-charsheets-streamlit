#
# License: APACHE LICENSE, VERSION 2.0
#
import numpy as np
from PIL import Image


def load_image_from_file(image_file):
    img = Image.open(image_file)
    return img


def get_image_as_rgb_array_from_file(image_file: object) -> np.ndarray:
    im_pil = load_image_from_file(image_file)
    # To use it in the OCR part
    image = np.asarray(im_pil)
    return image
