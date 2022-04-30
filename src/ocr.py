# License: APACHE LICENSE, VERSION 2.0

import numpy as np
import pytesseract
from omegaconf import DictConfig


def perform_ocr(ocr_config: DictConfig, lang: str, psm: int, image: np.ndarray) -> str:
    """Perform OCR on the provided image.
    Args:
        ocr_config (Spockspace): spock-config configuration
        lang (str): string of languages to use for OCR, e.g. "deu+eng"
        psm (int): page segmentation mode to use for OCR
        image (np.ndarray): image to perform OCR on
    Returns:
        str: the extracted raw text that has been retrieved from the image
    """

    options = (
        f"-l {lang} --psm {psm} --oem {ocr_config.pytesseract.oem} "
        f"-c thresholding_method={ocr_config.pytesseract.thresh} "
        f"-c tessedit_char_whitelist='{ocr_config.pytesseract.whitelist}' "
    )
    text = pytesseract.image_to_string(image, config=options)
    return text
