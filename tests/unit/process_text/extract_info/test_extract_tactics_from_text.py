import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, tactics_str, expected_result", [
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
    ]
)
def test_extract_tactics_from_text(ocr_text, tactics_str, expected_result):
    IE = InformationExtractor(ocr_text)
    assert IE._tactics == ""    # pylint: disable=protected-access
    assert IE.tactics == ""
    IE.extract_tactics_from_text(tactics_str)
    assert expected_result == IE.tactics == IE._tactics    # pylint: disable=protected-access
