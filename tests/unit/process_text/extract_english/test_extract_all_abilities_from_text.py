import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            {
                "Abilities found in text": "Zero"
            },
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            {
                "Bodyguard": "master",
                "Iron Fist": "master",
                "Two-handed Force": "adept"
            },
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            {
                "Acrobatics": "master",
                "Marksman": "master",
                "Sixth Sense": "master",
                "Steadfast": "master"
            },
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            {
                "Brimstone Cascade": "master",
                "Flame Wall": "master"
            },
        ),
    ]
)
def test_extract_all_abilities_from_text(
    ocr_text,
    expected_result,
    create_input_extract_all_attributes_from_text_eng_general,
):
    EE = EnglishExtractor(ocr_text, create_input_extract_all_attributes_from_text_eng_general)
    result = EE.extract_all_abilities_from_text()
    assert expected_result == result
