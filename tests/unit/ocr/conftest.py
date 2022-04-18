import pytest


@pytest.fixture()
def prep_text_detection_and_recognition(prep_ocr_image, prep_spock_config):
    ocr_config = prep_spock_config
    lang = "eng"
    psm = 4
    image = prep_ocr_image
    yield ocr_config, lang, psm, image
    del ocr_config, lang, psm, image
