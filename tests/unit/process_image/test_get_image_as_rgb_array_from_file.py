import numpy as np
import pytest
from src.process_image import get_image_as_rgb_array_from_file


@pytest.mark.parametrize("factor, expected_result", [
    (1.0, (1517, 1020)),
    (1.5, (2266, 1520)),
])
def test_get_image_as_rgb_array_from_file(factor, expected_result, prep_image_path):
    image_path = prep_image_path
    image = get_image_as_rgb_array_from_file(image_path, factor=factor)
    assert isinstance(image, np.ndarray)
    assert image.shape == expected_result
