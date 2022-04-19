#
# License: APACHE LICENSE, VERSION 2.0
#
import cv2
import numpy as np
from PIL import Image


def load_image_from_file(path_to_image: str) -> Image:
    img = Image.open(path_to_image)
    return img


def rescale_img(img: np.ndarray) -> np.ndarray:
    return cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)


def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def apply_dilation_erosions(img: np.ndarray, kernel_size: int) -> np.ndarray:
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    return img


def apply_blur(img: np.ndarray) -> np.ndarray:
    img = cv2.threshold(cv2.bilateralFilter(img, 15, 80, 80), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img


def preprocess_image(img: np.ndarray) -> np.ndarray:
    img = rescale_img(img)
    img = convert_to_grayscale(img)
    img = apply_dilation_erosions(img, kernel_size=1)
    img = apply_blur(img)
    return img


def get_image_as_rgb_array_from_file(path_to_image: str) -> np.ndarray:
    im_pil = load_image_from_file(path_to_image)
    # To use it in the OCR part
    image = np.asarray(im_pil)
    image = preprocess_image(image)
    return image
