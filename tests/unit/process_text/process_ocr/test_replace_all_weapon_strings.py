import pytest
from src.process_text.process_ocr import LanguageNotSupported, TextProcessor

# pylint: disable=protected-access


@pytest.mark.parametrize(
    "text, expected_result", [
        ("das ist ein test wüten test", "das ist ein test wüten test"),
        ("das ist ein test wten test", "das ist ein test wten test"),
        ("das ist ein test waffen test", "das ist ein test waffen test"),
        ("das ist ein test wafden test", "das ist ein test waffen test"),
        ("das ist ein test waddentest", "das ist ein test waffentest"),
        ("das ist ein test wten test", "das ist ein test wten test"),
        (" das ist ein test wten test", " das ist ein test wten test"),
        (" this is a test weapons test", " this is a test weapons test"),
        (" this is a test wehpons test", " this is a test wehpons test"),
        (" this is a test waepons test", " this is a test weapons test"),
        (" this is a test waeons test", " this is a test waeons test"),
        (" this is a test weponstest", " this is a test weponstest"),
        ("this is a test wafons test", "this is a test wafons test"),
        ("das ist ein test willen test", "das ist ein test willen test"),
        ("das ist ein test willen test", "das ist ein test willen test"),
        ("das ist ein test warmen test", "das ist ein test warmen test"),
        ("das ist ein test warmen test", "das ist ein test warmen test"),
    ]
)
def test_replace_all_weapon_strings(text, expected_result):
    TP = TextProcessor(text)
    TP._replace_all_weapon_strings()
    assert TP.text == expected_result


def test_replace_all_weapon_strings_exception():
    TP = TextProcessor("Je parle francais mon amour. Tu aime la souris?")
    lang = "fr"
    with pytest.raises(LanguageNotSupported) as e:
        TP._replace_all_weapon_strings()
    assert str(e.value) == f"Detected language {lang} not supported"
