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
    # return img
    # return cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    return cv2.resize(img, None, fx=1.1, fy=1.1, interpolation=cv2.INTER_CUBIC)


def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def apply_dilation_erosions(img: np.ndarray, kernel_size: int) -> np.ndarray:
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    img = cv2.erode(img, kernel, iterations=1)
    return img


def apply_blur(img: np.ndarray) -> np.ndarray:
    img = cv2.threshold(cv2.bilateralFilter(img, 10, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img


def convert_to_hsv(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def apply_inrange_thresholding(hsv_image):
    max_value = 255
    max_value_H = 360 // 2
    low_H = 0
    low_S = 0
    low_V = 0
    high_H = max_value_H
    high_S = max_value
    high_V = max_value
    img_threshed = cv2.inRange(hsv_image, (low_H, low_S, low_V), (high_H, high_S, high_V))
    # mask = cv2.inRange(hsv_image, np.array([0, 180, 218]), np.array([60, 255, 255]))
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    # img = cv2.dilate(mask, kernel, iterations=1)
    # img = 255 - cv2.bitwise_and(img, mask)
    return img_threshed
    # return mask


def preprocess_image(img: np.ndarray) -> np.ndarray:
    # img = rescale_img(img)
    # img = convert_to_hsv(img)
    # img = apply_inrange_thresholding(img)
    img = convert_to_grayscale(img)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    img = cv2.bitwise_not(img)
    # img = apply_dilation_erosions(img, kernel_size=1)
    # dont use these for now, the images are not homogeneous enough to fine-tune this
    # img = apply_blur(img)
    return img


def get_image_as_rgb_array_from_file(path_to_image: str) -> np.ndarray:
    im_pil = load_image_from_file(path_to_image)
    # To use it in the OCR part
    image = np.asarray(im_pil)
    image = preprocess_image(image)
    return image
