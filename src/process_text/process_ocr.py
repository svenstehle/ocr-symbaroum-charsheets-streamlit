# License: APACHE LICENSE, VERSION 2.0
#
import re
from typing import List, Tuple


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

    def replace_all_weapon_strings(self, string: str) -> None:
        """Replaces all weapon strings with the corresponding weapon name.

        Args:
            string (str): the string to replace the found matching 'weapon' strings with.

        Raises:
            ValueError: raises if the string is not a valid weapon name.
        """
        if string == "waffen":
            pattern = r"w[ä-üabdeft]{3}en"
        elif string == "weapons":
            pattern = r"w[aeop]{3}ons"
        else:
            raise ValueError(f"Search string '{string}' not supported.")

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
