import pytest


@pytest.fixture()
def prep_perform_ocr(prep_ocr_image, prep_hydra_config):
    ocr_config = prep_hydra_config.ocr
    lang = "eng"
    psm = 3
    image = prep_ocr_image
    yield ocr_config, lang, psm, image
    del ocr_config, lang, psm, image
