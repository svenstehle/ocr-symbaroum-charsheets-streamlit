from src.ocr import extract_tactics_from_text


def test_extract_tactics_from_text(prep_extract_tactics_from_text):
    text, expected_result = prep_extract_tactics_from_text
    result = extract_tactics_from_text(text)
    assert expected_result == result
