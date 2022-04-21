import numpy as np
import pytest
from src.process_image import ImageProcessor


@pytest.mark.parametrize(
    "color_img, factor, bordersize, expected_result", [
        (pytest.lazy_fixture("prep_color_img_arr"), 0.5, 10, np.ones((70, 70))),
        (pytest.lazy_fixture("prep_color_img_arr"), 1.5, 20, np.ones((190, 190))),
        (pytest.lazy_fixture("prep_color_img_arr"), 1.0, 1, np.ones((102, 102))),
    ]
)
def test_preprocess_image(color_img, factor, bordersize, expected_result):
    IP = ImageProcessor(factor, bordersize)
    IP.img = color_img
    IP.preprocess_image()
    assert IP.img.ndim == 2
    assert IP.img.shape == expected_result.shape
    assert IP.img.min() == 0
    assert IP.img.max() == 255
