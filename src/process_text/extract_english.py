# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List


class EnglishExtractor:
    """Extracts all attributes from English text."""
    def __init__(self, text: str):
        """Constructs all the necessary attributes for the EnglishExtractor object.

        Args:
            text (str): the preprocessed text to extract attributes from.
        """
        self.text = text

    def extract_all_attributes_from_text_eng(self, attribute_names_eng: List[str]) -> Dict[str, str]:
        """Extracts all roll20 character attributes from English text.

        Args:
            attribute_names_eng (List[str]): list of the attribute names in English.

        Returns:
            Dict[str, str]: dictionary of the attribute names and their values.
        """
        att_values = self.get_all_attribute_values_from_text_eng()
        return {a: v for a, v in zip(attribute_names_eng, att_values)}

    def get_all_attribute_values_from_text_eng(self) -> List[str]:
        """Returns all the attribute values from English text.

        Returns:
            List[str]: list of the attribute values without any names.
        """
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
            elif len(v) == 3 and v.startswith("4+") and v[2].isdigit():
                v = v.replace("4+", "+")
            att_values_clean.append(v)
        att_values_clean = [str((10 - int(v))) for v in att_values_clean]
        return att_values_clean

    def extract_all_abilities_from_text_eng(self) -> Dict[str, str]:
        """Extracts all roll20 character abilities from English text.

        Returns:
            Dict[str, str]: dictionary of the ability names and their rank.
        """
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
