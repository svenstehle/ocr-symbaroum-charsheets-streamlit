from src.process_text.extract_info import InformationExtractor


def test_abilities_default(prep_ocr_text_sikander):
    IE = InformationExtractor(prep_ocr_text_sikander)
    assert IE.abilities == {"Abilities not found in text": "Zero"}


def test_abilities_extracted(
    prep_ocr_text_sikander,
    prep_spock_config,
    create_expected_result_extract_all_abilities_from_text_sikander,
):
    IE = InformationExtractor(prep_ocr_text_sikander)
    assert IE._abilities == {"Abilities not found in text": "Zero"}    # pylint: disable=protected-access
    IE.extract_information_from_text("dummy", prep_spock_config)
    assert IE.abilities == create_expected_result_extract_all_abilities_from_text_sikander
    assert IE._abilities == create_expected_result_extract_all_abilities_from_text_sikander    # pylint: disable=protected-access
