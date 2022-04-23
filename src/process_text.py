# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List

from spock.backend.wrappers import Spockspace

from process_language import detect_language

#TODO add docstrings, maybe with extension?
#TODO add mypy correctly


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def preprocess_text(self) -> str:
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
        return self.text


# refactor the class to increase cohesion across methods
class InformationExtractor:
    def __init__(self, text: str):
        self.text = text
        self._abilities = {"Abilities not found in text": "Zero"}
        self._attributes = {"Attributes not found in text": "Zero"}
        self._tactics: str = ""
        self.setattr_str: str = ""
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

    def extract_information_from_text(self, charname: str, config: Spockspace) -> None:
        if self.lang == "de":
            self.extract_information_from_ger_text(charname, config.ExtractionConfig.attribute_names_ger)
        elif self.lang == "en":
            self.extract_information_from_eng_text(charname, config.ExtractionConfig.attribute_names_eng)
        else:
            raise ValueError(f"Detected language {self.lang} not supported")

    def extract_information_from_ger_text(self, charname: str, attribute_names: List[str]) -> None:
        self.text = TextProcessor(self.text).preprocess_text()
        GE = GermanExtractor(self.text)
        self._abilities = GE.extract_all_abilities_from_text_ger()
        self._attributes = GE.extract_all_attributes_from_text_ger(attribute_names)
        self.extract_tactics_from_text("Taktik:")
        self.setattr_str = self.get_roll20_chat_input_str(charname, self.attributes)

    def extract_information_from_eng_text(self, charname: str, attribute_names: List[str]) -> None:
        self.text = TextProcessor(self.text).preprocess_text()
        EE = EnglishExtractor(self.text)
        self._abilities = EE.extract_all_abilities_from_text_eng()
        self._attributes = EE.extract_all_attributes_from_text_eng(attribute_names)
        self.extract_tactics_from_text("Tactics:")
        self.setattr_str = self.get_roll20_chat_input_str(charname, self.attributes)

    def get_roll20_chat_input_str(self, charname: str, attributes: Dict[str, str]) -> str:
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
            att_string += f" --{key}|{attributes[value]}"

        toughness_string = f" --toughness|{self.get_toughness(attributes)}"
        self.setattr_str = basic_string + att_string + toughness_string
        return self.setattr_str

    def extract_tactics_from_text(self, tactics_str: str):
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


class GermanExtractor:
    def __init__(self, text: str):
        self.text = text

    def get_attribute_value_from_text_ger(self, attribute_name: str) -> str:
        attribute_name_len = len(attribute_name)
        att_start_loc = self.text.find(attribute_name) + attribute_name_len
        att_end_loc = self.text.find("(", att_start_loc)
        att_val = self.text[att_start_loc:att_end_loc].strip(" ")
        mapping = [
            ("/", "7"),
        ]
        for k, v in mapping:
            att_val = att_val.replace(k, v)
        return att_val

    def extract_all_attributes_from_text_ger(self, attribute_names: List[str]) -> Dict[str, str]:
        return {a: self.get_attribute_value_from_text_ger(a) for a in attribute_names}

    def extract_all_abilities_from_text_ger(self) -> Dict[str, str]:
        abilities_str = "Fähigkeiten"
        length = len(abilities_str)
        abilities_start_loc = self.text.find(abilities_str) + length + 1
        weapon_str = "Waffen"
        abilities_end_loc = self.text.find(weapon_str, abilities_start_loc)
        all_abilities = self.text[abilities_start_loc:abilities_end_loc].strip("., ").replace(".", ",")
        if all_abilities == "Keine":
            return {"Abilities found in text": "Zero"}
        all_abilities = [a.strip() for a in all_abilities.split(",")]
        all_abilities = {a.split(" ")[0]: a.split(" ")[1][1:-1] for a in all_abilities}
        return all_abilities


class EnglishExtractor:
    def __init__(self, text: str):
        self.text = text

    def extract_all_attributes_from_text_eng(self, attribute_names_eng: List[str]) -> Dict[str, str]:
        att_values = self.get_all_attribute_values_from_text_eng()
        return {a: v for a, v in zip(attribute_names_eng, att_values)}

    def get_all_attribute_values_from_text_eng(self) -> List[str]:
        start_word = "VIG"
        end_word = "Defense"
        att_start_loc = self.text.find(start_word) + 3
        att_end_loc = self.text.find(end_word, att_start_loc)
        att_values = self.text[att_start_loc:att_end_loc]
        mapping = [
            ("|", " "),
            ("[", " "),
            ("]", " "),
            ("{", " "),
            ("}", " "),
            ("(", " "),
            (")", " "),
            (",", " "),
            ("O", "0"),
            ("©", "0"),
            (".", " "),
            ("’", " "),
            ("‘", " "),
            ("“", " "),
            ("”", " "),
            ("\"", " "),
            ("\\", " "),
            ("/", " "),
            ("00", "0 0"),
        ]
        for k, v in mapping:
            att_values = att_values.replace(k, v)

        att_values_clean = []
        for v in att_values.split():
            if v.isdigit() and len(v) == 2 and v.startswith("4"):
                v = v.replace("4", "+")
            elif len(v) == 3 and v.startswith("+4") and v[1:].isdigit():
                v = v.replace("+4", "+")
            att_values_clean.append(v)
        att_values_clean = [str((10 - int(v))) for v in att_values_clean]
        return att_values_clean

    def extract_all_abilities_from_text_eng(self) -> Dict[str, str]:
        abilities_str = "Abilities"
        length = len(abilities_str)
        abilities_start_loc = self.text.find(abilities_str) + length + 1
        traits_str = "Traits"
        abilities_end_loc = self.text.find(traits_str, abilities_start_loc)
        all_abilities = self.text[abilities_start_loc:abilities_end_loc].strip("., ").replace(".", ",")
        if all_abilities in ["-", None, "", " "]:
            return {"Abilities found in text": "Zero"}
        all_abilities = [a.strip() for a in all_abilities.split(",")]
        all_abilities = {a.split("(")[0].strip(): a.split("(")[1].strip(") ") for a in all_abilities}
        return all_abilities
