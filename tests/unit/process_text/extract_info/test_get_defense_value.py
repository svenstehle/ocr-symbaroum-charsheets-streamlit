import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "ocr_text, attributes, expected_result", [
        (
            pytest.lazy_fixture("prep_ocr_text_draghul"),
            pytest.lazy_fixture("create_input_get_defense_value_draghul"),
            "15",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_baiagorn"),
            pytest.lazy_fixture("create_input_get_defense_value_baiagorn"),
            "7",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_brand"),
            pytest.lazy_fixture("create_input_get_defense_value_brand"),
            "11",
        ),
        (
            pytest.lazy_fixture("prep_ocr_text_fairy"),
            pytest.lazy_fixture("create_input_get_defense_value_fairy"),
            "13",
        ),
    ]
)
def test_get_defense_value(
    ocr_text,
    attributes,
    expected_result,
):
    IE = InformationExtractor(ocr_text)
    # set attributes used by get_defense_value
    IE._attributes = attributes    # pylint: disable=protected-access
    defense_value = IE.get_defense_value()
    assert defense_value == expected_result
