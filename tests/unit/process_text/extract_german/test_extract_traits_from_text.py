import pytest
from src.process_text.extract_german import GermanExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            "untot (I, siehe seite 231), robust (II, siehe seite 312)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            "natürliche waffen (I), robust (I), test1 (III), test2 (III), test3 (II)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            "kontakte (karawanerwächter)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            "natürlicher panzer (II), natürliche waffen (II), robust (III, siehe seite 13)",
        ),
    ]
)
def test_extract_traits_from_text(
    ocr_text,
    expected_result,
    create_input_extract_all_attributes_from_text_ger_general,
):
    attribute_names = create_input_extract_all_attributes_from_text_ger_general
    GE = GermanExtractor(ocr_text, attribute_names)
    result = GE.extract_traits_from_text()
    assert expected_result == result
