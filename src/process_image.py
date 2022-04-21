#
# License: APACHE LICENSE, VERSION 2.0
#
from typing import Union

import cv2
import numpy as np

from PIL import Image
from PIL.PngImagePlugin import PngImageFile
from PIL.TiffImagePlugin import TiffImageFile
from skimage import filters

# TODO write tests for all this once it is more stable and not trial & error
accepted_image_types = Union[PngImageFile, TiffImageFile]


def load_image_from_file(uploaded_image: object) -> accepted_image_types:
    img = Image.open(uploaded_image)
    return img


def rescale_img_arr(img: accepted_image_types, factor) -> np.ndarray:
    img = np.asarray(img)
    if factor > 1.0:
        img = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_LANCZOS4)
    elif factor < 1.0:
        img = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_LANCZOS4)
    return img


def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def denoising(img):
    # worthwhile as a LAST step! :) - Thresholding can introduce noise
    return cv2.fastNlMeansDenoising(img, h=3, templateWindowSize=7, searchWindowSize=21)


def thresholding(img):
    # designed for text recognition, can be configured/tuned
    return (img > filters.threshold_sauvola(img)).astype(np.uint8) * 255


def add_white_border(img, bordersize=10):
    return cv2.copyMakeBorder(
        img,
        top=bordersize,
        bottom=bordersize,
        left=bordersize,
        right=bordersize,
        borderType=cv2.BORDER_CONSTANT,
        value=[255, 255, 255]
    )


# test all this with the new images
def preprocess_image(img: accepted_image_types, factor: float) -> np.ndarray:
    # don't do rotation correction for now, we only use PDFs and not slanted scans
    img = rescale_img_arr(img, factor)
    img = convert_to_grayscale(img)
    img = thresholding(img)
    img = denoising(img)
    img = add_white_border(img, bordersize=10)
    return img


def get_image_as_rgb_array_from_file(uploaded_image: object, factor: float) -> np.ndarray:
    image = load_image_from_file(uploaded_image)
    image = preprocess_image(image, factor)
    return image
