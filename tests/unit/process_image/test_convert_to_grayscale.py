import numpy as np
from src.process_image import ImageProcessor


def test_convert_to_grayscale(prep_color_img_arr):
    IP = ImageProcessor()
    IP.img = prep_color_img_arr
    IP.convert_to_grayscale()
    assert IP.img.shape == (100, 100)
    assert IP.img.dtype == np.uint8
    assert IP.img.min() == 0
    assert IP.img.max() == 255
