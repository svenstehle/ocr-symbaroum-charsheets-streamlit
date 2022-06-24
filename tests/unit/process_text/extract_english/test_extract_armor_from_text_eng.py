import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_expected_result_extract_armor_from_text_eng_fairy")
        ),
    ]
)
def test_extract_armor_from_text_eng(ocr_text, expected_result):
    EE = EnglishExtractor(ocr_text)
    result = EE.extract_armor_from_text_eng()
    assert expected_result == result
