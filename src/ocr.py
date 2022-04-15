import pytesseract
import streamlit as st


@st.cache()
def text_detection_and_recognition(ocr_config, image):
    """
    OCR the image at the given path with respective pytesseract arguments.
    """

    options = f'-l {ocr_config.lang} --psm {ocr_config.psm} --oem {ocr_config.oem}'
    text = pytesseract.image_to_string(image, config=options)
    return text
