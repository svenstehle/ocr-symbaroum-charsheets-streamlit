import streamlit as st

from src.image_processing import load_image
from src.ocr import (
    extract_all_attributes_from_text, extract_all_skills_from_text, extract_tactics_from_text,
    get_roll20_chat_input_str, text_detection_and_recognition
)
from src.spock_config import load_configuration
from src.streamlit_setup import (
    display_ocr_output, display_setattr_info, display_skills, display_tactics, get_filename_from_user_input,
    get_image_as_rgb_array_from_file, get_radiobutton_selection
)
from src.utils import is_filename_supported_image


def write_image_selection_subheader():
    st.subheader()


def main():
    config = load_configuration()
    # TODO make lang a user-input parameter,
    #  maybe with st.radio and smaller language set in tessdata and gitlfs?

    # initialize necessary variables to None
    image = None
    text = None

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
            image = load_image(filename)
            st.info(config.StreamlitConfig.success_response)
        else:
            st.info(config.StreamlitConfig.failure_response)

    if image is not None:
        st.subheader("Perform OCR on selected image?")
        if st.button("Yes, start OCR", key="OCR"):
            with st.spinner("Performing OCR on image ..."):
                if "ocr_output" not in st.session_state:
                    text = text_detection_and_recognition(config.OCRConfig, image)
                    st.session_state["ocr_output"] = text
                else:
                    text = st.session_state["ocr_output"]

            display_ocr_output(text)

    if text is not None:
        st.header("Roll 20 info extraction")

    with st.form("roll20-setattr"):
        if "ocr_output" in st.session_state:
            text = st.session_state["ocr_output"]

        if text is not None:
            charname = st.text_input("Enter the character name you want to set attributes for", "Ironman")
            button_clicked = st.form_submit_button("Create Roll20 chat string for selected character")

            if button_clicked:
                attributes = extract_all_attributes_from_text(text, config.ExtractionConfig.attribute_names)
                skills = extract_all_skills_from_text(text)
                tactics = extract_tactics_from_text(text)
                setattr_str = get_roll20_chat_input_str(charname, attributes)

                st.subheader("Roll20 !setattr chat string")

                display_setattr_info(charname)
                st.code(setattr_str)
                display_tactics(tactics)
                display_skills(skills)


if __name__ == "__main__":
    main()

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
