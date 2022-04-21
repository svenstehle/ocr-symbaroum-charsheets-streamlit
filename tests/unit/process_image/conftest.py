import numpy as np
import pytest


@pytest.fixture
def prep_rescale_img_arr():
    img_arr = np.ones((1000, 1000, 3))
    yield img_arr
    del img_arr


@pytest.fixture
def prep_image_path():
    yield "tests/unit/process_image/cat.png"
