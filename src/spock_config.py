from typing import Optional

from spock import SpockBuilder, spock
from spock.backend.typed import SavePath


@spock
class OCRConfig:
    """Basic OCR configuration

    Attributes:
        image: path to an image file to read in and perform ocr on
        save_path: path to save the spock config information
        lang: text language that is expected to be present in the image
        to: language to translate the ocr'd text to
        psm: Tesseract PSM mode, read the docs for more info
        oem: Tesseract OCR Engine mode, read the docs for more info

    """

    image: str
    save_path: SavePath
    lang: Optional[str] = "deu"
    to: Optional[str] = "en"
    psm: Optional[int] = 4
    oem: Optional[int] = 3


def setup_spock():
    config = SpockBuilder(OCRConfig, desc="OCR config", configs=["src/config.yaml"]).save(
        file_extension=".toml",
        file_name="ocr_config",
        create_save_path=True,
    ).generate()
    return config
