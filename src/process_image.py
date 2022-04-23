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

upload_image_types = Union[PngImageFile, TiffImageFile]
accepted_image_types = Union[upload_image_types, str]


class ImageProcessor:
    def __init__(self, factor: float = 1.0, bordersize: int = 10) -> None:
        self.img: upload_image_types = None
        self.factor = factor
        self.bordersize = bordersize

    def get_processed_image(self, uploaded_image: accepted_image_types) -> np.ndarray:
        self.load_image_from_file(uploaded_image)
        self.preprocess_image()
        return self.img

    def load_image_from_file(self, uploaded_image: accepted_image_types) -> None:
        self.img = Image.open(uploaded_image)

    def preprocess_image(self) -> None:
        self.rescale_img_arr()
        self.convert_to_grayscale()
        self.apply_thresholding()
        self.apply_denoising()
        self.add_white_border()

    def rescale_img_arr(self) -> None:
        self.img = np.asarray(self.img)
        if self.factor > 1.0:
            self.img = cv2.resize(self.img, None, fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LANCZOS4)
        elif self.factor < 1.0:
            self.img = cv2.resize(self.img, None, fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LANCZOS4)

    def convert_to_grayscale(self) -> None:
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def is_image_grayscale(self) -> bool:
        if self.img.ndim != 2:
            raise ValueError("Image must be grayscale")
        return True

    def apply_thresholding(self) -> None:
        self.is_image_grayscale()
        # designed for text recognition, can be configured/tuned
        self.img = (self.img > filters.threshold_sauvola(self.img)).astype(np.uint8) * 255

    def apply_denoising(self) -> None:
        self.is_image_grayscale()
        # worthwhile as a LAST step! :) - Thresholding can introduce noise
        self.img = cv2.fastNlMeansDenoising(self.img, h=3, templateWindowSize=7, searchWindowSize=21)

    def add_white_border(self) -> None:
        self.img = cv2.copyMakeBorder(
            self.img,
            top=self.bordersize,
            bottom=self.bordersize,
            left=self.bordersize,
            right=self.bordersize,
            borderType=cv2.BORDER_CONSTANT,
            value=[255, 255, 255]
        )
