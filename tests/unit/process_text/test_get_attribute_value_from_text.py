import pytest
from src.process_text import get_attribute_value_from_text


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
def test_get_attribute_value_from_text(ocr_text, attribute_result_pair):
    target_attribute, expected_result = attribute_result_pair
    assert get_attribute_value_from_text(ocr_text, target_attribute) == expected_result
