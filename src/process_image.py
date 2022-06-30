#
# License: APACHE LICENSE, VERSION 2.0
#

from typing import Union

import cv2
import numpy as np
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from PIL.PngImagePlugin import PngImageFile
from PIL.TiffImagePlugin import TiffImageFile
from skimage import filters

upload_image_types = Union[PngImageFile, TiffImageFile, None]    # None at app start
accepted_image_types = Union[JpegImageFile, upload_image_types]
processed_image_types = Union[np.ndarray, None]


class ImageProcessor:
    """Class to preprocess images for OCR"""
    def __init__(self, factor: float = 1.0, bordersize: int = 10) -> None:
        """Constructs all the necessary attributes for the ImageProcessor object.

        Args:
            factor (float, optional): the rescale factor. Larger than 1 equals to zoom interpolation.
                Defaults to 1.0.
            bordersize (int, optional): the bordersize used during application
                of white border around the image with add_white_border. Defaults to 10.
        """
        self.img: processed_image_types = None
        self.factor = factor
        self.bordersize = bordersize

    def get_processed_image(self, uploaded_image: accepted_image_types) -> np.ndarray:
        """Load and preprocess the image.

        Args:
            uploaded_image (accepted_image_types): the image received from the streamlit file_uploader

        Returns:
            np.ndarray: the processed image
        """
        self.load_image_from_file(uploaded_image)
        self.preprocess_image()
        self.raise_if_not_ndarray("Image was not processed correctly!")
        # The environment mypy flags the value if we do not assert and we used # type: ignore.
        # But then pre-commit mypy complains about unused # type: ignore on return
        # Since we perform the same check in self.raise_if_not_ndarray, this is unfortunately very redundant
        assert isinstance(self.img, np.ndarray)
        return self.img

    def load_image_from_file(self, uploaded_image: accepted_image_types) -> None:
        """Load the image as PIL Image from the uploaded file and store it in the ImageProcessor object.

        Args:
            uploaded_image (accepted_image_types): uploaded image from streamlit file_uploader or clipboard.
        """
        try:
            self.img = Image.open(uploaded_image)
        except AttributeError:
            self.img = np.array(uploaded_image)

    def preprocess_image(self) -> None:
        """Preprocess the image and save it in the ImageProcessor object."""
        self.rescale_img_arr()
        self.convert_to_grayscale()
        self.apply_thresholding()
        self.apply_denoising()
        self.add_white_border()

    def raise_if_not_ndarray(self, msg: str) -> None:
        """Raises ValueError if the image is not a numpy array.

        Args:
            msg (str): the string to be displayed in the raised ValueError

        Raises:
            ValueError: _description_
        """
        if not isinstance(self.img, np.ndarray):
            raise ValueError(f"self.img is no instance of 'np.ndarray', {msg}")

    def rescale_img_arr(self) -> None:
        """Rescale the image to the desired factor. If factor is 1.0, no rescaling is applied."""
        self.img = np.asarray(self.img)
        if self.factor > 1.0:
            self.img = cv2.resize(self.img, None, fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LANCZOS4)
        elif self.factor < 1.0:
            self.img = cv2.resize(self.img, None, fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LANCZOS4)

    def convert_to_grayscale(self) -> None:
        """Convert the image to grayscale."""
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def is_image_grayscale(self) -> bool:
        """Check if the image is grayscale.

        Raises:
            ValueError: raise if the image is not grayscale

        Returns:
            bool: returns True if the image is grayscale, raises ValueError otherwise
        """
        self.raise_if_not_ndarray("Image was not loaded!")
        if self.img.ndim != 2:    # type: ignore
            raise ValueError("Image must be grayscale!")
        return True

    def apply_thresholding(self) -> None:
        """Apply thresholding filter to the image."""
        self.is_image_grayscale()
        # designed for text recognition, can be configured/tuned
        self.img = (self.img > filters.threshold_sauvola(self.img)).astype(np.uint8) * 255

    def apply_denoising(self) -> None:
        """Apply denoising filter to the image."""
        self.is_image_grayscale()
        # worthwhile as a LAST step! :) - Thresholding can introduce noise
        self.img = cv2.fastNlMeansDenoising(self.img, h=3, templateWindowSize=7, searchWindowSize=21)

    def add_white_border(self) -> None:
        """Add white border around the image."""
        self.img = cv2.copyMakeBorder(
            self.img,
            top=self.bordersize,
            bottom=self.bordersize,
            left=self.bordersize,
            right=self.bordersize,
            borderType=cv2.BORDER_CONSTANT,
            value=[255, 255, 255]
        )
