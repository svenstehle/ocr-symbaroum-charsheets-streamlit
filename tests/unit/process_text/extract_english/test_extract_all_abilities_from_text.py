import pytest
from src.process_text.extract_english import EnglishExtractor


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
def test_extract_all_abilities_from_text(ocr_text, expected_result):
    EE = EnglishExtractor(ocr_text)
    result = EE.extract_all_abilities_from_text()
    assert expected_result == result
