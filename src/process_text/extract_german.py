# License: APACHE LICENSE, VERSION 2.0
#
import re
from typing import Dict, List

from src.process_text.process_ocr import TextProcessor


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

    def extract_equipment_from_text_ger(self) -> str:
        """Extracts all roll20 character equipment from German text.

        Returns:
            str: string with the equipment.
        """
        equipment_str = "ausrüstung"
        length = len(equipment_str)
        equipment_start_loc = self.text.find(equipment_str) + length + 1

        shadow_str = "schatten"
        equipment_end_loc = self.text.find(shadow_str, equipment_start_loc)
        equipment = self.text[equipment_start_loc:equipment_end_loc].strip()
        # process misrecognized ocr'd characters, i.e. dice rolls like '1w10'
        search_pattern = re.compile(
            r"""
            [i1-9]          # matches a single character, either i or a digit from 1 to 9
            [wd]            # matches a single character, 'w' or 'd', literally (case sensitive)
            [i]?            # matches the single character 'i' zero or one time
            [io0-9]{1,2}    # matches a single character, either i, o or a digit from 0 to 9
                            # {1, 2} matches the previous token between 1 and 2 times
            """,
            re.X,
        )
        match = re.search(search_pattern, equipment)
        if match:
            # usually just one roll here, let's start with that base case
            dice_rolls = equipment[match.start():].split()[0]
            dice_rolls = dice_rolls.replace("i1", "1").replace("ii", "1").replace("1i", "1").replace("o", "0") + " "
            # refactor this to Textprocessor and replace all matching misrecognized dice rolls in original ocr'd text
            TP = TextProcessor(equipment)
            beginning = match.start()
            end = match.start() + len(dice_rolls)
            # insert cleaned rolls and remove redundant whitespaces
            equipment = TP.insert_str_between_indices(dice_rolls, beginning, end)
            equipment = " ".join(equipment.split())

        return equipment

    def extract_armor_from_text_ger(self) -> str:
        """Extracts, if possible, the roll20 character armor value from German text.
        Usually this is based on equipment and sometimes additional traits.
        Just using the equipment, this works well for German texts. However, applying
        values from traits has not been implemented. English texts are non-standard
        in this regard and armor is difficult to extract from them.

        Returns:
            str: string with the armor value.
        """
        armor_str = "rüstung"
        length = len(armor_str)
        armor_start_loc = self.text.find(armor_str) + length + 1

        shadow_str = "verteidigung"
        armor_end_loc = self.text.find(shadow_str, armor_start_loc)
        armor = self.text[armor_start_loc:armor_end_loc].strip()

        # filter digits from string and return armor value
        armor = ''.join(filter(lambda i: i.isdigit(), armor))
        return armor

    def extract_traits_from_text_ger(self) -> str:
        """Extracts, the roll20 character traits from German text.

        Returns:
            str: string with the traits.
        """
        traits_start_str = "merkmale"
        length = len(traits_start_str)
        traits_start_loc = self.text.find(traits_start_str) + length + 1

        traits_end_str = "aufmerksamkeit"
        traits_end_loc = self.text.find(traits_end_str, traits_start_loc)
        traits = self.text[traits_start_loc:traits_end_loc].strip()

        return TextProcessor.clean_roman_numerals(traits)
