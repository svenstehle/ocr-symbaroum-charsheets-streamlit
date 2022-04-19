# License: APACHE LICENSE, VERSION 2.0

from typing import List, Optional

from spock import SpockBuilder, spock
from spock.backend.typed import SavePath


@spock
class OCRConfig:
    """Basic OCR configuration

    Attributes:
        image: path to an image file to read in and perform ocr on
        save_path: path to save the spock config information
        debug_lang: ocr language to use, relevant for manual debug and dev
        to: language to translate the ocr'd text to
        debug_psm: Tesseract PSM mode, relevant for manual debug and dev
        oem: Tesseract OCR Engine mode, read the docs for more info

    """

    image: str
    save_path: SavePath
    debug_lang: Optional[str] = "deu"
    to: Optional[str] = "en"
    debug_psm: Optional[int] = 4
    oem: Optional[int] = 3


@spock
class StreamlitConfig:
    """
    Streamlit configuration

    Attributes:
        supported_image_types: list of supported image type extensions
        failure_response: message to display if no supported image is selected
        success_response: message to display if a supported image is selected

    """

    supported_image_types: List[str] = ["png", "jpg", "jpeg", "webp"]
    failure_response: str = "No supported Image file selected!"
    success_response: str = "Compatible Image file selected!"


@spock
class ExtractionConfig:
    """
    Config for roll20 attribute extraction

    Attributes:
        attribute_names_ger: list of German attribute names to extract from the text
        attribute_names_eng: list of English attribute names to extract from the text
    """

    attribute_names_ger: List[str]
    attribute_names_eng: List[str]


def load_configuration():
    config = SpockBuilder(OCRConfig, StreamlitConfig, ExtractionConfig, desc="OCR config",
                          configs=["src/config.yaml"]).save(
                              file_extension=".toml",
                              file_name="ocr_config",
                              create_save_path=True,
                          ).generate()
    return config
