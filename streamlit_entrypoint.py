import streamlit as st

from src.image_processing import load_image
from src.ocr import text_detection_and_recognition
from src.spock_config import setup_spock
from src.streamlit_setup import (get_filename_from_user_input, get_image_as_rgb_array_from_file, radio_selector)
from src.utils import is_filename_supported_image


def main():
    # load configuration
    config = setup_spock()
    ocr_cfg = config.OCRConfig
    st_cfg = config.StreamlitConfig

    # initialize
    image = None

    # start Streamlit page setup
    st.header("OCR for Symbaroum Charactersheets with Streamlit")
    selection = radio_selector()

    if selection == "Select Image from Explorer/Finder":
        image_file = st.file_uploader("Upload an Image", type=st_cfg.supported_image_types)
        if image_file is not None:
            image = get_image_as_rgb_array_from_file(image_file)
            st.write(st_cfg.success_response)
        else:
            st.write(st_cfg.failure_response)

    if selection == "Enter path to Image":
        filename = get_filename_from_user_input()
        if is_filename_supported_image(filename, st_cfg.supported_image_types):
            image = load_image(filename)
            st.write(st_cfg.success_response)
        else:
            st.write(st_cfg.failure_response)

    if image is not None:
        st.write("Do you want to perform OCR on the selected image?")
        if st.button("Yes, start OCR"):
            with st.spinner("Performing OCR on image ..."):
                text = text_detection_and_recognition(ocr_cfg, image)

            st.write("OCR OUTPUT")
            st.info(text)


if __name__ == "__main__":
    main()

#TODO format text on streamlit for roll20 charsheet creation with one attribute
#TODO extract more attributes in a roll20-copy-paste-friendly way

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
