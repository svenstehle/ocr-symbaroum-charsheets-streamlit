import numpy as np
import pytest
from src.process_image import rescale_img_arr


@pytest.mark.parametrize(
    "img_arr, factor, expected_result", [
        (pytest.lazy_fixture("prep_rescale_img_arr"), 1.0, pytest.lazy_fixture("prep_rescale_img_arr")),
        (pytest.lazy_fixture("prep_rescale_img_arr"), 1.5, np.ones((1500, 1500, 3))),
        (pytest.lazy_fixture("prep_rescale_img_arr"), 0.5, np.ones((500, 500, 3)))
    ]
)
def test_rescale_img_arr(img_arr, factor, expected_result):
    result = rescale_img_arr(img_arr, factor)
    assert result.shape == expected_result.shape
