from src.process_text import InformationExtractor


def test_tactics_default(prep_ocr_text_fairy):
    IE = InformationExtractor(prep_ocr_text_fairy)
    assert IE._tactics == ""    # pylint: disable=protected-access
    assert IE.tactics == ""


def test_tactics_extracted(
    prep_ocr_text_fairy,
    prep_spock_config,
    create_expected_result_extract_tactics_from_text_fairy,
):
    IE = InformationExtractor(prep_ocr_text_fairy)
    assert IE._tactics == ""    # pylint: disable=protected-access
    IE.extract_information_from_text("dummy", prep_spock_config)
    assert IE.tactics == create_expected_result_extract_tactics_from_text_fairy
    assert IE._tactics == create_expected_result_extract_tactics_from_text_fairy    # pylint: disable=protected-access
