import pytest
from src.process_text.extract_german import GermanExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            "1w10 orteg",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            "keine",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            "1w10 schillinge, kautabak",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            "keine",
        ),
    ]
)
def test_extract_equipment_from_text(
    ocr_text,
    expected_result,
    create_input_extract_all_attributes_from_text_ger_general,
):
    attribute_names = create_input_extract_all_attributes_from_text_ger_general
    GE = GermanExtractor(ocr_text, attribute_names)
    result = GE.extract_equipment_from_text()
    assert expected_result == result
