# License: APACHE LICENSE, VERSION 2.0
#
from typing import Dict, List

from omegaconf import DictConfig
from src.process_language import detect_language
from src.process_text.extract_english import EnglishExtractor
from src.process_text.extract_german import GermanExtractor
from src.process_text.process_ocr import TextProcessor


class InformationExtractor(TextProcessor):    # pylint: disable=too-many-instance-attributes
    """Extracts all Information from OCR'd text."""
    def __init__(self, text: str, **kwargs):
        """Constructs all the necessary attributes for the InformationExtractor object.

        Args:
            text (str): raw text from pytesseract OCR.
        """
        super().__init__(text, **kwargs)
        self.text = text
        self._abilities = {"Abilities not found in text": "Zero"}
        self._attributes = {"Attributes not found in text": "Zero"}
        self._tactics: str = ""
        self._setattr_name_str: str = ""
        self._setattr_sel_str: str = ""
        self._token_mod_str: str = ""
        self._lang: str = ""

    @property
    def lang(self) -> str:
        """Detects the language used in the text.

        Returns:
            str: language used in the text.
        """
        self._lang = detect_language(self.text)
        return self._lang

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
            self.extract_information_from_ger_text(charname, cfg.extraction.attribute_names_ger)
        elif self.lang == "en":
            self.extract_information_from_eng_text(charname, cfg.extraction.attribute_names_eng)
        else:
            raise ValueError(f"Detected language {self.lang} not supported")

    def extract_information_from_ger_text(self, charname: str, attribute_names: List[str]) -> None:
        """Extracts information from German text and saves it in the InformationExtractor object.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
            attribute_names (List[str]): list of the attribute names in German language.
        """
        self.preprocess_text()
        self.replace_all_weapon_strings("waffen")
        GE = GermanExtractor(self.text)
        self._abilities = GE.extract_all_abilities_from_text_ger()
        self.transform_attribute_keys_to_english_longhand(GE.extract_all_attributes_from_text_ger(attribute_names))
        self.extract_tactics_from_text("taktik:")
        self.get_roll20_chat_input_strings(charname)

    def extract_information_from_eng_text(self, charname: str, attribute_names: List[str]) -> None:
        """Extracts information from English text and saves it in the InformationExtractor object.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
            attribute_names (List[str]): list of the attribute names in English language.
        """
        self.preprocess_text()
        self.replace_all_weapon_strings("weapons")
        EE = EnglishExtractor(self.text)
        self._abilities = EE.extract_all_abilities_from_text_eng()
        self.transform_attribute_keys_to_english_longhand(EE.extract_all_attributes_from_text_eng(attribute_names))
        self.extract_tactics_from_text("tactics:")
        self.get_roll20_chat_input_strings(charname)

    def preprocess_text(self) -> None:
        """_summary_: Removes all the unnecessary characters from the text."""
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
        self.text = self.get_lowercase_text(self.text)

    def transform_attribute_keys_to_english_longhand(self, attributes: Dict[str, str]) -> None:
        """Transforms the attribute keys from the respective supported languages to
        English longhand. E.g. both 'acc' and 'präzision' will be transformed to 'accurate',
        to allow for easier unified handling of these attributes downstream.

        Args:
            attributes (Dict[str, str]): the transformed attribute dictionary
                with the attribute names (keys) in English longhand.
        """
        attr_new = {}
        mapping = self.get_attribute_mapping_for_language()

        for k, v in mapping.items():
            attr_new[k] = attributes[v]

        self._attributes = attr_new

    def extract_tactics_from_text(self, tactics_str: str) -> None:
        """Extracts the tactics from the text.

        Args:
            tactics_str (str): tactics search keyword in the relevant language.
        """
        length = len(tactics_str)
        tactics_start_loc = self.text.find(tactics_str) + length + 1
        tactics = self.text[tactics_start_loc:]
        tactics = [t.strip() for t in tactics.split(" ") if t.strip() != ""]
        self._tactics = " ".join(tactics)

    def get_roll20_chat_input_strings(self, charname: str) -> None:
        """Creates the roll20 chat input strings for the setattr and token-mod API scripts
        for input character name.

        Args:
            charname (str): name of the roll20 character for which to create the setattr string.
                token-mod does not depend on charname.
        """
        self.create_setattr_str(charname)
        self.create_token_mod_str()

    @staticmethod
    def get_lowercase_text(text: str) -> str:
        """Returns the text in lowercase.

        Args:
            text (str): input text with capital letters.

        Returns:
            str: text with only lowercase letters.
        """
        return text.lower()

    def create_setattr_str(self, charname: str) -> None:
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
        toughness = self.get_toughness(self.attributes)
        setattr_toughness = f" --toughness|{toughness}|{toughness}"

        # store in object
        self._setattr_name_str = setattr_name_beginning + setattr_attributes + setattr_toughness
        self._setattr_sel_str = setattr_sel_beginning + setattr_attributes + setattr_toughness

    def create_token_mod_str(self) -> None:
        """Creates and sets the roll20 token-mod API script string
        as attribute to the InformationExtractor object.
        """
        basic_token_mod_string = "!token-mod {{\n" +\
                                "--set\n" +\
                                    "\tlayer|gmlayer\n" +\
                                    "\tbar1_link|quick\n" +\
                                    "\tbar2_link|toughness\n" +\
                                    "\tbar3_link|accurate\n"
        # TODO we need Defense and Armor computations here and the extracted Abilities,
        # Traits and Equipment
        token_mod_tooltip_string = f"\ttooltip|Att: {self.get_attack_value()}/Def: 13337/ Armor: 13337" +\
                                    "\tABILITIES: blabla" +\
                                    "\tTRAITS: blablabla" +\
                                    "\tEQUIPMENT: blablabla"

        token_mod_ending_string = "\tshow_tooltip|yes" +\
                                    "\tdefaulttoken" +\
                                    "}}"

        # FIXME update README with token-mod
        self._token_mod_str = basic_token_mod_string + token_mod_tooltip_string + token_mod_ending_string

    def get_attribute_mapping_for_language(self) -> Dict[str, str]:
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
            raise ValueError(f"Language {self.lang} not supported.")
        return mapping

    @staticmethod
    def get_toughness(attributes: Dict[str, str]) -> int:
        """Calculates the toughness from the strong attribute in the relevant language.

        Args:
            attributes (Dict[str, str]): extracted attributes from the text.

        Returns:
            int: roll20 symbaroum character toughness value.
        """
        strength_key = "strong"
        strong = int(attributes[strength_key])
        return max((strong, 10))

    def get_attack_value(self) -> str:
        """Returns the value for a physical attack performed by that character.
        Usually this is simply calculated by using the value for 'accuracte'.
        If a character has certain abilities, the attack value might be calculated differently,
        e.g. if a character has the ability 'Iron Fist', attack is calculated as the value for 'strong'.

        Returns:
            str: the attack value.
        """
        return self.attributes["accurate"]
