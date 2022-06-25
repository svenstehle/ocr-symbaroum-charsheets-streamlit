from src.process_text.extract_info import InformationExtractor

# pylint: disable=protected-access


def test_get_toughness(prep_get_toughness):
    attributes, expected_result = prep_get_toughness
    result = InformationExtractor._get_toughness(attributes)
    assert expected_result == result
