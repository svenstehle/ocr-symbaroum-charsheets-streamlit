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
    selection = st.radio(
        "How do you want to select your Image",
        ("Select Image from Explorer/Finder", "Enter path to Image"),
    )
    st.info(f"You selected: {selection}")
    return selection


def get_image_as_rgb_array_from_file(image_file):
    im_pil = load_image_from_file(image_file)
    file_details = {"filename": image_file.name, "filetype": image_file.type, "filesize": image_file.size}
    st.info("File Details:")
    st.write(file_details)

    st.info("This is the Image you uploaded:")
    st.image(im_pil, width=450)

    # To use it in the OCR part
    image = np.asarray(im_pil)
    image = reorder_color_channels(image)
    return image


def get_filename_from_user_input():
    st.write("Select a file in a directory")
    folder_path = f"{os.getcwd()}"
    folder_path = st.text_input("Enter folder path", folder_path)
    filename = file_selector(folder_path=folder_path)
    st.info(f"You selected {filename}")
    return filename
