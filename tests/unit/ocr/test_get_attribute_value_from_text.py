from src.ocr import get_attribute_value_from_text


def test_get_attribute_value_from_text(prep_get_attribute_value_from_text):
    text, target_attribute, expected_result = prep_get_attribute_value_from_text
    assert get_attribute_value_from_text(text, target_attribute) == expected_result
