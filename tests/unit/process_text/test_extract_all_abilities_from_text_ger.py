import pytest
from src.process_text import GermanExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_expected_result_extract_all_abilities_from_text_draghul")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_expected_result_extract_all_abilities_from_text_baiagorn")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            pytest.lazy_fixture("create_expected_result_extract_all_abilities_from_text_guard")
        ),
    ]
)
def test_extract_all_abilities_from_text_ger(ocr_text, expected_result):
    GE = GermanExtractor(ocr_text)
    result = GE.extract_all_abilities_from_text_ger()
    assert expected_result == result
