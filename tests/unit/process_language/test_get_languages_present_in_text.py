import pytest
from src.process_language import get_languages_present_in_text


# pylint: disable=duplicate-code
@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (pytest.lazy_fixture("prep_ocr_text_draghul"), "deu"),
        (pytest.lazy_fixture("prep_ocr_text_baiagorn"), "deu"),
        (pytest.lazy_fixture("prep_ocr_text_guard"), "deu"),
        (pytest.lazy_fixture("prep_ocr_text_aeber"), "deu"),
        (pytest.lazy_fixture("prep_ocr_text_fairy"), "eng"),
        (pytest.lazy_fixture("prep_ocr_text_brand"), "eng"),
        (pytest.lazy_fixture("prep_ocr_text_hunter"), "eng"),
        (pytest.lazy_fixture("prep_ocr_text_sikander"), "eng"),
        (pytest.lazy_fixture("prep_ocr_text_mixed_language"), "eng+deu"),
    ]
)
def test_get_languages_present_in_text(ocr_text, expected_result):
    assert get_languages_present_in_text(ocr_text) == expected_result
