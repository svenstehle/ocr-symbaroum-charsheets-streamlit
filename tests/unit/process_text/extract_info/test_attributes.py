from src.process_text.extract_info import InformationExtractor

# pylint: disable=protected-access


def test_attributes_default(prep_ocr_text_fairy_raw):
    IE = InformationExtractor(prep_ocr_text_fairy_raw)
    assert IE.attributes == {"Attributes not found in text": "Zero"}


def test_attributes_extracted(
    prep_ocr_text_fairy_raw,
    prep_hydra_config,
    create_expected_result_attributes_fairy,
):
    IE = InformationExtractor(prep_ocr_text_fairy_raw)
    assert IE._attributes == {"Attributes not found in text": "Zero"}
    IE.extract_information_from_text("dummy", prep_hydra_config)
    assert IE.attributes == create_expected_result_attributes_fairy
    assert IE._attributes == create_expected_result_attributes_fairy
