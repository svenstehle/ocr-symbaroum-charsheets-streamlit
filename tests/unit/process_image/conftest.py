import numpy as np
import pytest


@pytest.fixture
def prep_color_img_arr():
    img_arr = np.random.randint(2, size=(100, 100, 4)) * 255
    img_arr = img_arr.astype(np.uint8)
    yield img_arr
    del img_arr


@pytest.fixture
def prep_grayscale_img_arr():
    img_arr = np.random.randint(2, size=(100, 100)) * 255
    img_arr = img_arr.astype(np.uint8)
    yield img_arr
    del img_arr


@pytest.fixture
def prep_image_path():
    yield "tests/unit/process_image/cat.png"
