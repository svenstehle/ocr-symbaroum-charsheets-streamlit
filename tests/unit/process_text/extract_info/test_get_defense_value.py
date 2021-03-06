import pytest
from src.process_text.extract_info import InformationExtractor

# pylint: disable=protected-access


@pytest.mark.parametrize(
    "attributes, expected_result", [
        (
            pytest.lazy_fixture("create_input_get_defense_value_draghul"),
            "15",
        ),
        (
            pytest.lazy_fixture("create_input_get_defense_value_baiagorn"),
            "7",
        ),
        (
            pytest.lazy_fixture("create_input_get_defense_value_brand"),
            "11",
        ),
        (
            pytest.lazy_fixture("create_input_get_defense_value_fairy"),
            "13",
        ),
    ]
)
def test_get_defense_value(
    attributes,
    expected_result,
):
    IE = InformationExtractor("dummy text")
    # set attributes used by get_defense_value
    IE._attributes = attributes
    defense_value = IE._get_defense_value()
    assert defense_value == expected_result
