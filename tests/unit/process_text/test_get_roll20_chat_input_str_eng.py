import pytest
from src.process_text import get_roll20_chat_input_str_eng


@pytest.mark.parametrize(
    "charname, attributes, expected_result", [
        (
            "Captain Marvel",
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_fairy"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_fairy"),
        ),
        (
            "Hulk",
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_brand"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_brand"),
        ),
    ]
)
def test_get_roll20_chat_input_str_eng(charname, attributes, expected_result):
    result = get_roll20_chat_input_str_eng(charname, attributes)
    assert expected_result == result
