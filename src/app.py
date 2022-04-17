# License: APACHE LICENSE, VERSION 2.0

import streamlit as st

from ocr import (
    extract_all_attributes_from_text, extract_all_skills_from_text, extract_tactics_from_text,
    get_roll20_chat_input_str, text_detection_and_recognition
)
from spock_config import load_configuration
from streamlit_helper import (
    display_charname_info, display_ocr_output, display_skills, display_tactics, get_filename_from_user_input,
    get_image_as_rgb_array_from_file, get_radiobutton_selection, is_ocr_cache_present, load_and_display_image
)
from utils import is_filename_supported_image


def main():
    config = load_configuration()
    # TODO make lang a user-input parameter,
    #  maybe with st.radio and smaller language set in tessdata and gitlfs?

    # initialize necessary variables to None
    image = None
    text = None
    ocr_cache_key = "ocr_output"

    # start Streamlit page setup
    st.title("OCR for Symbaroum Charactersheets with Streamlit")
    st.header("Image selection for OCR")
    selection, options = get_radiobutton_selection()

    if selection == options[0]:
        image_file = st.file_uploader("Upload an Image", type=config.StreamlitConfig.supported_image_types)
        if image_file is not None:
            image = get_image_as_rgb_array_from_file(image_file)
            st.info(config.StreamlitConfig.success_response)
        else:
            st.info(config.StreamlitConfig.failure_response)

    if selection == options[1]:
        filename = get_filename_from_user_input()
        if is_filename_supported_image(filename, config.StreamlitConfig.supported_image_types):
            image = load_and_display_image(filename)
            st.info(config.StreamlitConfig.success_response)
        else:
            st.info(config.StreamlitConfig.failure_response)

    if image is not None:
        st.subheader("Perform OCR on selected image?")
        performed_ocr = st.button("Yes, start OCR", key="OCR")
        if performed_ocr:
            with st.spinner("Performing OCR on image ..."):
                text = text_detection_and_recognition(config.OCRConfig, image)
                st.session_state[ocr_cache_key] = text
            display_ocr_output(text)
        elif is_ocr_cache_present(ocr_cache_key) and not performed_ocr:
            st.info("Using cached OCR output. Rerun OCR to update.")

    if is_ocr_cache_present(ocr_cache_key):
        text = st.session_state.get(ocr_cache_key)

        st.header("Roll 20 info extraction")
        with st.form("roll20-setattr"):

            if text is not None:
                charname = st.text_input("Enter the character name you want to set attributes for", "Ironman")
                button_clicked = st.form_submit_button(
                    "Create Roll20 chat string for selected character; using cached OCR output"
                )

                if button_clicked:
                    attributes = extract_all_attributes_from_text(text, config.ExtractionConfig.attribute_names)
                    skills = extract_all_skills_from_text(text)
                    tactics = extract_tactics_from_text(text)
                    setattr_str = get_roll20_chat_input_str(charname, attributes)

                    st.subheader("Roll20 !setattr chat string")
                    display_charname_info(charname)
                    st.code(setattr_str)
                    display_tactics(tactics)
                    display_skills(skills)
                else:
                    st.info("Click the button to create the chat string with provided character name")


if __name__ == "__main__":
    main()

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
