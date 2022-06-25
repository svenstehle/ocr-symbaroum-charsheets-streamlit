import pytest
from src.process_text.extract_german import GermanExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_draghul"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_baiagorn"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_guard"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_aeber"),
        ),
    ]
)
def test_extract_tactics_from_text(ocr_text, expected_result):
    GE = GermanExtractor(ocr_text)
    tactics = GE.extract_tactics_from_text()
    assert expected_result == tactics
