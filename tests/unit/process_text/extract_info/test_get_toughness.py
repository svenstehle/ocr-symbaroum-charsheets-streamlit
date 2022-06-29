import pytest
from src.process_text.extract_info import InformationExtractor

# pylint: disable=protected-access


@pytest.mark.parametrize(
    "attributes, expected_result", [
        (
            {
                "strong": "15"
            },
            15,
        ),
        (
            {
                "strong": "11"
            },
            11,
        ),
        (
            {
                "strong": "10"
            },
            10,
        ),
        (
            {
                "strong": "9"
            },
            10,
        ),
        (
            {
                "strong": "3"
            },
            10,
        ),
    ]
)
def test_get_toughness(attributes, expected_result):
    result = InformationExtractor._get_toughness(attributes)
    assert expected_result == result
