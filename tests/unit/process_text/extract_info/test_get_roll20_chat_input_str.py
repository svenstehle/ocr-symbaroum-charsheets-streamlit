import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "charname, ocr_text, attributes, expected_result", [
        (
            "Gandalf",
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_draghul"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_draghul"),
        ),
        (
            "Legolas",
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_baiagorn"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_baiagorn"),
        ),
        (
            "Hulk",
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_brand"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_brand"),
        ),
        (
            "Captain Marvel",
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_fairy"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_fairy"),
        ),
    ]
)
def test_get_roll20_chat_input_str(charname, ocr_text, attributes, expected_result):
    IE = InformationExtractor(ocr_text)
    IE._attributes = attributes    # pylint: disable=protected-access
    IE.get_roll20_chat_input_str(charname)
    assert expected_result == IE.setattr_str


def test_get_roll20_chat_input_str_not_supported_language(prep_get_roll20_chat_input_str_not_supported_language):
    text, charname, attributes = prep_get_roll20_chat_input_str_not_supported_language
    IE = InformationExtractor(text)
    IE._attributes = attributes    # pylint: disable=protected-access
    with pytest.raises(ValueError):
        IE.get_roll20_chat_input_str(charname)