# License: APACHE LICENSE, VERSION 2.0

import pytesseract


def text_detection_and_recognition(ocr_config, lang, psm, image):
    """
    OCR the image at the given path with respective pytesseract arguments.
    """

    options = (
        f"-l {lang} --psm {psm} --oem {ocr_config.oem} "
        f"-c thresholding_method={ocr_config.thresh} "
        f"-c tessedit_char_whitelist='{ocr_config.whitelist}' "
    )
    text = pytesseract.image_to_string(image, config=options)
    return text
