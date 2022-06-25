import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "attribute_values, expected_result", [
        (
            ["0", "0", "-5", "+1", "-3", "+3", "+5", "-1"],
            ["10", "10", "15", "9", "13", "7", "5", "11"],
        ),
        (
            ["-3", "+3", "+1", "+5", "-1", "0", "-5", "0"],
            ["13", "7", "9", "5", "11", "10", "15", "10"],
        ),
        (
            ["+5", "0", "0", "+3", "-1", "-6", "+1", "-8"],
            ["5", "10", "10", "7", "11", "16", "9", "18"],
        ),
        (
            ["+1", "-1", "+5", "0", "-3", "-5", "+3", "0"],
            ["9", "11", "5", "10", "13", "15", "7", "10"],
        ),
        (
            ["+4", "-2", "+5", "0", "-2", "-6", "+3", "+1"],
            ["6", "12", "5", "10", "12", "16", "7", "9"],
        ),
    ]
)
def test_express_attributes_as_decimal(attribute_values, expected_result):
    # pylint: disable=protected-access
    EE = EnglishExtractor("dummy_text")
    result = EE._express_attributes_as_decimal(attribute_values)
    assert expected_result == result
