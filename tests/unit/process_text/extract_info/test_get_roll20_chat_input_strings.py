import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "charname, ocr_text, inputs, expected_result_setattr_name, "
    "expected_result_setattr_sel, expected_result_token_mod", [
        (
            "Gandalf",
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_draghul"),
            pytest.lazy_fixture("create_expected_result_setattr_name_str_draghul"),
            pytest.lazy_fixture("create_expected_result_setattr_sel_str_draghul"),
            pytest.lazy_fixture("create_expected_result_create_token_mod_str_draghul"),
        ),
        (
            "Legolas",
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_baiagorn"),
            pytest.lazy_fixture("create_expected_result_setattr_name_str_baiagorn"),
            pytest.lazy_fixture("create_expected_result_setattr_sel_str_baiagorn"),
            pytest.lazy_fixture("create_expected_result_create_token_mod_str_baiagorn"),
        ),
        (
            "Hulk",
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_brand"),
            pytest.lazy_fixture("create_expected_result_setattr_name_str_brand"),
            pytest.lazy_fixture("create_expected_result_setattr_sel_str_brand"),
            pytest.lazy_fixture("create_expected_result_create_token_mod_str_brand"),
        ),
        (
            "Captain Marvel",
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_fairy"),
            pytest.lazy_fixture("create_expected_result_setattr_name_str_fairy"),
            pytest.lazy_fixture("create_expected_result_setattr_sel_str_fairy"),
            pytest.lazy_fixture("create_expected_result_create_token_mod_str_fairy"),
        ),
    ]
)
def test_get_roll20_chat_input_strings(
    charname,
    ocr_text,
    inputs,
    expected_result_setattr_name,
    expected_result_setattr_sel,
    expected_result_token_mod,
):
    IE = InformationExtractor(ocr_text)
    attributes, equipment, armor = inputs
    IE._attributes = attributes    # pylint: disable=protected-access
    IE._equipment = equipment    # pylint: disable=protected-access
    IE._armor = armor    # pylint: disable=protected-access
    IE.get_roll20_chat_input_strings(charname)
    assert expected_result_setattr_name == IE.setattr_name_str
    assert expected_result_setattr_sel == IE.setattr_sel_str
    assert expected_result_token_mod == IE.token_mod_str
