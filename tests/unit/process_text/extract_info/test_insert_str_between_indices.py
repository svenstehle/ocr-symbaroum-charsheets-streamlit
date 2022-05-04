import pytest
from src.process_text.extract_info import insert_str_between_indices


@pytest.mark.parametrize(
    "text, string, start, end, expected_result", [
        ("test wüten test", "waffen", 5, 10, "test waffen test"),
        ("test wten test", "waffen", 5, 9, "test waffen test"),
        ("tes waffen test", "waffen", 4, 10, "tes waffen test"),
        ("teste wafden test", "waffen", 6, 12, "teste waffen test"),
        ("test waddentest", "waffen", 5, 11, "test waffentest"),
        ("test wten test", "ohlala", 0, 4, "ohlala wten test"),
        (" test wten test", "ohlala", 0, 4, "ohlalat wten test"),
    ]
)
def test_insert_str_between_indices(text, string, start, end, expected_result):
    result = insert_str_between_indices(text, string, start, end)
    assert result == expected_result
