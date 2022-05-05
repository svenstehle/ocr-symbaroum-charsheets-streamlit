import pytest
from src.process_language import detect_languages


# pylint: disable=duplicate-code
@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (pytest.lazy_fixture("prep_ocr_text_draghul"), "de"),
        (pytest.lazy_fixture("prep_ocr_text_baiagorn"), "de"),
        (pytest.lazy_fixture("prep_ocr_text_guard"), "de"),
        (pytest.lazy_fixture("prep_ocr_text_aeber"), "de"),
        (pytest.lazy_fixture("prep_ocr_text_fairy"), "en"),
        (pytest.lazy_fixture("prep_ocr_text_brand"), "en"),
        (pytest.lazy_fixture("prep_ocr_text_hunter"), "en"),
        (pytest.lazy_fixture("prep_ocr_text_sikander"), "en"),
    ]
)
def test_detect_languages(ocr_text, expected_result):
    languages = detect_languages(ocr_text)
    assert len(languages) == 1
    assert languages[0] == expected_result
