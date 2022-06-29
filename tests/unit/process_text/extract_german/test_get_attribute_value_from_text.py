import pytest
from src.process_text.extract_german import GermanExtractor


@pytest.mark.parametrize(
    "ocr_text, attribute_result_pair", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("prep_input_result_get_attribute_value_from_text_draghul")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("prep_input_result_get_attribute_value_from_text_baiagorn")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("prep_input_result_get_attribute_value_from_text_guard")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            pytest.lazy_fixture("prep_input_result_get_attribute_value_from_text_aeber")
        )
    ]
)
def test_get_attribute_value_from_text(
    ocr_text,
    attribute_result_pair,
    create_input_extract_all_attributes_from_text_ger_general,
):
    attribute_names = create_input_extract_all_attributes_from_text_ger_general
    GE = GermanExtractor(ocr_text, attribute_names)
    target_attribute, expected_result = attribute_result_pair
    # pylint: disable=protected-access
    assert GE._get_attribute_value_from_text(target_attribute) == expected_result
