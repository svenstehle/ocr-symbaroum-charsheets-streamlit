import pytest
from src.process_text import InformationExtractor


@pytest.mark.parametrize(
    "charname, ocr_text, expected_result", [
        (
            "Gandalf",
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_draghul"),
        ),
        (
            "Captain Marvel",
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_input_str_fairy"),
        ),
    ]
)
def test_tactics_extracted(
    prep_spock_config,
    charname,
    ocr_text,
    expected_result,
):
    IE = InformationExtractor(ocr_text)
    assert IE._setattr_str == ""    # pylint: disable=protected-access
    IE.extract_information_from_text(charname, prep_spock_config)
    assert IE.setattr_str == expected_result
    assert IE._setattr_str == expected_result    # pylint: disable=protected-access


def test_setattr_str_default(prep_ocr_text_fairy):
    IE = InformationExtractor(prep_ocr_text_fairy)
    assert IE._setattr_str == ""    # pylint: disable=protected-access
    assert IE.setattr_str == ""
