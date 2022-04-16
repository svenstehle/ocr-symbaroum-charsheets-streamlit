import os

import numpy as np
import streamlit as st

from src.image_processing import load_image_from_file, reorder_color_channels

# TODO how to test functionality that includes streamlit stuff, especially user inputs?


def file_selector(folder_path=f"{os.getcwd()}") -> str:
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select a file", filenames)
    path = os.path.join(folder_path, selected_filename)
    return path


def get_radiobutton_selection():
    options = ("Select Image from Explorer/Finder or Drag'n'Drop", "Manually select a file in a directory")
    selection = st.radio(
        "How do you want to select your Image",
        options,
    )
    st.subheader(selection)
    return selection, options


def get_image_as_rgb_array_from_file(image_file):
    im_pil = load_image_from_file(image_file)
    st.subheader("This is the Image you uploaded")
    st.image(im_pil, width=450)

    # To use it in the OCR part
    image = np.asarray(im_pil)
    image = reorder_color_channels(image)
    return image


def get_filename_from_user_input():
    folder_path = f"{os.getcwd()}"
    folder_path = st.text_input("Enter folder path", folder_path)
    filename = file_selector(folder_path=folder_path)
    st.subheader("Your selection")
    st.code(f"{filename}")
    return filename


def display_ocr_output(text):
    st.subheader("OCR output")
    st.code(text)


def display_setattr_info(charname):
    setattr_string = f"Created string for character _**{charname}**_. " +\
                                    "Click on the button on the top right of the below cell to copy. " +\
                                    "Paste into Roll20 chat."
    st.write(setattr_string)


def display_tactics(tactics):
    st.subheader("Tactic")
    st.code(tactics)


def display_skills(skills):
    st.subheader("Skills")
    st.write(skills)
