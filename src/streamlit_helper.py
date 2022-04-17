# License: APACHE LICENSE, VERSION 2.0

import os

import numpy as np
import streamlit as st

from process_image import load_image, load_image_from_file

# TODO how to test functionality that includes streamlit stuff, especially user inputs?


def get_radiobutton_selection():
    options = (
        "Select Image from Explorer/Finder or Drag'n'Drop",
        "Manually select a file in a directory [only works when app is run locally]"
    )
    selection = st.radio(
        label="How do you want to select your Image",
        options=options,
    )
    st.subheader(selection)
    return selection, options


def display_selected_image(image: np.ndarray):
    st.subheader("This is the Image you uploaded")
    st.image(image, width=450)


def get_image_as_rgb_array_from_file(image_file: object) -> np.ndarray:
    im_pil = load_image_from_file(image_file)
    # To use it in the OCR part
    image = np.asarray(im_pil)
    display_selected_image(image)
    return image


def load_and_display_image(filename: str) -> np.ndarray:
    image = load_image(filename)
    display_selected_image(image)
    return image


def file_selector(folder_path: str = f"{os.getcwd()}") -> str:
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select a file", filenames)
    path = os.path.join(folder_path, selected_filename)
    return path


def get_filename_from_user_input() -> str:
    folder_path = f"{os.getcwd()}"
    folder_path = st.text_input("Enter folder path", folder_path)
    filename = file_selector(folder_path=folder_path)
    st.subheader("Your selection")
    st.code(f"{filename}")
    return filename


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
