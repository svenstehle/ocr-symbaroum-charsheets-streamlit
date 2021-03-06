import pytest
from src.process_text.extract_german import GermanExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            {
                "Eisenfaust": "Adept",
                "Schildkampf": "Novize",
                "Testskill": "Meister",
            },
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            {
                "Berserkerrausch": "Adept"
            },
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            {
                "Abilities found in text": "Zero"
            },
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            {
                "Eisenfaust": "Adept"
            },
        ),
    ]
)
def test_extract_all_abilities_from_text(
    ocr_text,
    expected_result,
    create_input_extract_all_attributes_from_text_ger_general,
):
    attribute_names = create_input_extract_all_attributes_from_text_ger_general
    GE = GermanExtractor(ocr_text, attribute_names)
    result = GE.extract_all_abilities_from_text()
    assert expected_result == result
