from src.ocr import OCR
from tests.testing_utils import replace_ubuntu_specific_characters


def test_repeat_ocr_if_only_one_language_present_with_one_language(create_ocr_test_setup):
    cfg, image, psm = create_ocr_test_setup
    ocr = OCR(cfg, image, psm)
    expected_result = "Das ist ein Test\n"
    assert ocr.text == "EMPTY DUMMY: OCR was not yet performed!"
    ocr.lang = "deu"
    ocr.repeat_ocr_if_only_one_language_present()
    out = replace_ubuntu_specific_characters(ocr.text)
    assert out == expected_result


def test_repeat_ocr_if_only_one_language_present_with_two_languages(create_ocr_test_setup):
    cfg, image, psm = create_ocr_test_setup
    ocr = OCR(cfg, image, psm)
    expected_result = "EMPTY DUMMY: OCR was not yet performed!"
    assert ocr.text == expected_result
    assert ocr.lang == "deu+eng"
    ocr.repeat_ocr_if_only_one_language_present()
    out = replace_ubuntu_specific_characters(ocr.text)
    assert out == expected_result
