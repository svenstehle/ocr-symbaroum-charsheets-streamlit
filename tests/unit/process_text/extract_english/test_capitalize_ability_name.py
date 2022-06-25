import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "ability_name, expected_result", [
        ("bodyguard", "Bodyguard"),
        ("iron fist", "Iron Fist"),
        ("two-handed force", "Two-handed Force"),
        ("sixth sense", "Sixth Sense"),
        ("brimstone cascade", "Brimstone Cascade"),
    ]
)
def test_capitalize_ability_name(ability_name, expected_result):
    # pylint: disable=protected-access
    EE = EnglishExtractor("dummy_text")
    result = EE._capitalize_ability_name(ability_name)
    assert expected_result == result
