import numpy as np
import pytest
from src.process_image import get_image_as_rgb_array_from_file


@pytest.mark.parametrize("factor, expected_result", [
    (1.0, (1517, 1020)),
    (1.5, (2266, 1520)),
])
def test_get_image_as_rgb_array_from_file(factor, expected_result):
    image_path = "tests/unit/process_image/cat.jpeg"
    image = get_image_as_rgb_array_from_file(image_path, factor=factor)
    assert isinstance(image, np.ndarray)
    assert image.shape == expected_result
