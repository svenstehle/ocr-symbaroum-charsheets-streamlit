import numpy as np
import pytest
from src.process_image import ImageProcessor


@pytest.mark.parametrize(
    "img_arr, factor, expected_result", [
        (pytest.lazy_fixture("prep_color_img_arr"), 1.0, pytest.lazy_fixture("prep_color_img_arr")),
        (pytest.lazy_fixture("prep_color_img_arr"), 1.5, np.ones((150, 150, 4))),
        (pytest.lazy_fixture("prep_color_img_arr"), 0.5, np.ones((50, 50, 4)))
    ]
)
def test_rescale_img_arr(img_arr, factor, expected_result):
    IP = ImageProcessor(factor)
    IP.img = img_arr
    IP.rescale_img_arr()
    assert IP.img.shape == expected_result.shape
