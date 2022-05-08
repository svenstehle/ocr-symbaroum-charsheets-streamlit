import pytest
from src.process_image import ImageProcessor


def test_is_image_grayscale_valid(prep_grayscale_img_arr):
    IP = ImageProcessor()
    IP.img = prep_grayscale_img_arr
    assert IP.is_image_grayscale()


def test_is_image_grayscale_exception_not_grayscale(prep_color_img_arr):
    IP = ImageProcessor()
    IP.img = prep_color_img_arr
    with pytest.raises(ValueError) as e:
        IP.is_image_grayscale()
    assert str(e.value) == "Image must be grayscale!"


def test_is_image_grayscale_exception_not_ndarray():
    IP = ImageProcessor()
    IP.img = None
    with pytest.raises(ValueError) as e:
        IP.is_image_grayscale()
    assert str(e.value) == "self.img is no instance of 'np.ndarray', Image was not loaded!"
