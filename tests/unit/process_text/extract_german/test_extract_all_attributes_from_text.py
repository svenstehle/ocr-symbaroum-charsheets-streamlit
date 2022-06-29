import pytest
from src.process_text.extract_german import GermanExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_draghul")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_baiagorn")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_guard")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            pytest.lazy_fixture("create_expected_result_extract_all_attributes_from_text_aeber")
        ),
    ]
)
def test_extract_all_attributes_from_text(
    ocr_text,
    expected_result,
    create_input_extract_all_attributes_from_text_ger_general,
):
    attribute_names = create_input_extract_all_attributes_from_text_ger_general
    GE = GermanExtractor(ocr_text, attribute_names)
    result = GE.extract_all_attributes_from_text()
    assert result == expected_result
