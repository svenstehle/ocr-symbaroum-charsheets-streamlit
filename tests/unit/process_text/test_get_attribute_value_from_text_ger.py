import pytest
from src.process_text import GermanExtractor


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
        )
    ]
)
def test_get_attribute_value_from_text_ger(ocr_text, attribute_result_pair):
    GE = GermanExtractor(ocr_text)
    target_attribute, expected_result = attribute_result_pair
    assert GE.get_attribute_value_from_text_ger(target_attribute) == expected_result
