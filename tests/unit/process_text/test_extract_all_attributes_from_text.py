from src.process_text import extract_all_attributes_from_text


def test_extract_all_attributes_from_text(prep_extract_all_attributes_from_text):
    text, attribute_names, expected_result = prep_extract_all_attributes_from_text
    result = extract_all_attributes_from_text(text, attribute_names)
    assert result == expected_result
