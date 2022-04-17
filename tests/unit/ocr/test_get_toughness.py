from src.ocr import get_toughness


def test_get_toughness(prep_get_toughness):
    attributes, expected_result = prep_get_toughness
    result = get_toughness(attributes)
    assert expected_result == result
