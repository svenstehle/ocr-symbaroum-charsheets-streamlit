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
        if st.button("Yes, start OCR", key="OCR"):
            with st.spinner("Performing OCR on image ..."):
                if "ocr_output" not in st.session_state:
                    text = text_detection_and_recognition(ocr_cfg, image)
                    st.session_state["ocr_output"] = text
                else:
                    text = st.session_state["ocr_output"]

            st.write("OCR OUTPUT")
            st.info(text)

    with st.form("roll20-setattr"):
        _ = st.form_submit_button("Create Roll20 Attributes")
        if "ocr_output" in st.session_state:
            text = st.session_state["ocr_output"]

        # TODO refactor these
        # extract attributes from text
        # strong
        strong_val = get_attribute_value_from_text(text, "Stärke")
        st.write(strong_val)

        # quick
        quick_val = get_attribute_value_from_text(text, "Gewandtheit")
        st.write(quick_val)

        # create roll20 !setattr chat-command string
        charname = st.text_input("Enter the character name you want to set attributes for", "Ironman")
        st.write(f"You entered: {charname}. Please copy&paste the following string into your Roll20 chat:")
        st.info(f"!setattr --name {charname} --strong|{strong_val} --quick|{quick_val}")


def get_attribute_value_from_text(text: str, attribute_name: str) -> int:
    attribute_name_len = len(attribute_name)
    att_start_loc = text.find(attribute_name) + attribute_name_len + 1
    att_end_loc = att_start_loc + 3
    att_val = text[att_start_loc:att_end_loc]
    return att_val


if __name__ == "__main__":
    main()

#TODO extract more attributes in a roll20-copy-paste-friendly way

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
