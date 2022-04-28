# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List

from process_language import detect_language
from spock.backend.wrappers import \
    Spockspace  # pylint: disable=wrong-import-order

from process_text.extract_english import EnglishExtractor
from process_text.extract_german import GermanExtractor

#TODO add docstrings, maybe with extension?


class InformationExtractor:
    def __init__(self, text: str):
        self.text = text
        self._abilities = {"Abilities not found in text": "Zero"}
        self._attributes = {"Attributes not found in text": "Zero"}
        self._tactics: str = ""
        self._setattr_str: str = ""
        self._lang: str = ""

    @property
    def lang(self) -> str:
        self._lang = detect_language(self.text)
        return self._lang

    @property
    def abilities(self) -> Dict[str, str]:
        return self._abilities

    @property
    def attributes(self) -> Dict[str, str]:
        return self._attributes

    @property
    def tactics(self) -> str:
        return self._tactics

    @property
    def setattr_str(self) -> str:
        return self._setattr_str

    def extract_information_from_text(self, charname: str, config: Spockspace) -> None:
        if self.lang == "de":
            self.extract_information_from_ger_text(charname, config.ExtractionConfig.attribute_names_ger)
        elif self.lang == "en":
            self.extract_information_from_eng_text(charname, config.ExtractionConfig.attribute_names_eng)
        else:
            raise ValueError(f"Detected language {self.lang} not supported")

    def extract_information_from_ger_text(self, charname: str, attribute_names: List[str]) -> None:
        self.preprocess_text()
        GE = GermanExtractor(self.text)
        self._abilities = GE.extract_all_abilities_from_text_ger()
        self._attributes = GE.extract_all_attributes_from_text_ger(attribute_names)
        self.extract_tactics_from_text("Taktik:")
        self.get_roll20_chat_input_str(charname)

    def extract_information_from_eng_text(self, charname: str, attribute_names: List[str]) -> None:
        self.preprocess_text()
        EE = EnglishExtractor(self.text)
        self._abilities = EE.extract_all_abilities_from_text_eng()
        self._attributes = EE.extract_all_attributes_from_text_eng(attribute_names)
        self.extract_tactics_from_text("Tactics:")
        self.get_roll20_chat_input_str(charname)

    def preprocess_text(self) -> None:
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

    def get_roll20_chat_input_str(self, charname: str) -> None:
        if self.lang == "de":
            mapping = {
                "strong": "Stärke",
                "quick": "Gewandtheit",
                "vigilant": "Aufmerksamkeit",
                "resolute": "Willenskraft",
                "persuasive": "Ausstrahlung",
                "cunning": "Scharfsinn",
                "discreet": "Heimlichkeit",
                "accurate": "Präzision"
            }
        elif self.lang == "en":
            mapping = {
                "strong": "STR",
                "quick": "QUI",
                "vigilant": "VIG",
                "resolute": "RES",
                "persuasive": "PER",
                "cunning": "CUN",
                "discreet": "DIS",
                "accurate": "ACC"
            }
        else:
            raise ValueError(f"Language {self.lang} not supported.")

        basic_string = f"!setattr --name {charname}"

        att_string = ""
        for key, value in mapping.items():
            att_string += f" --{key}|{self.attributes[value]}"

        toughness_string = f" --toughness|{self.get_toughness(self.attributes)}"
        self._setattr_str = basic_string + att_string + toughness_string

    def extract_tactics_from_text(self, tactics_str: str) -> None:
        length = len(tactics_str)
        tactics_start_loc = self.text.find(tactics_str) + length + 1
        tactics = self.text[tactics_start_loc:]
        tactics = [t.strip() for t in tactics.split(" ") if t.strip() != ""]
        self._tactics = " ".join(tactics)

    @staticmethod
    def get_toughness(attributes: Dict[str, str]) -> int:
        strength_key = "STR" if "STR" in attributes else "Stärke"
        strong = int(attributes[strength_key])
        return max((strong, 10))
