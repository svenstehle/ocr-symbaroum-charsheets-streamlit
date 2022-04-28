import pytest
from src.process_text.extract_english import EnglishExtractor


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
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            pytest.lazy_fixture("create_expected_result_get_all_attribute_values_from_text_eng_sikander"),
        ),
    ]
)
def test_get_all_attribute_values_from_text_eng(ocr_text, expected_result):
    EE = EnglishExtractor(ocr_text)
    assert EE.get_all_attribute_values_from_text_eng() == expected_result
