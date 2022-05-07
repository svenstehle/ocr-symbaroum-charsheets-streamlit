import pytest


@pytest.fixture()
def create_ocr_test_setup(prep_ocr_image, prep_hydra_config):
    cfg = prep_hydra_config
    image = prep_ocr_image
    psm = 3
    yield cfg, image, psm
    del cfg, image, psm
