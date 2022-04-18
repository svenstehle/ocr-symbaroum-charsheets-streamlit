# License: APACHE LICENSE, VERSION 2.0

import numpy as np
import streamlit as st

# TODO how to test functionality that includes streamlit stuff, especially user inputs?


def get_language_radiobutton_selection():
    options = ("German", "English")
    selection = st.radio(
        label="Main language present in image",
        options=options,
    )
    st.info(f"{selection} language selected!")
    return selection, options


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
    st.subheader("Tactic")
    st.code(tactics)


def display_skills(skills: dict):
    st.subheader("Skills")
    st.write(skills)


def is_ocr_cache_present(ocr_cache_key: str) -> bool:
    return ocr_cache_key in st.session_state
