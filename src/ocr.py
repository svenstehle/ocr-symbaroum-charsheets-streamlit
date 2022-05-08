# License: APACHE LICENSE, VERSION 2.0

import numpy as np
import pytesseract
from omegaconf import DictConfig

from process_language import get_languages_present_in_text


class OCR:
    """Performs OCR on a provided image,
    i.e. it automatically segments and detects text from an image.
    """
    def __init__(self, cfg: DictConfig, image: np.ndarray, psm: int):
        """Constructs all the necessary attributes for the OCR object.

        Args:
            cfg (DictConfig): hydra cfg object.
            image (np.ndarray): provided image.
            psm (int): page segmentation mode for OCR.
        """
        self.cfg: DictConfig = cfg
        self.image: np.ndarray = image
        self.psm: int = psm
        self.text: str = "EMPTY DUMMY: OCR was not yet performed!"
        self.lang: str = "deu+eng"

    def detect_text_from_image(self) -> str:
        """Detects the text from an image by performing OCR on it.
        Also detects the languages used in the text in a format
        that is understood by tesseracts 'lang' parameter.
        If only one language is detected, repeats OCR with just that language.
        Then returns detected text.

        Returns:
            str: the detected and OCR'd text.
        """
        self.perform_ocr()
        self.lang = get_languages_present_in_text(self.text)
        self.repeat_ocr_if_only_one_language_present()
        return self.text

    def repeat_ocr_if_only_one_language_present(self) -> None:
        """If we have only one language detected,
        we perform OCR again with only that language as the expected language in the image.
        """
        if isinstance(self.lang, str) and len(self.lang) == 3:
            self.perform_ocr()

    def perform_ocr(self) -> None:
        """Perform OCR on the provided image."""
        options = (
            f"-l {self.lang} --psm {self.psm} --oem {self.cfg.ocr.pytesseract.oem} "
            f"-c thresholding_method={self.cfg.ocr.pytesseract.thresh} "
            f"-c tessedit_char_whitelist='{self.cfg.ocr.pytesseract.whitelist}' "
        )
        self.text = pytesseract.image_to_string(self.image, config=options)
