import pytesseract
import streamlit as st


@st.cache(suppress_st_warning=True)
def text_detection_and_recognition(ocr_config, image):
    """
    OCR the image at the given path with respective pytesseract arguments.
    """

    options = f'-l {ocr_config.lang} --psm {ocr_config.psm} --oem {ocr_config.oem}'
    text = pytesseract.image_to_string(image, config=options)
    return text


def get_attribute_value_from_text(text: str, attribute_name: str) -> str:
    attribute_name_len = len(attribute_name)
    att_start_loc = text.find(attribute_name) + attribute_name_len + 1
    att_end_loc = att_start_loc + 2
    att_val = text[att_start_loc:att_end_loc].strip(" ")
    return att_val


def get_all_attribute_names_values_from_text(text: str, attribute_names: str) -> dict:
    return {a: get_attribute_value_from_text(text, a) for a in attribute_names}


def get_roll20_setattr_str(charname, attributes: dict) -> str:
    string = f"!setattr --name {charname} --strong|{attributes['Stärke']} --quick|{attributes['Gewandtheit']}" +\
                f" --vigilant|{attributes['Aufmerksamkeit']} --resolute|{attributes['Willenskraft']}" +\
                f" --persuasive|{attributes['Ausstrahlung']} --cunning|{attributes['Scharfsinn']}" +\
                f" --discreet|{attributes['Heimlichkeit']} --accurate|{attributes['Präzision']}"

    return string
