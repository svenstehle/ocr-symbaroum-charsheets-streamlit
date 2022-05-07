# License: APACHE LICENSE, VERSION 2.0

from typing import List

from langdetect import DetectorFactory, detect, detect_langs


def get_languages_present_in_text(text: str) -> str:
    """Gets the languages used in input text.

    Args:
        text (str): the raw OCR'd text.

    Returns:
        str: the languages used in the text.
        Most used language is the first (or only) item in the list.
    """
    languages = detect_languages(text)
    languages = language_mapper_for_tesseract(languages)
    languages = "+".join(languages)
    return languages


def detect_languages(text: str) -> List[str]:
    """Detects languages used in input text.

    Args:
        text (str): input text for which to detect used languages.

    Returns:
        List[str]: list of detected languages.
    """
    DetectorFactory.seed = 0
    languages = detect_langs(text)
    languages = [l.lang for l in languages]
    return languages


def language_mapper_for_tesseract(languages: List[str]) -> List[str]:
    """Returns a list of language mappings that are compatible with tesseract input argument 'lang'.

    Args:
        languages (List[str]): list of languages returned by 'detect_languages'.

    Returns:
        List[str]: list of languages that are compatible with tesseract input argument 'lang'.
    """
    mappings = {"en": "eng", "de": "deu"}
    for i, l in enumerate(languages):
        if l in mappings:
            languages[i] = mappings[l]
    return languages


def detect_language(text: str) -> str:
    """Detects language of text.

    Args:
        text (str): input text to detect language of.

    Returns:
        str: the detected language of the input text.
    """
    DetectorFactory.seed = 0
    lang = detect(text)
    return lang
