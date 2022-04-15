import os

import streamlit as st


def file_selector(folder_path=f"{os.getcwd()}") -> str:
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select a file", filenames)
    path = os.path.join(folder_path, selected_filename)
    return path


def start_streamlit():
    pass
