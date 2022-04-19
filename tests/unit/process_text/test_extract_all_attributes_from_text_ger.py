import pytest
from src.process_text import extract_all_attributes_from_text_ger


@pytest.mark.parametrize(
    "ocr_text, attribute_names, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_draghul")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_baiagorn")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_guard")
        ),
    ]
)
def test_extract_all_attributes_from_text_ger(ocr_text, attribute_names, expected_result):
    result = extract_all_attributes_from_text_ger(ocr_text, attribute_names)
    assert result == expected_result
