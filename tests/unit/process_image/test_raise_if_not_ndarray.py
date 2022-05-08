import pytest
from src.process_image import ImageProcessor


@pytest.mark.parametrize(
    "image_type, msg, expected_result", [
        (None, "omg it is None", "self.img is no instance of 'np.ndarray', omg it is None"),
        ([1, 1], "test", "self.img is no instance of 'np.ndarray', test"),
    ]
)
def test_raise_if_not_ndarray_exception(image_type, msg, expected_result):
    IP = ImageProcessor()
    IP.img = image_type
    with pytest.raises(ValueError) as e:
        IP.raise_if_not_ndarray(msg)
    assert str(e.value) == expected_result


def test_raise_if_not_ndarray_valid(prep_color_img_arr):
    IP = ImageProcessor()
    IP.img = prep_color_img_arr
    IP.raise_if_not_ndarray("test")
    assert IP.img.ndim == 3
    assert IP.img.min() == 0
    assert IP.img.max() == 255
