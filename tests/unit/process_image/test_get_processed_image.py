import numpy as np
import pytest
from src.process_image import ImageProcessor


@pytest.mark.parametrize("factor, bordersize, expected_result", [
    (1.0, 10, (1517, 1020)),
    (1.5, 25, (2296, 1550)),
])
def test_get_processed_image(factor, bordersize, expected_result, prep_image_path):
    image_path = prep_image_path
    IP = ImageProcessor(factor, bordersize)
    img = IP.get_processed_image(image_path)
    assert isinstance(IP.img, np.ndarray)
    assert IP.img.shape == expected_result
    assert np.all(img == IP.img)
