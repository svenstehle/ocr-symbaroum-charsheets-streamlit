import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "attribute_values, expected_result", [
        (
            ["0", "0", "-5", "41", "-3", "+3", "+5", "-1"],
            ["0", "0", "-5", "+1", "-3", "+3", "+5", "-1"],
        ),
        (
            ["-3", "+43", "+1", "+5", "-1", "0", "-5", "0"],
            ["-3", "+3", "+1", "+5", "-1", "0", "-5", "0"],
        ),
        (
            ["45", "0", "0", "43", "-1", "-6", "4+1", "-8"],
            ["+5", "0", "0", "+3", "-1", "-6", "+1", "-8"],
        ),
        (
            ["+41", "-1", "+45", "0", "-3", "-5", "4+3", "0"],
            ["+1", "-1", "+5", "0", "-3", "-5", "+3", "0"],
        ),
        (
            ["+44", "-2", "++5", "0", "-2", "-6", "4++3", "+1"],
            ["+4", "-2", "+5", "0", "-2", "-6", "+3", "+1"],
        ),
    ]
)
def test_clean_misrecognized_plus_characters(
    attribute_values,
    expected_result,
    create_input_extract_all_attributes_from_text_eng_general,
):
    # pylint: disable=protected-access
    EE = EnglishExtractor("dummy_text", create_input_extract_all_attributes_from_text_eng_general)
    result = EE._clean_misrecognized_plus_characters(attribute_values)
    assert expected_result == result
