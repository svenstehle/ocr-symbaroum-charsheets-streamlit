from src.translate import translate_text_to


def test_translate_text_to(prep_translate_text_to):
    to, text, expected_result = prep_translate_text_to
    translation = translate_text_to(text, to)
    assert expected_result == translation
