import pytest
from src.process_text import extract_tactics_from_text


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_draghul")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_baiagorn")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_guard")
        ),
    ]
)
def test_extract_tactics_from_text(ocr_text, expected_result):
    result = extract_tactics_from_text(ocr_text)
    assert expected_result == result
