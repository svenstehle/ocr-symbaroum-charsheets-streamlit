import pytest
from src.process_text.extract_info import InformationExtractor

# pylint: disable=protected-access


@pytest.mark.parametrize(
    "ocr_text, attributes, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_transform_attribute_keys_to_english_longhand_draghul"),
            pytest.lazy_fixture("create_expected_result_transform_attribute_keys_to_english_longhand_draghul"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_transform_attribute_keys_to_english_longhand_baiagorn"),
            pytest.lazy_fixture("create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_transform_attribute_keys_to_english_longhand_brand"),
            pytest.lazy_fixture("create_expected_result_transform_attribute_keys_to_english_longhand_brand"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_transform_attribute_keys_to_english_longhand_fairy"),
            pytest.lazy_fixture("create_expected_result_transform_attribute_keys_to_english_longhand_fairy"),
        ),
    ]
)
def test_transform_attribute_keys_to_english_longhand(
    ocr_text,
    attributes,
    expected_result,
):
    IE = InformationExtractor(ocr_text)
    # set attributes used by get_attack_value
    assert IE._attributes == {"Attributes not found in text": "Zero"}
    IE._transform_attribute_keys_to_english_longhand(attributes)
    assert expected_result == IE._attributes == IE.attributes


def test_transform_attribute_keys_to_english_longhand_not_supported_language(
    prep_transform_attribute_keys_to_english_longhand_not_supported_language
):
    text, attributes = prep_transform_attribute_keys_to_english_longhand_not_supported_language
    IE = InformationExtractor(text)
    with pytest.raises(ValueError):
        IE._transform_attribute_keys_to_english_longhand(attributes)
