from typing import Dict

import pytest
from src.process_text import InformationExtractor

# TODO add tests for extract_information_from_text_eng and extract_information_from_text


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
def test_extract_information_from_ger_text(ocr_text, attribute_names, expected_result):
    IE = InformationExtractor(ocr_text)
    IE.extract_information_from_ger_text("dummyname", attribute_names)
    assert isinstance(IE.attributes, Dict)
    assert isinstance(IE.abilities, Dict)
    assert isinstance(IE.tactics, str)
    assert isinstance(IE.setattr_str, str)
