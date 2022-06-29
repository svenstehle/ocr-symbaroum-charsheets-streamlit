# License: APACHE LICENSE, VERSION 2.0
#

from typing import Dict, List

from src.process_text.base_extractor import BaseExtractor


class GermanExtractor(BaseExtractor):
    """Extracts all attributes from German text."""
    def __init__(self, text: str, attribute_names: List[str]):
        # pylint: disable=useless-super-delegation
        """Constructs all the necessary attributes for the GermanExtractor object.

        Args:
            text (str): the preprocessed text to extract attributes from.
            attribute_names (List[str]): list of the attribute names in German language.
        """
        super().__init__(text, attribute_names)

    def extract_all_attributes_from_text(self) -> Dict[str, str]:
        """Extracts all roll20 character attributes from German text.

        Returns:
            Dict[str, str]: dictionary of the attribute names and their values.
        """
        return {a: self._get_attribute_value_from_text(a) for a in self.attribute_names}

    def extract_all_abilities_from_text(self) -> Dict[str, str]:
        """Extracts all roll20 character abilities from German text.

        Returns:
            Dict[str, str]: dictionary of the ability names and their values.
        """
        all_abilities = self._extract_string_between_keywords("fähigkeiten", "waffen").strip("., ").replace(".", ",")
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
        equipment = self._extract_string_between_keywords("ausrüstung", "schatten")
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
        armor = self._extract_string_between_keywords("rüstung", "verteidigung")

        # filter digits from string and return armor value
        armor = ''.join(filter(lambda i: i.isdigit(), armor))
        return armor

    def extract_traits_from_text(self) -> str:
        """Extracts, the roll20 character traits from German text.

        Returns:
            str: string with the traits.
        """
        traits = self._extract_string_between_keywords("merkmale", "aufmerksamkeit")
        return self._clean_roman_numerals(traits)

    def extract_tactics_from_text(self) -> str:
        """Extracts the tactics from the German text.

        Returns:
            str: the extracted tactics string.
        """
        tactics_str = "taktik:"
        return self._extract_from_start_token_until_end(tactics_str)

    def _get_attribute_value_from_text(self, attribute_name: str) -> str:
        """Extracts the attribute value from German text.

        Args:
            attribute_name (str): the attribute name to extract the value for.

        Returns:
            str: the attribute value for the given attribute name.
        """
        att_val = self._extract_string_between_keywords(attribute_name, "(", 0).strip(" ")
        att_val = att_val.replace("/", "7")
        return att_val
