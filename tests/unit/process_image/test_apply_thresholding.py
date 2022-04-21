import numpy as np
import pytest
from src.process_image import ImageProcessor


def test_apply_thresholding(prep_grayscale_img_arr):
    IP = ImageProcessor()
    IP.img = prep_grayscale_img_arr
    IP.apply_thresholding()
    assert IP.img.shape == (100, 100)
    assert IP.img.dtype == np.uint8
    assert IP.img.min() == 0
    assert IP.img.max() == 255


def test_apply_thresholding_exception(prep_color_img_arr):
    IP = ImageProcessor()
    IP.img = prep_color_img_arr
    with pytest.raises(ValueError):
        IP.apply_thresholding()
