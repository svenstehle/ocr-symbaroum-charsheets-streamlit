# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List


class GermanExtractor:
    """Extracts all attributes from German text."""
    def __init__(self, text: str):
        """Constructs all the necessary attributes for the GermanExtractor object.

        Args:
            text (str): the preprocessed text to extract attributes from.
        """
        self.text = text

    def extract_all_attributes_from_text_ger(self, attribute_names: List[str]) -> Dict[str, str]:
        """Extracts all roll20 character attributes from German text.

        Args:
            attribute_names (List[str]): list of the attribute names in German.

        Returns:
            Dict[str, str]: dictionary of the attribute names and their values.
        """
        return {a: self.get_attribute_value_from_text_ger(a) for a in attribute_names}

    def get_attribute_value_from_text_ger(self, attribute_name: str) -> str:
        """Extracts the attribute value from German text.

        Args:
            attribute_name (str): the attribute name to extract the value for.

        Returns:
            str: the attribute value for the given attribute name.
        """
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

    def extract_all_abilities_from_text_ger(self) -> Dict[str, str]:
        """Extracts all roll20 character abilities from German text.

        Returns:
            Dict[str, str]: dictionary of the ability names and their values.
        """
        abilities_str = "fähigkeiten"
        length = len(abilities_str)
        abilities_start_loc = self.text.find(abilities_str) + length + 1
        weapon_str = "waffen"
        abilities_end_loc = self.text.find(weapon_str, abilities_start_loc)
        all_abilities = self.text[abilities_start_loc:abilities_end_loc].strip("., ").replace(".", ",")
        if all_abilities == "keine":
            return {"Abilities found in text": "Zero"}
        all_abilities = [a.strip() for a in all_abilities.split(",")]
        all_abilities = {a.split(" ")[0].title(): a.split(" ")[1][1:-1].title() for a in all_abilities}
        return all_abilities
