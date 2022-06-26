import pytest
from src.process_text.process_ocr import TextProcessor


@pytest.mark.parametrize(
    "ocr_text, start_token, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            "tactics:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_fairy"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            "tactics:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_brand"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            "tactics:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_hunter"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            "tactics:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_sikander"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            "taktik:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_draghul"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            "taktik:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_baiagorn"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            "taktik:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_guard"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            "taktik:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_aeber"),
        ),
    ]
)
def test_extract_from_start_token_until_end(ocr_text, start_token, expected_result):
    TP = TextProcessor(ocr_text)
    # pylint: disable=protected-access
    result = TP._extract_from_start_token_until_end(start_token)
    assert expected_result == result
