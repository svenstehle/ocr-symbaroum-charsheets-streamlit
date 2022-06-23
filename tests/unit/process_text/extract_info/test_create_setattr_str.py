import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "charname, ocr_text, attributes, expected_result_name, expected_result_sel", [
        (
            "Gandalf",
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_create_setattr_str_draghul"),
            pytest.lazy_fixture("create_expected_result_setattr_name_str_draghul"),
            pytest.lazy_fixture("create_expected_result_setattr_sel_str_draghul"),
        ),
        (
            "Legolas",
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_create_setattr_str_baiagorn"),
            pytest.lazy_fixture("create_expected_result_setattr_name_str_baiagorn"),
            pytest.lazy_fixture("create_expected_result_setattr_sel_str_baiagorn"),
        ),
        (
            "Hulk",
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_create_setattr_str_brand"),
            pytest.lazy_fixture("create_expected_result_setattr_name_str_brand"),
            pytest.lazy_fixture("create_expected_result_setattr_sel_str_brand"),
        ),
        (
            "Captain Marvel",
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_create_setattr_str_fairy"),
            pytest.lazy_fixture("create_expected_result_setattr_name_str_fairy"),
            pytest.lazy_fixture("create_expected_result_setattr_sel_str_fairy"),
        ),
    ]
)
def test_create_setattr_str(
    charname,
    ocr_text,
    attributes,
    expected_result_name,
    expected_result_sel,
):
    IE = InformationExtractor(ocr_text)
    # set attributes used by create_setattr_str
    IE._attributes = attributes    # pylint: disable=protected-access
    # assert defaults
    assert IE._setattr_name_str == ""    # pylint: disable=protected-access
    assert IE._setattr_sel_str == ""    # pylint: disable=protected-access
    assert IE.setattr_name_str == ""
    assert IE.setattr_sel_str == ""
    IE.create_setattr_str(charname)
    assert IE.setattr_name_str == expected_result_name
    assert IE._setattr_name_str == expected_result_name    # pylint: disable=protected-access
    assert IE.setattr_sel_str == expected_result_sel
    assert IE._setattr_sel_str == expected_result_sel    # pylint: disable=protected-access
