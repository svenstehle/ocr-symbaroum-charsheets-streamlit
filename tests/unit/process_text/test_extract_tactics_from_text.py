import pytest
from src.process_text import extract_tactics_from_text


@pytest.mark.parametrize(
    "ocr_text, lang, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"), "deu",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_draghul")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"), "deu",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_baiagorn")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"), "deu",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_guard")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"), "eng",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_fairy")
        ),
    ]
)
def test_extract_tactics_from_text(ocr_text, lang, expected_result):
    result = extract_tactics_from_text(ocr_text, lang)
    assert expected_result == result
