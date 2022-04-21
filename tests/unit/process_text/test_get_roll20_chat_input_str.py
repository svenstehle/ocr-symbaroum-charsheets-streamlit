import pytest
from src.process_text import TextProcessor


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
    TP = TextProcessor(ocr_text)
    result = TP.get_roll20_chat_input_str(charname, attributes)
    assert expected_result == result


def test_get_roll20_chat_input_str_not_supported_language(prep_get_roll20_chat_input_str_not_supported_language):
    text, charname, attributes = prep_get_roll20_chat_input_str_not_supported_language
    TP = TextProcessor(text)
    with pytest.raises(ValueError):
        TP.get_roll20_chat_input_str(charname, attributes)
