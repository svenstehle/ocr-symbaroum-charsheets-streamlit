import pytest
from src.process_text import get_roll20_chat_input_str

#TODO add tests for eng chars


@pytest.mark.parametrize(
    "charname, attributes, expected_result", [
        (
            "Gandalf",
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_draghul"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_draghul"),
        ),
        (
            "Legolas",
            pytest.lazy_fixture("create_input_get_roll20_chat_input_str_baiagorn"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_baiagorn"),
        ),
    ]
)
def test_get_roll20_chat_input_str(charname, attributes, expected_result):
    result = get_roll20_chat_input_str(charname, attributes)
    assert expected_result == result
