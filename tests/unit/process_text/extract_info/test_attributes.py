from src.process_text.extract_info import InformationExtractor


def test_attributes_default(prep_ocr_text_fairy):
    IE = InformationExtractor(prep_ocr_text_fairy)
    assert IE.attributes == {"Attributes not found in text": "Zero"}


def test_attributes_extracted(
    prep_ocr_text_fairy,
    prep_spock_config,
    create_expected_result_extract_all_attributes_from_text_eng_fairy,
):
    IE = InformationExtractor(prep_ocr_text_fairy)
    assert IE._attributes == {"Attributes not found in text": "Zero"}    # pylint: disable=protected-access
    IE.extract_information_from_text("dummy", prep_spock_config)
    assert IE.attributes == create_expected_result_extract_all_attributes_from_text_eng_fairy
    assert IE._attributes == create_expected_result_extract_all_attributes_from_text_eng_fairy    # pylint: disable=protected-access
