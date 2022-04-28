# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List


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
