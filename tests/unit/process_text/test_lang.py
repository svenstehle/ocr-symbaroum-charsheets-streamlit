import pytest
from src.process_text import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, lang", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            "de",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            "en",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            "en",
        ),
    ]
)
def test_lang(ocr_text, lang):
    IE = InformationExtractor(ocr_text)
    assert IE._lang == ""    # pylint: disable=protected-access
    assert IE.lang == lang
    assert IE._lang == lang    # pylint: disable=protected-access
