# License: APACHE LICENSE, VERSION 2.0
#

from typing import Dict, List

from src.process_text.process_ocr import TextProcessor


class GermanExtractor(TextProcessor):
    """Extracts all attributes from German text."""
    def __init__(self, text: str, *args, **kwargs):
        """Constructs all the necessary attributes for the GermanExtractor object.

        Args:
            text (str): the preprocessed text to extract attributes from.
        """
        super().__init__(text, *args, **kwargs)
        self.text = text

    def extract_all_attributes_from_text(self, attribute_names: List[str]) -> Dict[str, str]:
        """Extracts all roll20 character attributes from German text.

        Args:
            attribute_names (List[str]): list of the attribute names in German.

        Returns:
            Dict[str, str]: dictionary of the attribute names and their values.
        """
        return {a: self._get_attribute_value_from_text(a) for a in attribute_names}

    def extract_all_abilities_from_text(self) -> Dict[str, str]:
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

    def extract_equipment_from_text(self) -> str:
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

        equipment = self._cleanup_dice_rolls(equipment)
        return equipment

    def extract_armor_from_text(self) -> str:
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

    def extract_traits_from_text(self) -> str:
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
        return self._clean_roman_numerals(traits)

    def extract_tactics_from_text(self) -> str:
        """Extracts the tactics from the German text.

        Returns:
            str: the extracted tactics string.
        """
        tactics_str = "taktik:"
        length = len(tactics_str)
        tactics_start_loc = self.text.find(tactics_str) + length + 1
        tactics = self.text[tactics_start_loc:]
        tactics = [t.strip() for t in tactics.split(" ") if t.strip() != ""]
        return " ".join(tactics)

    def _get_attribute_value_from_text(self, attribute_name: str) -> str:
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
