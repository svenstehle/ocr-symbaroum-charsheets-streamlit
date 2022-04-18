# License: APACHE LICENSE, VERSION 2.0

import pytesseract


def text_detection_and_recognition(ocr_config, lang, image):
    """
    OCR the image at the given path with respective pytesseract arguments.
    """

    options = f'-l {lang} --psm {ocr_config.psm} --oem {ocr_config.oem}'
    text = pytesseract.image_to_string(image, config=options)
    return text
