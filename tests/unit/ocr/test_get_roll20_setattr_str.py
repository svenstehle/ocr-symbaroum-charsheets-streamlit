from src.ocr import get_roll20_setattr_str


def test_get_roll20_setattr_str(prep_get_roll20_setattr_str):
    charname, attributes, expected_result = prep_get_roll20_setattr_str
    result = get_roll20_setattr_str(charname, attributes)
    assert expected_result == result
