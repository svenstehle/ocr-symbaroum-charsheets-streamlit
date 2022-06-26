# License: APACHE LICENSE, VERSION 2.0
#
import re
from typing import List, Tuple

from src.process_language import detect_language


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

    def _replace_all_weapon_strings(self) -> None:
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

        indices = self._get_indices_of_weapon_strings(pattern)
        for (start, end) in indices:
            self.text = self._insert_str_between_indices(self.text, string, start, end)

    def _get_indices_of_weapon_strings(self, pattern: str) -> List[Tuple[int, int]]:
        """Returns the indices of all matching weapon strings in the text. Using regex.

        Args:
            pattern (str): the regex pattern to find matching weapon strings in the text with.

        Returns:
            List[Tuple[int, int]]: List of Tuples with the start and end indices of the weapon strings.
        """
        all_matches = [(m.start(0), m.end(0)) for m in re.finditer(pattern, self.text)]
        return all_matches

    @staticmethod
    def _insert_str_between_indices(original_text: str, string: str, start: int, end: int) -> str:
        """Inserts a string between two indices of another string, called text.

        Args:
            string (str): string to insert.
            start (int): starting index for insertion into text.
            end (int): ending index for insertion (excluding, character at index will remain in text).

        Returns:
            str: text with the inserted string.
        """
        return original_text[:start] + string + original_text[end:]

    @staticmethod
    def _clean_roman_numerals(traits: str) -> str:
        """Cleans the present characters in the 'traits'-str and replaces them with their actual
        roman numerals. We use regex here because ocr has so much trouble in correctly recognizing
        characters like '(I)', '(II)' and '(III)'. Very often, the output will be an '(1ln)' or
        something else incorrect.

        Args:
            traits (str): string containing the traits information.

        Returns:
            str: the cleaned traits-string with the restored roman numerals.
        """
        # TODO find a more concise but correct regex for this. The two ORs are horrible to read.
        # E.g. use regex just to find string and use replace to replace parts iteratively.

        # first, we replace '(III)'
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

    def _cleanup_dice_rolls(self, string: str) -> str:
        """Cleanup misrecognized ocr'd characters in string,
        i.e. dice rolls like '1w10' or '2d6'.

        Args:
            string (str): the string with possible dice rolls in it.

        Returns:
            str: the cleaned string.
        """
        search_pattern = re.compile(
            r"""
            [i1-9]          # matches a single character, either i or a digit from 1 to 9
            [wd]            # matches the character 'w' literally (case sensitive)
            [i]?            # matches the single character 'i' zero or one time
            [io0-9]{1,2}    # matches a single character, either i, o or a digit from 0 to 9
                            # {1, 2} matches the previous token between 1 and 2 times
            """,
            re.X,
        )
        match = re.search(search_pattern, string)
        if match:
            # usually just one roll here, let's start with that base case
            dice_rolls = string[match.start():].split()[0]
            dice_rolls = (
                dice_rolls.replace("i1", "1").replace("ii", "1").replace("1i", "1").replace("o", "0").replace("i", "1")
            )
            dice_rolls += " "

            # insert cleaned rolls and remove redundant whitespaces
            beginning = match.start()
            end = match.start() + len(dice_rolls)
            string = self._insert_str_between_indices(string, dice_rolls, beginning, end)
            string = " ".join(string.split())
        return string

    def _extract_from_start_token_until_end(self, start_token: str) -> str:
        """Extracts and returns the last part of a string. Starting from a
        excluded start token it returns everything afterwards.

        Args:
            start_token (str): the start token to look for in the text.
                First match is used.

        Returns:
            str: the part of the string that comes after the start token
                until the end of the string.
        """
        length = len(start_token)
        start_loc = self.text.find(start_token) + length + 1
        extract = self.text[start_loc:]
        extract = [t.strip() for t in extract.split(" ") if t.strip() != ""]
        return " ".join(extract)

    def _extract_string_between_keywords(self, start_word: str, end_word: str, offset: int = 1) -> str:
        """Extracts a string between two keywords, which are exclusive.
        Example:
        >>> string = "my rabbit hops into the deep dark hole"
        >>> output = self.__extract_string_between_keywords('rabbit', 'dark')
        >>> print(output)
        'hops into the deep'

        Args:
            start_word (str): the first match found in the text.
                If 'start_word' is not found, raises SearchWordNotFound.
            end_word (str): the first match found in the text.
                But the search begins starting with the start_word.
                If 'end_word' is not found, raises SearchWordNotFound.
            offset (int): the offset that is added to the length of the 'start_word'.
                Extraction of text begins with the index of the last character of
                'start_word' + 'offset'. Defaults to 1.

        Raises:
            SearchWordNotFound: Raised when the specified word to search for
                could not be found in a string.

        Returns:
            str: the extracted string between the selected start and end words.
        """
        offset += len(start_word)
        start_word_loc = self.text.find(start_word) + offset
        end_word_loc = self.text.find(end_word, start_word_loc)

        if start_word_loc < offset:
            raise SearchWordNotFound(f"The start_word '{start_word}' cannot be found in text.")
        if end_word_loc < 0:
            raise SearchWordNotFound(f"The end_word '{end_word}' cannot be found in text.")

        extract = self.text[start_word_loc:end_word_loc].strip()
        return extract


class LanguageNotSupported(ValueError):
    """Raised when the detected language of the ocr'd
    input text is not German or English
    """


class SearchWordNotFound(ValueError):
    """Raised when the specified word to search for
    could not be found in a string.
    """
