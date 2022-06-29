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
def test_capitalize_ability_name(
    ability_name,
    expected_result,
    create_input_extract_all_attributes_from_text_eng_general,
):
    # pylint: disable=protected-access
    attribute_names = create_input_extract_all_attributes_from_text_eng_general
    EE = EnglishExtractor("dummy_text", attribute_names)
    result = EE._capitalize_ability_name(ability_name)
    assert expected_result == result
