import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, prep_create_token_mod_str", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("prep_create_token_mod_str_draghul"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("prep_create_token_mod_str_baiagorn"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("prep_create_token_mod_str_brand"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("prep_create_token_mod_str_fairy"),
        ),
    ]
)
def test_create_token_mod_str(
    ocr_text,
    prep_create_token_mod_str,
):
    IE = InformationExtractor(ocr_text)
    attributes, equipment, armor, expected_result = prep_create_token_mod_str
    IE._attributes = attributes    # pylint: disable=protected-access
    IE._equipment = equipment    # pylint: disable=protected-access
    IE._armor = armor    # pylint: disable=protected-access
    # assert defaults
    assert IE._token_mod_str == ""    # pylint: disable=protected-access
    assert IE.token_mod_str == ""
    IE.create_token_mod_str()
    assert IE._token_mod_str == expected_result    # pylint: disable=protected-access
    assert IE.token_mod_str == expected_result
