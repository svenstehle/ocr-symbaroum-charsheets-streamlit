import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "ocr_text, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            " ,0o, |\"-5(41 |’-3] (+3[‘+5 | -1 ",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            " ,-3,.[|+43] |/[+1 /+5|-1 |] (, ©] [{(-5 \"0 ",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            " “+5 ,“0[ |©, []43 [”-1 \\-6 (4+1 -8 ",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            " +1, -1/ +5 | [0 -3 -5|+3 | o ",
        ),
    ]
)
def test_extract_raw_attribute_values(ocr_text, expected_result):
    # pylint: disable=protected-access
    EE = EnglishExtractor(ocr_text)
    result = EE._extract_raw_attribute_values()
    assert expected_result == result
