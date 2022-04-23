import pytest
from src.process_image import ImageProcessor


def test_is_image_grayscale_valid(prep_grayscale_img_arr):
    IP = ImageProcessor()
    IP.img = prep_grayscale_img_arr
    assert IP.is_image_grayscale()


def test_is_image_grayscale_exception(prep_color_img_arr):
    IP = ImageProcessor()
    IP.img = prep_color_img_arr
    with pytest.raises(ValueError):
        IP.is_image_grayscale()
