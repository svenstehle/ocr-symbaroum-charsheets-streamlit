from src.process_text import InformationExtractor


def test_get_toughness(prep_get_toughness):
    attributes, expected_result = prep_get_toughness
    result = InformationExtractor.get_toughness(attributes)
    assert expected_result == result
