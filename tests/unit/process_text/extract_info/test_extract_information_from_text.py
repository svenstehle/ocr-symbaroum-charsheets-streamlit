from typing import Dict

import pytest
from src.process_text.extract_info import InformationExtractor
from src.process_text.process_ocr import LanguageNotSupported

# pylint: disable=duplicate-code
# pylint: disable=protected-access


@pytest.mark.parametrize(
    "ocr_text, config, lang", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul_raw"),
            pytest.lazy_fixture("prep_hydra_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn_raw"),
            pytest.lazy_fixture("prep_hydra_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard_raw"),
            pytest.lazy_fixture("prep_hydra_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber_raw"),
            pytest.lazy_fixture("prep_hydra_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy_raw"),
            pytest.lazy_fixture("prep_hydra_config"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand_raw"),
            pytest.lazy_fixture("prep_hydra_config"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander_raw"),
            pytest.lazy_fixture("prep_hydra_config"),
            "en",
        ),
    ]
)
def test_extract_information_from_text(ocr_text, config, lang):
    IE = InformationExtractor(ocr_text)
    # assert setup is correct
    assert IE.text == ocr_text
    assert IE._abilities == {"Abilities not found in text": "Zero"}
    assert IE._attributes == {"Attributes not found in text": "Zero"}
    assert IE._equipment == ""
    assert IE._armor == ""
    assert IE._traits == ""
    assert IE._tactics == ""
    assert IE._setattr_name_str == ""
    assert IE._setattr_sel_str == ""
    assert IE._token_mod_str == ""
    assert IE._lang == ""

    # run the extraction and check state
    IE.extract_information_from_text("dummyname", config)
    assert IE.lang == lang
    assert isinstance(IE.attributes, Dict)
    assert isinstance(IE.abilities, Dict)
    assert isinstance(IE.tactics, str)

    assert isinstance(IE.equipment, str)
    assert len(IE.equipment) > 3

    assert isinstance(IE._armor, str)
    assert len(IE._armor) > 0

    assert isinstance(IE.setattr_name_str, str)
    assert len(IE.setattr_name_str) > 30

    assert isinstance(IE.setattr_sel_str, str)
    assert len(IE.setattr_sel_str) > 30

    assert isinstance(IE.token_mod_str, str)
    assert len(IE.token_mod_str) > 30


def test_extract_information_from_text_exception(
    prep_ocr_text_unknown_language,
    prep_hydra_config,
):
    IE = InformationExtractor(prep_ocr_text_unknown_language)
    with pytest.raises(LanguageNotSupported) as e:
        IE.extract_information_from_text("dummyname", prep_hydra_config)
    assert str(e.value) == "Detected language fr not supported"
    assert IE._lang == "fr"
