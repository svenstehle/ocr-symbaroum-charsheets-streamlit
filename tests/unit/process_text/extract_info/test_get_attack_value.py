import pytest
from src.process_text.extract_info import InformationExtractor

# pylint: disable=protected-access


@pytest.mark.parametrize(
    "ocr_text, attributes, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_get_attack_value_draghul"),
            "9",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_get_attack_value_baiagorn"),
            "10",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_get_attack_value_brand"),
            "13",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_get_attack_value_fairy"),
            "10",
        ),
    ]
)
def test_get_attack_value(
    ocr_text,
    attributes,
    expected_result,
):
    IE = InformationExtractor(ocr_text)
    # set attributes used by get_attack_value
    IE._attributes = attributes
    attack_value = IE._get_attack_value()
    assert attack_value == expected_result
