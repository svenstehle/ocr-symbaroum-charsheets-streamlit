# License: APACHE LICENSE, VERSION 2.0

import numpy as np
import streamlit as st

# TODO how to test functionality that includes streamlit stuff, especially user inputs?


def setup_image_selection(config):
    with st.sidebar:
        st.header("Image selection for OCR")
        image_file = st.file_uploader("Upload an Image", type=config.StreamlitConfig.supported_image_types)
    return image_file


def get_language_radiobutton_selection():
    options = ("German", "English")
    selection = st.radio(
        label="Sometimes number detection works best in German for English text...",
        options=options,
    )
    return selection, options


def get_ocr_mode_radiobutton_selection():
    options = ("Assume a single column of text of variable sizes", "Assume a single uniform block of text")
    selection = st.radio(
        label="Try one or the other and take the one that works best",
        options=options,
    )
    return selection, options


def setup_ocr_mode_selection():
    with st.sidebar:
        st.subheader("Mode selection for OCR")
        mode_selection, mode_options = get_ocr_mode_radiobutton_selection()
        if mode_selection == mode_options[0]:
            psm = 4
        elif mode_selection == mode_options[1]:
            psm = 6
    return psm


def setup_language_selection():
    with st.sidebar:
        st.subheader("Language selection for OCR")
        lang_selection, lang_options = get_language_radiobutton_selection()
        if lang_selection == lang_options[0]:
            lang = "deu"
        elif lang_selection == lang_options[1]:
            lang = "eng"
    return lang


def display_selected_image(image: np.ndarray):
    st.subheader("This is the Image you uploaded")
    st.image(image, width=450)


def display_ocr_output(text: str):
    st.subheader("OCR output")
    st.code(text)


def display_charname_info(charname: str):
    charname_info = f"Created string for character _**{charname}**_. " +\
                                    "Click on the button on the top right of the below cell to copy. " +\
                                    "Paste into Roll20 chat."
    st.write(charname_info)


def display_tactics(tactics: str):
    st.subheader("Tactics")
    st.code(tactics)


def display_abilities(abilities: dict):
    st.subheader("Abilities")
    st.write(abilities)


def is_ocr_cache_present(ocr_cache_key: str) -> bool:
    return ocr_cache_key in st.session_state
