import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_eng_fairy"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_eng_brand"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_eng_hunter"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_eng_sikander"),
        ),
    ]
)
def test_extract_all_attributes_from_text(
    ocr_text,
    expected_result,
    create_input_extract_all_attributes_from_text_eng_general,
):
    EE = EnglishExtractor(ocr_text, create_input_extract_all_attributes_from_text_eng_general)
    result = EE.extract_all_attributes_from_text()
    assert result == expected_result
