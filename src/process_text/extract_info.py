# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, Union

from omegaconf import DictConfig
from src.process_text.extract_english import EnglishExtractor
from src.process_text.extract_german import GermanExtractor
from src.process_text.process_ocr import LanguageNotSupported, TextProcessor

# TODO change all methods in all classes into public and non-public methods in the long run

# TODO reorder functions


class InformationExtractor(TextProcessor):
    # pylint: disable=too-many-instance-attributes
    """Extracts all Information from OCR'd text."""
    def __init__(self, text: str, *args, **kwargs):
        """Constructs all the necessary attributes for the InformationExtractor object.

        Args:
            text (str): raw text from pytesseract OCR.
        """
        super().__init__(text, *args, **kwargs)
        self.text: str = text
        self._abilities: Dict[str, str] = {"Abilities not found in text": "Zero"}
        self._attributes: Dict[str, str] = {"Attributes not found in text": "Zero"}
        self._equipment: str = ""
        self._armor: str = ""
        self._traits: str = ""
        self._tactics: str = ""
        self._setattr_name_str: str = ""
        self._setattr_sel_str: str = ""
        self._token_mod_str: str = ""

    @property
    def abilities(self) -> Dict[str, str]:
        """Returns the abilities extracted from the text.

        Returns:
            Dict[str, str]: the abilities that were extracted from the text.
        """
        return self._abilities

    @property
    def attributes(self) -> Dict[str, str]:
        """Returns the attributes extracted from the text.

        Returns:
            Dict[str, str]: the attributes that were extracted from the text.
        """
        return self._attributes

    @property
    def equipment(self) -> str:
        """Returns the equipment extracted from the text.

        Returns:
            str: the equipment and its features that were extracted from the text.
        """
        return self._equipment

    @property
    def tactics(self) -> str:
        """Returns the tactics extracted from the text.

        Returns:
            str: the tactics that were extracted from the text.
        """
        return self._tactics

    @property
    def setattr_name_str(self) -> str:
        """Returns the roll20 chat input string for the setattr API script
        for character name.

        Returns:
            str: roll20 chat input string.
        """
        return self._setattr_name_str

    @property
    def setattr_sel_str(self) -> str:
        """Returns the roll20 chat input string for the setattr API script
        for selected tokens.

        Returns:
            str: roll20 chat input string.
        """
        return self._setattr_sel_str

    @property
    def token_mod_str(self) -> str:
        """Returns the roll20 chat input string for the token-mod API script
        for selected tokens.

        Returns:
            str: roll20 chat input string.
        """
        return self._token_mod_str

    def extract_information_from_text(self, charname: str, cfg: DictConfig) -> None:
        """Extracts information from the text and saves it in the InformationExtractor object.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
            config (Spockspace): spock-config configuration object.

        Raises:
            ValueError: raised if the detected language of the input text is not supported.
        """
        if self.lang == "de":
            GE = GermanExtractor(self.text, cfg.extraction.attribute_names_ger)
            self._apply_extractor_to_text(GE, charname)
        elif self.lang == "en":
            EE = EnglishExtractor(self.text, cfg.extraction.attribute_names_eng)
            self._apply_extractor_to_text(EE, charname)
        else:
            raise LanguageNotSupported(f"Detected language {self.lang} not supported")

    def _apply_extractor_to_text(
        self,
        extractor: Union[GermanExtractor, EnglishExtractor],
        charname: str,
    ) -> None:
        """Extracts information from German or English text and saves it in the InformationExtractor
        object.

        Args:
            extractor (Union[GermanExtractor, EnglishExtractor]): the Extractor object for the
                extraction part of the respective language.
            charname (str): name of the roll20 character for which to create the setattr string.
        """
        self._preprocess_text()
        self._replace_all_weapon_strings()
        self._abilities = extractor.extract_all_abilities_from_text()
        self._transform_attribute_keys_to_english_longhand(extractor.extract_all_attributes_from_text())
        self._equipment = extractor.extract_equipment_from_text()
        self._armor = extractor.extract_armor_from_text()
        self._traits = extractor.extract_traits_from_text()
        self._tactics = extractor.extract_tactics_from_text()
        self._get_roll20_chat_input_strings(charname)

    def _transform_attribute_keys_to_english_longhand(self, attributes: Dict[str, str]) -> None:
        """Transforms the attribute keys from the respective supported languages to
        English longhand. E.g. both 'acc' and 'präzision' will be transformed to 'accurate',
        to allow for easier unified handling of these attributes downstream.

        Args:
            attributes (Dict[str, str]): the transformed attribute dictionary
                with the attribute names (keys) in English longhand.
        """
        attr_new = {}
        mapping = self._get_attribute_mapping_for_language()

        for k, v in mapping.items():
            attr_new[k] = attributes[v]

        self._attributes = attr_new

    def _get_roll20_chat_input_strings(self, charname: str) -> None:
        """Creates the roll20 chat input strings for the setattr and token-mod API scripts
        for input character name.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
                token-mod does not depend on charname.
        """
        self._create_setattr_str(charname)
        self._create_token_mod_str()

    def _create_setattr_str(self, charname: str) -> None:
        """Creates and sets the roll20 setattr API script string
         as attribute to the InformationExtractor object.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
                token-mod does not depend on charname.
        """
        setattr_name_beginning = f"!setattr --name {charname}"
        setattr_sel_beginning = "!setattr --sel"
        setattr_attributes = ""

        # build the attribute string from attributes
        for att_name, value in self.attributes.items():
            setattr_attributes += f" --{att_name}|{value}"

        # build toughness string
        toughness = self._get_toughness(self.attributes)
        setattr_toughness = f" --toughness|{toughness}|{toughness}"

        # store in object
        self._setattr_name_str = setattr_name_beginning + setattr_attributes + setattr_toughness
        self._setattr_sel_str = setattr_sel_beginning + setattr_attributes + setattr_toughness

    def _create_token_mod_str(self) -> None:
        """Creates and sets the roll20 token-mod API script string
        as attribute to the InformationExtractor object.
        """
        basic_token_mod_string = "!token-mod {{\n" +\
                                "--set\n" +\
                                    "\tlayer|gmlayer\n" +\
                                    "\tbar1_link|quick\n" +\
                                    "\tbar2_link|toughness\n" +\
                                    "\tbar3_link|accurate\n"

        # TODO we need Armor & Defense computations after/during extraction if possible,
        # English charsheets dont have infos on that though

        # convert abilities for tooltip
        abilities_token = tuple(f"{a}:{v}" for a, v in self.abilities.items())
        abilities_token = ", ".join(abilities_token)

        token_mod_tooltip_string = f"\ttooltip|Att: {self._get_attack_value()}" +\
                                    f"/Def: {self._get_defense_value()}" +\
                                    f"/Armor: {self._armor}" +\
                                    f"\tABILITIES: {abilities_token}" +\
                                    f"\tTRAITS: {self._traits}" +\
                                    f"\tEQUIPMENT: {self.equipment}\n"

        token_mod_ending_string = "\tshow_tooltip|yes\n" +\
                                    "\tdefaulttoken\n" +\
                                    "}}"

        self._token_mod_str = basic_token_mod_string + token_mod_tooltip_string + token_mod_ending_string

    def _get_attribute_mapping_for_language(self) -> Dict[str, str]:
        """Returns the mapping of roll20 API script specific values to the
        extracted attribute names in the original language of the ocr'd text.

        Raises:
            ValueError: raised if the detected language of the input text is not supported.

        Returns:
            Dict[str, str]: the mapping from the roll20 API script specific values
            to the attribute names in the text language
        """
        if self.lang == "de":
            mapping = {
                "strong": "stärke",
                "quick": "gewandtheit",
                "vigilant": "aufmerksamkeit",
                "resolute": "willenskraft",
                "persuasive": "ausstrahlung",
                "cunning": "scharfsinn",
                "discreet": "heimlichkeit",
                "accurate": "präzision"
            }
        elif self.lang == "en":
            mapping = {
                "strong": "str",
                "quick": "qui",
                "vigilant": "vig",
                "resolute": "res",
                "persuasive": "per",
                "cunning": "cun",
                "discreet": "dis",
                "accurate": "acc"
            }
        else:
            raise LanguageNotSupported(f"Detected language {self.lang} not supported")
        return mapping

    @staticmethod
    def _get_toughness(attributes: Dict[str, str]) -> int:
        """Calculates the toughness from the strong attribute in the relevant language.

        Args:
            attributes (Dict[str, str]): extracted attributes from the text.

        Returns:
            int: roll20 symbaroum character toughness value.
        """
        strength_key = "strong"
        strong = int(attributes[strength_key])
        return max((strong, 10))

    def _get_attack_value(self) -> str:
        """Returns the value for a physical attack roll performed by that character.
        Usually this is simply calculated by using the value for 'accuracte'.
        If a character has certain abilities, the attack value might be calculated differently,
        e.g. if a character has the ability 'Iron Fist', attack is calculated as the value for 'strong'.
        No other modifiers are factored into this calculation as of right now.

        Returns:
            str: the attack value.
        """
        return self.attributes["accurate"]

    def _get_defense_value(self) -> str:
        """Returns the value for a defense roll performed by that character.
        Usually this is simply calculated by using the value for 'quick'.
        If a character has certain abilities, the defense value might be calculated differently,
        e.g. if a character has the ability 'Iron Fist', defense is calculated as the value for 'strong'.
        Also, modifiers from e.g. 'berserk' could be factored into this in the future.
        Currently, they are not.

        Returns:
            str: the defense value.
        """
        return self.attributes["quick"]
