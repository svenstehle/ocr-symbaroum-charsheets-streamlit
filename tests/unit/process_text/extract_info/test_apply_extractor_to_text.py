from typing import Dict

import pytest
from src.process_text.extract_english import EnglishExtractor
from src.process_text.extract_german import GermanExtractor
from src.process_text.extract_info import InformationExtractor

# pylint: disable=duplicate-code
# pylint: disable=protected-access


@pytest.mark.parametrize(
    "ocr_text, lang, attribute_names", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            "en",
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            "en",
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            "en",
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            "de",
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            "de",
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            "de",
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            "de",
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
        ),
    ]
)
def test_apply_extractor_to_text(ocr_text, lang, attribute_names):
    IE = InformationExtractor(ocr_text)
    assert IE._lang == ""
    if lang == "en":
        extractor = EnglishExtractor(IE.text, attribute_names)
    elif lang == "de":
        extractor = GermanExtractor(IE.text, attribute_names)
    else:
        raise ValueError("Wrong test setup")

    IE._apply_extractor_to_text(extractor, "dummyname")
    assert isinstance(IE.attributes, Dict)
    assert IE.attributes == IE._attributes
    assert isinstance(IE.abilities, Dict)
    assert IE.abilities == IE.abilities
    assert isinstance(IE.tactics, str)
    assert IE.tactics == IE._tactics

    assert isinstance(IE.equipment, str)
    assert len(IE.equipment) > 3
    assert IE.equipment == IE._equipment

    assert isinstance(IE.setattr_name_str, str)
    assert len(IE.setattr_name_str) > 30
    assert IE.setattr_name_str == IE._setattr_name_str

    assert isinstance(IE.setattr_sel_str, str)
    assert len(IE.setattr_sel_str) > 30
    assert IE.setattr_sel_str == IE._setattr_sel_str

    assert isinstance(IE.token_mod_str, str)
    assert len(IE.token_mod_str) > 30
    assert IE.token_mod_str == IE._token_mod_str
