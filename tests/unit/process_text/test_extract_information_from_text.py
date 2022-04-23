from typing import Dict

import pytest
from src.process_text import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, config, lang", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("prep_spock_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("prep_spock_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("prep_spock_config"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("prep_spock_config"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("prep_spock_config"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            pytest.lazy_fixture("prep_spock_config"),
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
    assert isinstance(IE.setattr_str, str)


def test_extract_information_from_text_exception(
    prep_ocr_text_unknown_language,
    prep_spock_config,
):
    IE = InformationExtractor(prep_ocr_text_unknown_language)
    with pytest.raises(ValueError):
        IE.extract_information_from_text("dummyname", prep_spock_config)
    assert IE.lang == "fr"
