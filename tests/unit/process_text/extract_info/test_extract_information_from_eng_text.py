from typing import Dict

import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, attribute_names", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
        ),
    ]
)
def test_extract_information_from_eng_text(ocr_text, attribute_names):
    IE = InformationExtractor(ocr_text)
    IE.extract_information_from_eng_text("dummyname", attribute_names)
    assert isinstance(IE.attributes, Dict)
    assert isinstance(IE.abilities, Dict)
    assert isinstance(IE.tactics, str)
    assert isinstance(IE.setattr_sel_str, str)
    assert isinstance(IE.setattr_name_str, str)
