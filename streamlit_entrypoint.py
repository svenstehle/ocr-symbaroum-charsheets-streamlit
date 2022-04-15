import os

import numpy as np
import streamlit as st

from src.image_processing import (load_image, load_image_from_file, reorder_color_channels)
from src.ocr import text_detection_and_recognition
from src.spock_config import setup_spock
from src.streamlit_setup import file_selector, start_streamlit


def main():
    config = setup_spock()
    ocr_cfg = config.OCRConfig

    start_streamlit()

    st.header("OCR for Symbaroum Charactersheets with Streamlit")
    filename = None
    image = None

    if st.checkbox("Upload Image", key="upload_image_from_disk"):
        image_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg", "webp"])
        if image_file is not None:
            im_pil = load_image_from_file(image_file)
            file_details = {"filename": image_file.name, "filetype": image_file.type, "filesize": image_file.size}
            st.info("File Details:")
            st.write(file_details)

            st.info("This is the Image you uploaded:")
            st.image(im_pil, width=450)

            # To use it in the OCR part
            image = np.asarray(im_pil)
            image = reorder_color_channels(image)

    elif st.checkbox("Select Image from filesystem", key="select_image_path"):
        # Select a file
        st.write("Select a file in a directory")
        folder_path = f"{os.getcwd()}"
        folder_path = st.text_input("Enter folder path", folder_path)
        filename = file_selector(folder_path=folder_path)
        st.info(f"You selected {filename}")

    st.write("Do you want to perform OCR on the selected image?")
    if st.button("Yes, start OCR"):
        with st.spinner("Performing OCR on image ..."):
            if filename and not image:
                # with st.spinner(f"Performing OCR on file: '{filename}' ..."):
                image = load_image(filename)

            text = text_detection_and_recognition(ocr_cfg, image)

        st.write("OCR OUTPUT")
        st.info(text)


if __name__ == "__main__":
    main()

#TODO format text on streamlit for roll20 charsheet creation with one attribute
#TODO extract more attributes in a roll20-copy-paste-friendly way

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
