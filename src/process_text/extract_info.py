# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List

from omegaconf import DictConfig
from src.process_language import detect_language
from src.process_text.extract_english import EnglishExtractor
from src.process_text.extract_german import GermanExtractor
from src.process_text.process_ocr import TextProcessor


class InformationExtractor(TextProcessor):
    """Extracts all Information from OCR'd text."""
    def __init__(self, text: str, **kwargs):
        """Constructs all the necessary attributes for the InformationExtractor object.

        Args:
            text (str): raw text from pytesseract OCR.
        """
        super().__init__(text, **kwargs)
        self.text = text
        self._abilities = {"Abilities not found in text": "Zero"}
        self._attributes = {"Attributes not found in text": "Zero"}
        self._tactics: str = ""
        self._setattr_str: str = ""
        self._lang: str = ""

    @property
    def lang(self) -> str:
        """Detects the language used in the text.

        Returns:
            str: language used in the text.
        """
        self._lang = detect_language(self.text)
        return self._lang

    @property
    def abilities(self) -> Dict[str, str]:
        """Returns the abilities extracted from the text.

        Returns:
            Dict[str, str]: the abilities that were extracted from the text.
        """
        return self._abilities

    @property
    def attributes(self) -> Dict[str, str]:
        """Returns the attributes extracted from the text.

        Returns:
            Dict[str, str]: the attributes that were extracted from the text.
        """
        return self._attributes

    @property
    def tactics(self) -> str:
        """Returns the tactics extracted from the text.

        Returns:
            str: the tactics that were extracted from the text.
        """
        return self._tactics

    @property
    def setattr_str(self) -> str:
        """Returns the roll20 chat input string for the setattr API script.

        Returns:
            str: roll20 chat input string.
        """
        return self._setattr_str

    def extract_information_from_text(self, charname: str, cfg: DictConfig) -> None:
        """Extracts information from the text and saves it in the InformationExtractor object.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
            config (Spockspace): spock-config configuration object.

        Raises:
            ValueError: raised if the detected language of the input text is not supported.
        """
        if self.lang == "de":
            self.extract_information_from_ger_text(charname, cfg.extraction.attribute_names_ger)
        elif self.lang == "en":
            self.extract_information_from_eng_text(charname, cfg.extraction.attribute_names_eng)
        else:
            raise ValueError(f"Detected language {self.lang} not supported")

    def extract_information_from_ger_text(self, charname: str, attribute_names: List[str]) -> None:
        """Extracts information from German text and saves it in the InformationExtractor object.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
            attribute_names (List[str]): list of the attribute names in German language.
        """
        self.preprocess_text()
        self.replace_all_weapon_strings("waffen")
        GE = GermanExtractor(self.text)
        self._abilities = GE.extract_all_abilities_from_text_ger()
        self._attributes = GE.extract_all_attributes_from_text_ger(attribute_names)
        self.extract_tactics_from_text("taktik:")
        self.get_roll20_chat_input_str(charname)

    def extract_information_from_eng_text(self, charname: str, attribute_names: List[str]) -> None:
        """Extracts information from English text and saves it in the InformationExtractor object.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
            attribute_names (List[str]): list of the attribute names in English language.
        """
        self.preprocess_text()
        self.replace_all_weapon_strings("weapons")
        EE = EnglishExtractor(self.text)
        self._abilities = EE.extract_all_abilities_from_text_eng()
        self._attributes = EE.extract_all_attributes_from_text_eng(attribute_names)
        self.extract_tactics_from_text("tactics:")
        self.get_roll20_chat_input_str(charname)

    def preprocess_text(self) -> None:
        """_summary_: Removes all the unnecessary characters from the text."""
        replacements = [
            ("=", "-"),    # replace equal sign with dash
            (" -\n\n", " - "),    # keep single dash that is NOT a line continuation
            (" -\n", " - "),    # keep single dash that is NOT a line continuation
            ("-\n\n", ""),    # remove single dash that is a line continuation
            ("-\n", ""),    # remove single dash that is a line continuation
            ("\n\n", " "),    # remove line continuation
            ("\n", " "),    # remove line continuation
            (" _ ", " - "),    # replace separate underscore with dash
        ]
        for key, rep in replacements:
            self.text = self.text.replace(key, rep)
        self.text = self.text.strip()
        self.text = self.get_lowercase_text(self.text)

    def extract_tactics_from_text(self, tactics_str: str) -> None:
        """Extracts the tactics from the text.

        Args:
            tactics_str (str): tactics search keyword in the relevant language.
        """
        length = len(tactics_str)
        tactics_start_loc = self.text.find(tactics_str) + length + 1
        tactics = self.text[tactics_start_loc:]
        tactics = [t.strip() for t in tactics.split(" ") if t.strip() != ""]
        self._tactics = " ".join(tactics)

    def get_roll20_chat_input_str(self, charname: str) -> None:
        """Creates the roll20 chat input string for the setattr API script.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.

        Raises:
            ValueError: raised if the detected language of the input text is not supported.
        """
        if self.lang == "de":
            mapping = {
                "strong": "stärke",
                "quick": "gewandtheit",
                "vigilant": "aufmerksamkeit",
                "resolute": "willenskraft",
                "persuasive": "ausstrahlung",
                "cunning": "scharfsinn",
                "discreet": "heimlichkeit",
                "accurate": "präzision"
            }
        elif self.lang == "en":
            mapping = {
                "strong": "str",
                "quick": "qui",
                "vigilant": "vig",
                "resolute": "res",
                "persuasive": "per",
                "cunning": "cun",
                "discreet": "dis",
                "accurate": "acc"
            }
        else:
            raise ValueError(f"Language {self.lang} not supported.")

        basic_string = f"!setattr --name {charname}"

        att_string = ""
        for key, value in mapping.items():
            att_string += f" --{key}|{self.attributes[value]}"

        toughness_string = f" --toughness|{self.get_toughness(self.attributes)}"
        self._setattr_str = basic_string + att_string + toughness_string

    @staticmethod
    def get_lowercase_text(text: str) -> str:
        """Returns the text in lowercase.

        Args:
            text (str): input text with capital letters.

        Returns:
            str: text with only lowercase letters.
        """
        return text.lower()

    @staticmethod
    def get_toughness(attributes: Dict[str, str]) -> int:
        """Calculates the toughness from the strong attribute in the relevant language.

        Args:
            attributes (Dict[str, str]): extracted attributes from the text.

        Returns:
            int: roll20 symbaroum character toughness value.
        """
        strength_key = "str" if "str" in attributes else "stärke"
        strong = int(attributes[strength_key])
        return max((strong, 10))
