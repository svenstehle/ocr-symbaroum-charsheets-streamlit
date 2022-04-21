from src.process_text import TextProcessor


def test_get_toughness(prep_get_toughness):
    attributes, expected_result = prep_get_toughness
    result = TextProcessor.get_toughness(attributes)
    assert expected_result == result
