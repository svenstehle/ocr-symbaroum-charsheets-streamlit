import pytest


@pytest.fixture()
def prep_perform_ocr(prep_ocr_image, prep_spock_config):
    ocr_config = prep_spock_config.OCRConfig
    lang = "eng"
    psm = 3
    image = prep_ocr_image
    yield ocr_config, lang, psm, image
    del ocr_config, lang, psm, image
