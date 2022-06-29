import pytest
from src.process_text.extract_info import InformationExtractor

# pylint: disable=protected-access


@pytest.mark.parametrize(
    "prep_create_token_mod_str", [
        pytest.lazy_fixture("prep_create_token_mod_str_draghul"),
        pytest.lazy_fixture("prep_create_token_mod_str_baiagorn"),
        pytest.lazy_fixture("prep_create_token_mod_str_brand"),
        pytest.lazy_fixture("prep_create_token_mod_str_fairy"),
    ]
)
def test_create_token_mod_str(prep_create_token_mod_str):
    IE = InformationExtractor("dummy text")
    attributes, equipment, armor, abilities, traits, expected_result = prep_create_token_mod_str
    IE._attributes = attributes
    IE._abilities = abilities
    IE._equipment = equipment
    IE._armor = armor
    IE._traits = traits

    # assert defaults
    assert IE._token_mod_str == ""
    assert IE.token_mod_str == ""

    IE._create_token_mod_str()
    assert IE._token_mod_str == expected_result
    assert IE.token_mod_str == expected_result
