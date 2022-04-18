from src.process_text import get_roll20_chat_input_str


def test_get_roll20_chat_input_str(prep_get_roll20_chat_input_str):
    charname, attributes, expected_result = prep_get_roll20_chat_input_str
    result = get_roll20_chat_input_str(charname, attributes)
    assert expected_result == result
