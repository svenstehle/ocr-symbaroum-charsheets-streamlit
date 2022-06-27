from src.process_text.extract_info import InformationExtractor

# pylint: disable=protected-access


def test_abilities_default(prep_ocr_text_sikander):
    IE = InformationExtractor(prep_ocr_text_sikander)
    assert IE.abilities == {"Abilities not found in text": "Zero"}


def test_abilities_extracted(
    prep_ocr_text_sikander,
    prep_hydra_config,
):
    expected_result = {"Brimstone Cascade": "master", "Flame Wall": "master"}
    IE = InformationExtractor(prep_ocr_text_sikander)
    assert IE._abilities == {"Abilities not found in text": "Zero"}
    IE.extract_information_from_text("dummy", prep_hydra_config)
    assert IE.abilities == expected_result
    assert IE._abilities == expected_result
