import pytest


@pytest.fixture()
def prep_text_detection_and_recognition(prep_ocr_image, prep_spock_config):
    image = prep_ocr_image
    ocr_config = prep_spock_config
    yield ocr_config, image
    del ocr_config, image
