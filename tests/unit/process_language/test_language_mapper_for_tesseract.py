import pytest
from src.process_language import language_mapper_for_tesseract


@pytest.mark.parametrize(
    "languages, expected_result", [
        (["en", "es", "de"], ["eng", "es", "deu"]),
        (["en"], ["eng"]),
        (["de"], ["deu"]),
        (["de", "en"], ["deu", "eng"]),
        (["en", "de"], ["eng", "deu"]),
    ]
)
def test_language_mapper_for_tesseract(languages, expected_result):
    result = language_mapper_for_tesseract(languages)
    assert result == expected_result
