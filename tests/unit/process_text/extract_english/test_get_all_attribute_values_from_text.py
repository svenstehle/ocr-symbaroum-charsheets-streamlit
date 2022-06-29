import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            ["10", "10", "15", "9", "13", "7", "5", "11"],
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            ["13", "7", "9", "5", "11", "10", "15", "10"],
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            ["5", "10", "10", "7", "11", "16", "9", "18"],
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            ["9", "11", "5", "10", "13", "15", "7", "10"],
        ),
    ]
)
def test_get_all_attribute_values_from_text(
    ocr_text,
    expected_result,
    create_input_extract_all_attributes_from_text_eng_general,
):
    # pylint: disable=protected-access
    EE = EnglishExtractor(ocr_text, create_input_extract_all_attributes_from_text_eng_general)
    assert EE._get_all_attribute_values_from_text() == expected_result
