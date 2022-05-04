import pytest
from src.process_text.extract_info import replace_all_weapon_strings


@pytest.mark.parametrize(
    "text, string, expected_result", [
        ("test wüten test", "waffen", "test wüten test"),
        ("test wten test", "waffen", "test wten test"),
        ("tes waffen test", "waffen", "tes waffen test"),
        ("teste wafden test", "waffen", "teste waffen test"),
        ("test waddentest", "waffen", "test waffentest"),
        ("test wten test", "waffen", "test wten test"),
        (" test wten test", "waffen", " test wten test"),
        (" test weapons test", "weapons", " test weapons test"),
        (" test wehpons test", "weapons", " test wehpons test"),
        (" test waepons test", "weapons", " test weapons test"),
        (" test waeons test", "weapons", " test waeons test"),
        (" test weponstest", "weapons", " test weponstest"),
        ("test wafons test", "weapons", "test wafons test"),
        ("test willen test", "weapons", "test willen test"),
        ("test willen test", "waffen", "test willen test"),
        ("test warmen test", "weapons", "test warmen test"),
        ("test warmen test", "waffen", "test warmen test"),
    ]
)
def test_replace_all_weapon_strings(text, string, expected_result):
    result = replace_all_weapon_strings(text, string)
    assert result == expected_result
