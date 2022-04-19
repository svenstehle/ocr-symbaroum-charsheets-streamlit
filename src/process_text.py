# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List, Union

# TODO: due to diversity of OCRed text, we should preprocess all the text before handing it to the functions


class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.preprocess_text()

    def preprocess_text(self) -> None:
        replacements = [
            (" -\n\n", " - "),    # keep single dash that is NOT a line continuation
            (" -\n", " - "),    # keep single dash that is NOT a line continuation
            ("-\n\n", ""),    # remove single dash that is a line continuation
            ("-\n", ""),    # remove single dash that is a line continuation
            ("\n\n", " "),    # remove line continuation
            ("\n", " "),    # remove line continuation
            (" _ ", " - "),    # replace separate underscore with dash
            (" = ", " - "),    # replace separate equal sign with dash
        ]
        for key, rep in replacements:
            self.text = self.text.replace(key, rep)
        self.text = self.text.strip()


def get_attribute_value_from_text_ger(text: str, attribute_name: str) -> str:
    attribute_name_len = len(attribute_name)
    att_start_loc = text.find(attribute_name) + attribute_name_len
    att_end_loc = text.find("(", att_start_loc)
    att_val = text[att_start_loc:att_end_loc].strip(" ")
    return att_val


def extract_all_attributes_from_text_ger(text: str, attribute_names_ger: List[str]) -> Dict[str, str]:
    return {a: get_attribute_value_from_text_ger(text, a) for a in attribute_names_ger}


def get_all_attribute_values_from_text_eng(text: str) -> List[str]:
    start_word = "VIG"
    end_word = "Defense"
    att_start_loc = text.find(start_word) + 3
    att_end_loc = text.find(end_word, att_start_loc)
    att_values = text[att_start_loc:att_end_loc].replace("|", " ").replace("O", "0").split()
    att_values = [str((10 - int(v))) for v in att_values]
    return att_values


def extract_all_attributes_from_text_eng(text: str, attribute_names_eng: List[str]) -> Dict[str, str]:
    att_values = get_all_attribute_values_from_text_eng(text)
    return {a: v for a, v in zip(attribute_names_eng, att_values)}


def extract_all_abilities_from_text_ger(text: str) -> Dict[str, str]:
    abilities_str = "Fähigkeiten"
    length = len(abilities_str)
    abilities_start_loc = text.find(abilities_str) + length + 1
    weapon_str = "Waffen"
    abilities_end_loc = text.find(weapon_str, abilities_start_loc)
    all_abilities = text[abilities_start_loc:abilities_end_loc].strip()
    if all_abilities == "Keine":
        return {"Abilities found in text": "Zero"}
    all_abilities = [a.strip() for a in all_abilities.split(",")]
    all_abilities = {a.split(" ")[0]: a.split(" ")[1][1:-1] for a in all_abilities}
    return all_abilities


def extract_all_abilities_from_text_eng(text: str) -> Dict[str, str]:
    abilities_str = "Abilities"
    length = len(abilities_str)
    abilities_start_loc = text.find(abilities_str) + length + 1
    traits_str = "Traits"
    abilities_end_loc = text.find(traits_str, abilities_start_loc)
    all_abilities = text[abilities_start_loc:abilities_end_loc].strip()
    if all_abilities in ["-", None, "", " "]:
        return {"Abilities found in text": "Zero"}
    all_abilities = [a.strip() for a in all_abilities.split(",")]
    all_abilities = {a.split("(")[0].strip(): a.split("(")[1].strip(") ") for a in all_abilities}
    return all_abilities


def extract_tactics_from_text(text: str, lang: str) -> str:
    if lang == "deu":
        tactics_str = "Taktik:"
    if lang == "eng":
        tactics_str = "Tactics:"
    length = len(tactics_str)
    tactics_start_loc = text.find(tactics_str) + length + 1
    tactics = text[tactics_start_loc:]
    tactics = [t.strip() for t in tactics.split(" ") if t.strip() != ""]
    tactics = " ".join(tactics)
    return tactics


def get_toughness(attributes: Dict[str, str]) -> int:
    strong = int(attributes["Stärke"])
    return max((strong, 10))


def get_roll20_chat_input_str(charname, attributes: Dict[str, str]) -> str:
    basic_string = f"!setattr --name {charname}"
    att_string = f" --strong|{attributes['Stärke']} --quick|{attributes['Gewandtheit']}" +\
                f" --vigilant|{attributes['Aufmerksamkeit']} --resolute|{attributes['Willenskraft']}" +\
                f" --persuasive|{attributes['Ausstrahlung']} --cunning|{attributes['Scharfsinn']}" +\
                f" --discreet|{attributes['Heimlichkeit']} --accurate|{attributes['Präzision']}"

    toughness_string = f" --toughness|{get_toughness(attributes)}"
    return basic_string + att_string + toughness_string


def extract_information_from_text_ger(
    text: str,
    attribute_names_ger: List[str],
    charname: str,
) -> Dict[str, Union[str, Dict[str, str]]]:
    TP = TextProcessor(text)
    text = TP.text
    information: Dict[str, Union[str, Dict[str, str]]] = {}
    information["abilities"] = extract_all_abilities_from_text_ger(text)
    information["tactics"] = extract_tactics_from_text(text, "deu")
    attributes = extract_all_attributes_from_text_ger(text, attribute_names_ger)
    information["setattr_str"] = get_roll20_chat_input_str(charname, attributes)
    return information


def extract_information_from_text_eng(
    text: str,
    attribute_names_eng: List[str],
    charname: str,
) -> Dict[str, Union[str, Dict[str, str]]]:
    TP = TextProcessor(text)
    text = TP.text
    information: Dict[str, Union[str, Dict[str, str]]] = {}
    information["abilities"] = extract_all_abilities_from_text_eng(text)
    information["tactics"] = extract_tactics_from_text(text, "eng")
    attributes = extract_all_attributes_from_text_eng(text, attribute_names_eng)
    information["setattr_str"] = get_roll20_chat_input_str(charname, attributes)
    return information
