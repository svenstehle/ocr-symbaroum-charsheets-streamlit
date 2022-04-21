import pytest
from src.process_text import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, tactics_str, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            "Taktik:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_draghul"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            "Taktik:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_baiagorn"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            "Taktik:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_guard"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            "Tactics:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_fairy"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            "Tactics:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_brand"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            "Tactics:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_hunter"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            "Tactics:",
            pytest.lazy_fixture("create_expected_result_extract_tactics_from_text_sikander"),
        ),
    ]
)
def test_extract_tactics_from_text(ocr_text, tactics_str, expected_result):
    IE = InformationExtractor(ocr_text)
    assert expected_result == IE.extract_tactics_from_text(tactics_str)
    assert expected_result == IE.tactics
