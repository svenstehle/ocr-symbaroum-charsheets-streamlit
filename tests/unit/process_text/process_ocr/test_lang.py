import pytest
from src.process_text.process_ocr import LanguageNotSupported, TextProcessor

# pylint: disable=protected-access


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
    IE = TextProcessor(ocr_text)
    assert IE._lang == ""
    assert IE.lang == lang
    assert IE._lang == lang


def test_lang_exception(prep_ocr_text_unknown_language):
    IE = TextProcessor(prep_ocr_text_unknown_language)
    lang = "fr"
    assert IE._lang == ""
    with pytest.raises(LanguageNotSupported) as e:
        assert IE.lang == lang
    assert str(e.value) == f"Detected language {lang} not supported"
    assert IE._lang == lang
