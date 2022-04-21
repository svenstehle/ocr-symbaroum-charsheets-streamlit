# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List, Union

from process_language import detect_language


class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.preprocess_text()
        self.tactics = None

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

    @property
    def lang(self) -> str:
        return detect_language(self.text)

    def extract_tactics_from_text(self, tactics_str: str) -> str:
        length = len(tactics_str)
        tactics_start_loc = self.text.find(tactics_str) + length + 1
        tactics = self.text[tactics_start_loc:]
        tactics = [t.strip() for t in tactics.split(" ") if t.strip() != ""]
        self.tactics = " ".join(tactics)
        return self.tactics

    @staticmethod
    def get_toughness(attributes: Dict[str, str]) -> int:
        strength_key = "STR" if "STR" in attributes else "Stärke"
        strong = int(attributes[strength_key])
        return max((strong, 10))

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

        toughness_string = f" --toughness|{TextProcessor.get_toughness(attributes)}"
        return basic_string + att_string + toughness_string


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


# class InformationExtractor:
#     def __init__(self, text: str):
#         self.text = text

#     def extract_information_from_text(
#         self,
#         text: str,
#         attribute_names_ger: List[str],
#         attribute_names_eng: List[str],
#         charname: str,
#     ) -> Dict[str, Union[str, Dict[str, str]]]:
#         lang = detect_language(text)
#         if lang == "de":
#             return self.extract_information_from_ger_text(text, attribute_names_ger, charname)
#         if lang == "en":
#             return extract_information_from_text_eng(text, attribute_names_eng, charname)
#         raise ValueError(f"Detected language {lang} not supported")

#     def extract_information_from_ger_text(self, charname: str, attribute_names: List[str]) -> None:
#         GE = GermanExtractor(self.text)
#         abilities = GE.extract_all_abilities_from_text_ger()
#         attributes = GE.extract_all_attributes_from_text_ger(attribute_names)
#         tactics = self.extract_tactics_from_text("Taktik:")
#         setattr_str = self.get_roll20_chat_input_str(charname, attributes)


def extract_information_from_text_ger(
    text: str,
    attribute_names_ger: List[str],
    charname: str,
) -> Dict[str, Union[str, Dict[str, str]]]:
    TP = TextProcessor(text)
    processed_text = TP.text
    information: Dict[str, Union[str, Dict[str, str]]] = {}
    GE = GermanExtractor(processed_text)
    information["abilities"] = GE.extract_all_abilities_from_text_ger()
    attributes = GE.extract_all_attributes_from_text_ger(attribute_names_ger)
    TP.extract_tactics_from_text("Taktik:")
    information["tactics"] = TP.tactics
    information["setattr_str"] = TP.get_roll20_chat_input_str(charname, attributes)
    return information


def get_all_attribute_values_from_text_eng(text: str) -> List[str]:
    start_word = "VIG"
    end_word = "Defense"
    att_start_loc = text.find(start_word) + 3
    att_end_loc = text.find(end_word, att_start_loc)
    att_values = text[att_start_loc:att_end_loc]
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


def extract_all_attributes_from_text_eng(text: str, attribute_names_eng: List[str]) -> Dict[str, str]:
    att_values = get_all_attribute_values_from_text_eng(text)
    return {a: v for a, v in zip(attribute_names_eng, att_values)}


def extract_all_abilities_from_text_eng(text: str) -> Dict[str, str]:
    abilities_str = "Abilities"
    length = len(abilities_str)
    abilities_start_loc = text.find(abilities_str) + length + 1
    traits_str = "Traits"
    abilities_end_loc = text.find(traits_str, abilities_start_loc)
    all_abilities = text[abilities_start_loc:abilities_end_loc].strip("., ").replace(".", ",")
    if all_abilities in ["-", None, "", " "]:
        return {"Abilities found in text": "Zero"}
    all_abilities = [a.strip() for a in all_abilities.split(",")]
    all_abilities = {a.split("(")[0].strip(): a.split("(")[1].strip(") ") for a in all_abilities}
    return all_abilities


def extract_information_from_text_eng(
    text: str,
    attribute_names_eng: List[str],
    charname: str,
) -> Dict[str, Union[str, Dict[str, str]]]:
    TP = TextProcessor(text)
    text = TP.text
    information: Dict[str, Union[str, Dict[str, str]]] = {}
    information["abilities"] = extract_all_abilities_from_text_eng(text)
    TP.extract_tactics_from_text("Tactics:")
    information["tactics"] = TP.tactics
    attributes = extract_all_attributes_from_text_eng(text, attribute_names_eng)
    information["setattr_str"] = TP.get_roll20_chat_input_str(charname, attributes)
    return information


def extract_information_from_text(
    text: str,
    attribute_names_ger: List[str],
    attribute_names_eng: List[str],
    charname: str,
) -> Dict[str, Union[str, Dict[str, str]]]:
    lang = detect_language(text)
    if lang == "de":
        return extract_information_from_text_ger(text, attribute_names_ger, charname)
    if lang == "en":
        return extract_information_from_text_eng(text, attribute_names_eng, charname)
    raise ValueError(f"Detected language {lang} not supported")
