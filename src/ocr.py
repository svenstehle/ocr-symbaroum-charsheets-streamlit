# License: APACHE LICENSE, VERSION 2.0

import numpy as np
import pytesseract
from spock.backend.wrappers import \
    Spockspace  # pylint: disable=wrong-import-order


def perform_ocr(ocr_config: Spockspace, lang: str, psm: int, image: np.ndarray) -> str:
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
        f"-l {lang} --psm {psm} --oem {ocr_config.oem} "
        f"-c thresholding_method={ocr_config.thresh} "
        f"-c tessedit_char_whitelist='{ocr_config.whitelist}' "
    )
    text = pytesseract.image_to_string(image, config=options)
    return text
