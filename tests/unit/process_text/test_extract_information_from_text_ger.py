from typing import Dict

import pytest
from src.process_text import extract_information_from_text_ger

# TODO add tests for eng chars


@pytest.mark.parametrize(
    "ocr_text, attribute_names, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_expected_result_extract_information_from_text_ger")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_expected_result_extract_information_from_text_ger")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_expected_result_extract_information_from_text_ger")
        ),
    ]
)
def test_extract_information_from_text_ger(ocr_text, attribute_names, expected_result):
    result = extract_information_from_text_ger(ocr_text, attribute_names, "dummyname")
    assert result.keys() == expected_result.keys()
    assert isinstance(result["abilities"], Dict)
    assert isinstance(result["tactics"], str)
    assert isinstance(result["setattr_str"], str)
