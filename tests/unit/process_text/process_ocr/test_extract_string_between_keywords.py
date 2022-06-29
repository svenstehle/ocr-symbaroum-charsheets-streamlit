import pytest
from src.process_text.process_ocr import SearchWordNotFound, TextProcessor

# pylint: disable=protected-access


@pytest.mark.parametrize(
    "ocr_text, start_word, end_word, offset, expected_result",
    [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            "merkmale",
            "aufmerksamkeit",
            1,
            "untot (i, siehe seite 231), robust (il, siehe seite 312)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            "merkmale",
            "aufmerksamkeit",
            1,
            "natürliche waffen (1), robust (), test1 (nl), test2 (ln), test3 (n)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_guard"),
            "merkmale",
            "aufmerksamkeit",
            1,
            "kontakte (karawanerwächter)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_aeber"),
            "merkmale",
            "aufmerksamkeit",
            1,
            "natürlicher panzer (il), natürliche waffen (il), robust (i|l, siehe seite 13)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            "traits",
            "integrated",
            1,
            "-",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            "traits",
            "integrated",
            1,
            "-",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_hunter"),
            "traits",
            "integrated",
            1,
            "bloodlust (ill. see p. 54), manifestation (in), spirit form (111)",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            "traits",
            "integrated",
            1,
            "test1 (ii), test2 (nl), test3 (ln), test4 (n), test5 (1il)",
        ),

    # test offsets
        (
            "that ismy small test for a different offset",
            "is",
            "different",
            0,
            "my small test for a",
        ),
        (
            "that ismy small test for a different offset",
            "is",
            "different",
            1,
            "y small test for a",
        )
    ]
)
def test_extract_string_between_keywords(ocr_text, start_word, end_word, offset, expected_result):
    TP = TextProcessor(ocr_text)
    result = TP._extract_string_between_keywords(start_word, end_word, offset)
    assert expected_result == result


def test_extract_string_between_keywords_exception_start_word_not_found(prep_ocr_text_draghul):
    TP = TextProcessor(prep_ocr_text_draghul)
    start_word = "BAZINGA"
    end_word = "merkmale"

    with pytest.raises(SearchWordNotFound) as e:
        TP._extract_string_between_keywords(start_word, end_word)
    assert str(e.value) == f"The start_word '{start_word}' cannot be found in text."


def test_extract_string_between_keywords_exception_end_word_not_found(prep_ocr_text_draghul):
    TP = TextProcessor(prep_ocr_text_draghul)
    start_word = "merkmale"
    end_word = "BAZINGA"

    with pytest.raises(SearchWordNotFound) as e:
        TP._extract_string_between_keywords(start_word, end_word)
    assert str(e.value) == f"The end_word '{end_word}' cannot be found in text."
