import os

import streamlit as st

from src.image_processing import load_image
from src.ocr import text_detection_and_recognition
from src.spock_config import setup_spock
from src.streamlit_setup import file_selector, start_streamlit


def main():
    config = setup_spock()
    ocr_cfg = config.OCRConfig

    start_streamlit()

    st.header("OCR for Symbaroum Charactersheets with Streamlit")

    # Select a file
    st.write("Select a file in a directory")
    folder_path = f"{os.getcwd()}"
    folder_path = st.text_input("Enter folder path", folder_path)
    filename = file_selector(folder_path=folder_path)
    st.info(f"You selected {filename}")

    # if st.checkbox(f"Tick this to perform OCR on '{filename}' ?"):
    st.write("Do you want to perform OCR on the selected file?")
    if st.button("Yes, start OCR"):
        st.info(f"Performing OCR on file: '{filename}' ...")

        image = load_image(filename)
        text = text_detection_and_recognition(ocr_cfg, image)

        st.write("OCR OUTPUT")
        st.info(text)


if __name__ == "__main__":
    main()

#TODO run this on streamlit
#TODO format text on streamlit for roll20 charsheet creation with one attribute
#TODO extract more attributes in a roll20-copy-paste-friendly way
#TODO easy image selection functionality for streamlit or even drag'n'drop

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
