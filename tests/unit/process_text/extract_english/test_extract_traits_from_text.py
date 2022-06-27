import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            "-",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            "-",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            "bloodlust (III. see p. 54), manifestation (III), spirit form (III)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            "test1 (II), test2 (III), test3 (III), test4 (II), test5 (III)",
        ),
    ]
)
def test_extract_traits_from_text(
    ocr_text,
    expected_result,
    create_input_extract_all_attributes_from_text_eng_general,
):
    EE = EnglishExtractor(ocr_text, create_input_extract_all_attributes_from_text_eng_general)
    result = EE.extract_traits_from_text()
    assert expected_result == result
