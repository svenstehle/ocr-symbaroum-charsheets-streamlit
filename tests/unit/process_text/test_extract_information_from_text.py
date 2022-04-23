from typing import Dict

import pytest
from src.process_text import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, attribute_names_ger, attribute_names_eng, lang", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_ger_general"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            "en",
        ),
    ]
)
def test_extract_information_from_text(ocr_text, attribute_names_ger, attribute_names_eng, lang):
    IE = InformationExtractor(ocr_text)
    IE.extract_information_from_text("dummyname", attribute_names_ger, attribute_names_eng)
    assert IE.lang == lang
    assert isinstance(IE.attributes, Dict)
    assert isinstance(IE.abilities, Dict)
    assert isinstance(IE.tactics, str)
    assert isinstance(IE.setattr_str, str)


def test_extract_information_from_text_exception(
    prep_ocr_text_unknown_language,
    create_input_extract_all_attributes_from_text_ger_general,
    create_input_extract_all_attributes_from_text_eng_general,
):
    IE = InformationExtractor(prep_ocr_text_unknown_language)
    with pytest.raises(ValueError):
        IE.extract_information_from_text(
            "dummyname",
            create_input_extract_all_attributes_from_text_ger_general,
            create_input_extract_all_attributes_from_text_eng_general,
        )
    assert IE.lang == "fr"
