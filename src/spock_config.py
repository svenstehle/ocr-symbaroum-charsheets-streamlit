from typing import Optional

from spock import spock


@spock
class OCRConfig:
    """Basic OCR configuration

    Attributes:
        save_path: path to save the spock config information
        image: path to an image file to read in and perform ocr on
        lang: text language that is expected to be present in the image
        to: language to translate the ocr'd text to
        psm: Tesseract PSM mode, read the docs for more info
        oem: Tesseract OCR Engine mode, read the docs for more info

    """

    image: str
    lang: Optional[str] = "deu"
    to: Optional[str] = "en"
    psm: Optional[int] = 4
    oem: Optional[int] = 3
