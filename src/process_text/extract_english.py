# License: APACHE LICENSE, VERSION 2.0
#
import re
from typing import Dict, List

from src.process_text.base_extractor import BaseExtractor


class EnglishExtractor(BaseExtractor):
    """Extracts all attributes from English text."""
    def __init__(self, text: str, attribute_names: List[str], *args, **kwargs):
        """Constructs all the necessary attributes for the EnglishExtractor object.

        Args:
            text (str): the preprocessed text to extract attributes from.
            attribute_names (List[str]): list of the attribute names in English language.
        """
        super().__init__(text, attribute_names, *args, **kwargs)
        self.text = text
        self.attribute_names = attribute_names

    def extract_all_attributes_from_text(self) -> Dict[str, str]:
        """Extracts all roll20 character attributes from English text.

        Returns:
            Dict[str, str]: dictionary of the attribute names and their values.
        """
        att_values = self._get_all_attribute_values_from_text()
        return {a: v for a, v in zip(self.attribute_names, att_values)}

    def extract_all_abilities_from_text(self) -> Dict[str, str]:
        """Extracts all roll20 character abilities from English text.

        Returns:
            Dict[str, str]: dictionary of the ability names and their rank.
        """
        all_abilities = self._extract_string_between_keywords("abilities", "traits", 1).strip("., ").replace(".", ",")
        if all_abilities in ["-", None, "", " "]:
            return {"Abilities found in text": "Zero"}
        all_abilities = [a.strip() for a in all_abilities.split(",")]
        all_abilities = {
            self._capitalize_ability_name(a.split("(")[0].strip()): a.split("(")[1].strip(") ")
            for a in all_abilities
        }
        return all_abilities

    def extract_equipment_from_text(self) -> str:
        """Extracts all roll20 character equipment from English text.

        Returns:
            str: string with the equipment.
        """
        equipment = self._extract_string_between_keywords("equipment", "shadow", 1)
        equipment = self._cleanup_dice_rolls(equipment)
        return equipment

    def extract_armor_from_text(self) -> str:
        """Extracts, if possible, the roll20 character armor value from English text.
        Usually this is based on equipment and sometimes additional traits.
        Just using the equipment, this works well for German texts. However, applying
        values from traits has not been implemented. English texts are non-standard
        in this regard and armor is difficult to extract from them.
        Alas this is just a dummy, because so far we have not found a way to reliably
        extract armor from English text.

        Returns:
            str: dummy string with the armor value of 'UNKNOWN'.
        """
        return "UNKNOWN"

    def extract_traits_from_text(self) -> str:
        """Extracts, the roll20 character traits from English text.

        Returns:
            str: string with the traits.
        """
        traits = self._extract_string_between_keywords("traits", "integrated")
        return self._clean_roman_numerals(traits)

    def extract_tactics_from_text(self) -> str:
        """Extracts the tactics from the English text.

        Returns:
            str: the extracted tactics string.
        """
        tactics_str = "tactics:"
        return self._extract_from_start_token_until_end(tactics_str)

    def _get_all_attribute_values_from_text(self) -> List[str]:
        """Returns all the attribute values from English text.

        Returns:
            List[str]: list of the attribute values without any names.
        """
        att_values = self._extract_raw_attribute_values()
        att_values_clean = self._clean_filler_characters(att_values)
        att_values_clean = self._clean_misrecognized_plus_characters(att_values_clean)
        att_values_clean = self._express_attributes_as_decimal(att_values_clean)
        return att_values_clean

    @staticmethod
    def _capitalize_ability_name(ability_name: str) -> str:
        """Capitalizes the ability name. Leaves hyphens or dashes etc
        untouched and only capitalizes words separated by whitespaces.

        Args:
            ability_name (str): the roll20 ability name extracted from the text.

        Returns:
            str: the capitalized ability name.
        """
        ability_name = ability_name.split()
        ability_name = " ".join([a.capitalize() for a in ability_name])
        return ability_name

    def _extract_raw_attribute_values(self) -> str:
        """Extracts the raw attribute values from preprocessed English text.

        Returns:
            str: the raw attribute values without any cleaning applied.
        """
        att_values = self._extract_string_between_keywords("vig", "defense", 0)
        return att_values

    @staticmethod
    def _clean_filler_characters(attribute_values: str) -> List[str]:
        """Cleans the attribute values based on the mappings.

        Args:
            attribute_values (str): string of attribute values extracted
            from the OCR'd text with misrecognized / altered characters.

        Returns:
            List[str]: list of cleaned attribute values.
        """
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
            ("o", "0"),
            ("©", "0"),
            (".", " "),
            ("’", " "),
            ("‘", " "),
            ("“", " "),
            ("”", " "),
            ("\"", " "),
            ("\\", " "),
            ("/", " "),
            ("00", "0 0"),    # important to execute this only after the other 0's
        ]
        for k, v in mapping:
            attribute_values = attribute_values.replace(k, v)
        return attribute_values.split()

    @staticmethod
    def _clean_misrecognized_plus_characters(attribute_values: List[str]) -> List[str]:
        """Cleans the attribute values based on the regex match.
        Mainly targets the plus characters that can get misrecognized or even added as additional '4's.

        Args:
            attribute_values (List[str]): list of the attribute values with only '[-+0-9]' characters.

        Returns:
            List[str]: cleaned list of attribute values.
        """
        for i, v in enumerate(attribute_values):
            pattern = r"[+0-9]{2,3}$"
            match = re.search(pattern, v)
            if match:
                attribute_values[i] = "+" + v[-1]
        return attribute_values

    @staticmethod
    def _express_attributes_as_decimal(att_values_clean: List[str]) -> List[str]:
        """Transforms the attribute values, which are expressed as deviations
        from 10 with regards to the player character rolls, into decimal values.
        10 is the average character attribute value.

        5 and 15 are regarded as the general minimum and maximum starting attribute values;
        there can be exceptions for characters based on talents or background story.
        A blind character won't have a very high precision.

        These transformed values can be used as NPC attributes in the roll20 character sheets directly.
        Example: '+5' becomes '5', since the player has a roll with a bonus of
        +5 against that attribute. '-3' becomes '13', since the player has a roll
        with a penalty of 3 against that attribute.

        Args:
            att_values_clean (List[str]): list of cleaned attribute values
            in the 'deviation from 10 notation'.

        Returns:
            List[str]: list of cleaned attribute values in decimal notation.
        """
        att_values_clean = [str((10 - int(v))) for v in att_values_clean]
        return att_values_clean
