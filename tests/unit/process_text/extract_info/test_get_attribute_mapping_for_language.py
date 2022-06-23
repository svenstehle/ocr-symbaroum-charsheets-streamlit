import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, lang, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            "de",
            pytest.lazy_fixture("create_expected_result_get_attribute_mapping_for_language_ger"),
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_sikander"),
            "en",
            pytest.lazy_fixture("create_expected_result_get_attribute_mapping_for_language_eng"),
        ),
    ]
)
def test_get_attribute_mapping_for_language(ocr_text, lang, expected_result):
    IE = InformationExtractor(ocr_text)
    mapping = IE._get_attribute_mapping_for_language()    # pylint: disable=protected-access
    assert IE.lang == lang
    assert mapping == expected_result


def test_get_attribute_mapping_for_language_exception(prep_ocr_text_unknown_language):
    IE = InformationExtractor(prep_ocr_text_unknown_language)
    with pytest.raises(ValueError):
        IE._get_attribute_mapping_for_language()    # pylint: disable=protected-access
    assert IE.lang == "fr"
