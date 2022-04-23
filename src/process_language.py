# License: APACHE LICENSE, VERSION 2.0

from typing import List

from langdetect import DetectorFactory, detect, detect_langs


def detect_language(text: str) -> str:
    DetectorFactory.seed = 0
    lang = detect(text)
    return lang


def detect_languages(text: str) -> List[str]:
    DetectorFactory.seed = 0
    languages = detect_langs(text)
    languages = [l.lang for l in languages]
    return languages


def language_mapper_for_tesseract(languages: List[str]) -> List[str]:
    mappings = {"en": "eng", "de": "deu"}
    for i, l in enumerate(languages):
        if l in mappings:
            languages[i] = mappings[l]
    return languages
