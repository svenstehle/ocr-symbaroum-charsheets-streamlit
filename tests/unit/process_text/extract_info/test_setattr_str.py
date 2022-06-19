import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "charname, ocr_text, expected_result_name, expected_result_sel", [
        (
            "Gandalf",
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_name_input_str_draghul"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_sel_input_str_draghul"),
        ),
        (
            "Captain Marvel",
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_name_input_str_fairy"),
            pytest.lazy_fixture("create_expected_result_get_roll20_chat_sel_input_str_fairy"),
        ),
    ]
)
def test_setattr_str_with_info_extracted(
    prep_hydra_config,
    charname,
    ocr_text,
    expected_result_name,
    expected_result_sel,
):
    IE = InformationExtractor(ocr_text)
    assert IE._setattr_name_str == ""    # pylint: disable=protected-access
    assert IE._setattr_sel_str == ""    # pylint: disable=protected-access
    IE.extract_information_from_text(charname, prep_hydra_config)
    assert IE.setattr_name_str == expected_result_name
    assert IE._setattr_name_str == expected_result_name    # pylint: disable=protected-access
    assert IE.setattr_sel_str == expected_result_sel
    assert IE._setattr_sel_str == expected_result_sel    # pylint: disable=protected-access


def test_setattr_str_default(prep_ocr_text_fairy):
    IE = InformationExtractor(prep_ocr_text_fairy)
    assert IE._setattr_name_str == ""    # pylint: disable=protected-access
    assert IE.setattr_name_str == ""
    assert IE._setattr_sel_str == ""    # pylint: disable=protected-access
    assert IE.setattr_sel_str == ""
