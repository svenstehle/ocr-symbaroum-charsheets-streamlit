import pytest
from src.process_text import get_all_attribute_values_from_text_eng


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_expected_result_get_all_attribute_values_from_text_eng_fairy"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_expected_result_get_all_attribute_values_from_text_eng_brand"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            pytest.lazy_fixture("create_expected_result_get_all_attribute_values_from_text_eng_hunter"),
        ),
    ]
)
def test_get_all_attribute_values_from_text_eng(ocr_text, expected_result):
    assert get_all_attribute_values_from_text_eng(ocr_text) == expected_result
