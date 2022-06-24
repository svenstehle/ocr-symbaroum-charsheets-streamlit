from typing import Dict

import pytest
from src.process_text.extract_info import InformationExtractor

# pylint: disable=duplicate-code


@pytest.mark.parametrize(
    "ocr_text, config, lang", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("prep_hydra_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("prep_hydra_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("prep_hydra_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            pytest.lazy_fixture("prep_hydra_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("prep_hydra_config"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("prep_hydra_config"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            pytest.lazy_fixture("prep_hydra_config"),
            "en",
        ),
    ]
)
def test_extract_information_from_text(ocr_text, config, lang):
    IE = InformationExtractor(ocr_text)
    IE.extract_information_from_text("dummyname", config)
    assert IE.lang == lang
    assert isinstance(IE.attributes, Dict)
    assert isinstance(IE.abilities, Dict)
    assert isinstance(IE.tactics, str)

    assert isinstance(IE.equipment, str)
    assert len(IE.equipment) > 3

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
    with pytest.raises(ValueError):
        IE.extract_information_from_text("dummyname", prep_hydra_config)
    assert IE.lang == "fr"
