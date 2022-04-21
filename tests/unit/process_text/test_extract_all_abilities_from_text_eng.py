import pytest
from src.process_text import extract_all_abilities_from_text_eng


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
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            pytest.lazy_fixture("create_expected_result_extract_all_abilities_from_text_sikander")
        ),
    ]
)
def test_extract_all_abilities_from_text_eng(ocr_text, expected_result):
    result = extract_all_abilities_from_text_eng(ocr_text)
    assert expected_result == result
