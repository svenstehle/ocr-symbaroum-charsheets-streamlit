from src.ocr import get_all_attribute_names_values_from_text


def test_get_all_attribute_names_values_from_text(prep_get_all_attribute_names_values_from_text):
    text, attribute_names, expected_result = prep_get_all_attribute_names_values_from_text
    result = get_all_attribute_names_values_from_text(text, attribute_names)
    assert result == expected_result
