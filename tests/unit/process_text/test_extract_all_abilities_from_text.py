import pytest
from src.process_text import (extract_all_abilities_from_text_eng, extract_all_abilities_from_text_ger)


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
    result = extract_all_abilities_from_text_ger(ocr_text)
    assert expected_result == result


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_expected_result_extract_all_abilities_from_text_fairy")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_expected_result_extract_all_abilities_from_text_brand")
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            pytest.lazy_fixture("create_expected_result_extract_all_abilities_from_text_hunter")
        ),
    ]
)
def test_extract_all_abilities_from_text_eng(ocr_text, expected_result):
    result = extract_all_abilities_from_text_eng(ocr_text)
    assert expected_result == result
