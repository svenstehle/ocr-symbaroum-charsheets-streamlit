import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "ocr_text, attribute_names, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_eng_fairy"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_eng_brand"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_eng_hunter"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            pytest.lazy_fixture("create_input_extract_all_attributes_from_text_eng_general"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_eng_sikander"),
        ),
    ]
)
def test_extract_all_attributes_from_text_eng(ocr_text, attribute_names, expected_result):
    EE = EnglishExtractor(ocr_text)
    result = EE.extract_all_attributes_from_text_eng(attribute_names)
    assert result == expected_result
