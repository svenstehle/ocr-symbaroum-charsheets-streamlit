# License: APACHE LICENSE, VERSION 2.0
#
import re
from typing import List, Tuple

from src.process_language import detect_language


# TODO watch out for refactoring inheritance of TextProcessor
# Depending on future features, mb move to English/GermanExtractor
class TextProcessor:
    """Processes the text from OCR'd images."""
    def __init__(self, text: str):
        """Constructs all the necessary attributes for the TextProcessor object.

        Args:
            text (str): text from pytesseract OCR.
        """
        self.text = text
        self._lang: str = ""

    @property
    def lang(self) -> str:
        """Detects the language used in the text.

        Returns:
            str: language used in the text.
        """
        self._lang = detect_language(self.text)
        return self._lang

    def replace_all_weapon_strings(self) -> None:
        """Replaces all weapon strings in text with the correct corresponding
        weapon name, based on the detected language.

        Raises:
            ValueError: raises if the string is not a valid weapon name.
        """
        if self.lang == "de":
            string = "waffen"
            pattern = r"w[ä-üabdeft]{3}en"
        elif self.lang == "en":
            string = "weapons"
            pattern = r"w[aeop]{3}ons"
        else:
            raise LanguageNotSupported(f"Detected language {self.lang} not supported")

        indices = self.get_indices_of_weapon_strings(pattern)
        for (start, end) in indices:
            self.text = self.insert_str_between_indices(string, start, end)

    def get_indices_of_weapon_strings(self, pattern: str) -> List[Tuple[int, int]]:
        """Returns the indices of all matching weapon strings in the text. Using regex.

        Args:
            pattern (str): the regex pattern to find matching weapon strings in the text with.

        Returns:
            List[Tuple[int, int]]: List of Tuples with the start and end indices of the weapon strings.
        """
        all_matches = [(m.start(0), m.end(0)) for m in re.finditer(pattern, self.text)]
        return all_matches

    def insert_str_between_indices(self, string: str, start: int, end: int) -> str:
        """Inserts a string between two indices of another string, called text.

        Args:
            string (str): string to insert.
            start (int): starting index for insertion into text.
            end (int): ending index for insertion (excluding, character at index will remain in text).

        Returns:
            str: text with the inserted string.
        """
        return self.text[:start] + string + self.text[end:]

    @staticmethod
    def clean_roman_numerals(traits: str) -> str:
        # process traits with regex because ocr has so much trouble
        # with '(I)', '(II)' and '(III)' expressions

        # first, we replace '(III)'
        # TODO test
        # TODO Docstring
        # TODO find a more concise but correct regex for this. The two ORs are horrible to read
        traits = re.sub(
            r"""
            (?x)        # Use free-spacing mode.
            \(          # Match a literal '('
            [i1l|]{3}   # Match one of the tokens in the brackets, three times
            |           # OR operator, match the first or the second regex option
            \(          # Match a literal '('
            n           # Match a literal 'n'
            [i1l|]{1}   # Match one of the tokens in the brackets, two times
            |           # OR operator, match the first or the second regex option
            \(          # Match a literal '('
            [i1l|]{1}   # Match one of the tokens in the brackets, two times
            n           # Match a literal 'n'
            """, "(III", traits
        )
        # second, replace '(II)'
        traits = re.sub(
            r"""
            (?x)        # Use free-spacing mode.
            \(          # Match a literal '('
            [^I]?       # Exclude a literal 'I' from the match, which means we replaced before
                        # '?' means to match this greedy from 0 times to 1, however many found
            [i1l|]{2}   # Match one of the tokens in the brackets, two times
            |           # OR operator, match the first or the second regex option
            \(          # Match a literal '('
            n           # Match a literal 'n'
            """, "(II", traits
        )

        # third, replace '(I)'
        traits = re.sub(
            r"""
            (?x)        # Use free-spacing mode.
            \(          # Match a literal '('
            [^I]?       # Exclude a literal 'I' from the match, which means we replaced before
                        # '?' means to match this greedy from 0 times to 1, however many found
            [i1l|]{1}   # Match one of the tokens in the brackets, zero or one times
            """, "(I", traits
        )

        # last, replace '()'
        traits = re.sub(
            r"""
            (?x)        # Use free-spacing mode.
            \(          # Match a literal '('
            \)          # Match a literal ')'
            """, "(I)", traits
        )
        return traits


class LanguageNotSupported(ValueError):
    """Raised when the detected language of the ocr'd
    input text is not German or English
    """
