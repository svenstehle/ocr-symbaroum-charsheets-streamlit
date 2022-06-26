# License: APACHE LICENSE, VERSION 2.0
#

from abc import ABCMeta, abstractmethod
from typing import List

from src.process_text.process_ocr import TextProcessor


class BaseExtractor(TextProcessor, metaclass=ABCMeta):
    """Abstract base class for Text Extraction."""
    @abstractmethod
    def __init__(self, text: str, attribute_names: List[str]):
        # pylint: disable=super-init-not-called
        self.text = text
        self.attribute_names = attribute_names

    @abstractmethod
    def extract_all_attributes_from_text(self):
        """Extracts all roll20 character attributes from given text."""

    @abstractmethod
    def extract_all_abilities_from_text(self):
        """Extracts all roll20 character abilities from given text."""

    @abstractmethod
    def extract_equipment_from_text(self):
        """Extracts all roll20 character equipment from given text."""

    @abstractmethod
    def extract_armor_from_text(self):
        """Extracts the roll20 armor value from a given text."""

    @abstractmethod
    def extract_traits_from_text(self) -> str:
        """Extracts, the roll20 character traits from given text."""

    @abstractmethod
    def extract_tactics_from_text(self) -> str:
        """Extracts the tactics from the given text."""
