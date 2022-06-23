import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, attributes, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_create_token_mod_str_draghul"),
            pytest.lazy_fixture("create_expected_result_create_token_mod_str_draghul"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_create_token_mod_str_baiagorn"),
            pytest.lazy_fixture("create_expected_result_create_token_mod_str_baiagorn"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_create_token_mod_str_brand"),
            pytest.lazy_fixture("create_expected_result_create_token_mod_str_brand"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_create_token_mod_str_fairy"),
            pytest.lazy_fixture("create_expected_result_create_token_mod_str_fairy"),
        ),
    ]
)
def test_create_token_mod_str(
    ocr_text,
    attributes,
    expected_result,
):
    IE = InformationExtractor(ocr_text)
    # set attributes used by create_token_mod_str
    IE._attributes = attributes    # pylint: disable=protected-access
    # assert defaults
    assert IE._token_mod_str == ""    # pylint: disable=protected-access
    assert IE.token_mod_str == ""
    IE.create_token_mod_str()
    assert IE._token_mod_str == expected_result    # pylint: disable=protected-access
    assert IE.token_mod_str == expected_result
