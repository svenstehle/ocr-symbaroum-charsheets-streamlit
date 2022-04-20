#
# License: APACHE LICENSE, VERSION 2.0
#
import cv2
import numpy as np
from PIL import Image
from skimage import filters

# TODO write tests for all this once it is more stable and not trial & error


def load_image_from_file(uploaded_image: object) -> Image:
    img = Image.open(uploaded_image)
    return img


def rescale_img_arr(img: np.ndarray, factor) -> np.ndarray:
    img = np.asarray(img)
    assert isinstance(img, np.ndarray)
    if factor > 1.0:
        img = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_CUBIC)
    elif factor < 1.0:
        img = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_AREA)
    return img


def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def apply_dilation_erosions(img: np.ndarray, kernel_size: int) -> np.ndarray:
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    img = cv2.erode(img, kernel, iterations=1)
    return img


def denoising(img):
    # worthwhile as a LAST step! :)
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
def preprocess_image(img: np.ndarray, factor: float) -> np.ndarray:
    img = rescale_img_arr(img, factor)
    img = convert_to_grayscale(img)
    img = thresholding(img)
    # img = apply_dilation_erosions(img, kernel_size=2)
    img = denoising(img)
    img = add_white_border(img, bordersize=10)
    # don't do rotation correction for now, we only use PDFs and not slanted scans
    return img


def get_image_as_rgb_array_from_file(uploaded_image: object, factor: float) -> np.ndarray:
    image = load_image_from_file(uploaded_image)
    image = preprocess_image(image, factor)
    return image
