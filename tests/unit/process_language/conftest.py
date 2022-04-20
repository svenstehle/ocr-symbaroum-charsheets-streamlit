import pytest


def create_input_translate_text_to():
    input_result_pairs = [
        ("Das ist ein Test", "This is a test"),
        (
            "Das ist ein unerhört schwerster blablatest des Grauens. Lilalbassblau",
            "That's an unheard of the heaviest bluelate of gray. Lilalbass Blue"
        )
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_translate_text_to())
def prep_translate_text_to(request):
    original_text = request.param[0]
    translated_text = request.param[1]
    to = "en"
    yield to, original_text, translated_text
    del to, original_text, translated_text
