import pytest
from src.process_text.extract_info import InformationExtractor
from src.process_text.process_ocr import TextProcessor

# TODO really think about cleaning TextProcessor / InformationExtractor etc interactions


@pytest.mark.parametrize(
    "string, expected_result", [
        (
            "Bloodlust (Ill. see p. 54), Manifestation (IN), Spirit Form (111)",
            "bloodlust (III. see p. 54), manifestation (III), spirit form (III)",
        ),
        (
            "Test1 (iI), Test2 (nl), Test3 (ln), test4 (n), Test5 (1Il)",
            "test1 (II), test2 (III), test3 (III), test4 (II), test5 (III)",
        ),
        (
            "Natürlicher Panzer (Il), Natürliche Waffen (il), Robust (I|l, siehe Seite 13)",
            "natürlicher panzer (II), natürliche waffen (II), robust (III, siehe seite 13)",
        ),
        (
            "Untot (I, siehe Seite 231), Robust (IL, siehe Seite 312)",
            "untot (I, siehe seite 231), robust (II, siehe seite 312)",
        ),
        (
            "Natürliche Waffen (1), Robust (), test1 (Nl), test2 (lN), test3 (N)",
            "natürliche waffen (I), robust (I), test1 (III), test2 (III), test3 (II)",
        ),
        (
            "Kontakte (Karawanerwächter)",
            "kontakte (karawanerwächter)",
        ),
        (
            "-",
            "-",
        ),
    ]
)
def test_clean_roman_numerals(string, expected_result):
    IE = InformationExtractor(string)
    IE._preprocess_text()    # pylint: disable=protected-access
    TP = TextProcessor(IE.text)
    result = TP.clean_roman_numerals(IE.text)
    assert result == expected_result
