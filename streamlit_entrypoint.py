import streamlit as st

from src.image_processing import load_image
from src.ocr import (extract_all_attributes_from_text, get_roll20_chat_input_str, text_detection_and_recognition)
from src.spock_config import load_configuration
from src.streamlit_setup import (
    get_filename_from_user_input, get_image_as_rgb_array_from_file, get_radiobutton_selection
)
from src.utils import is_filename_supported_image


def main():
    config = load_configuration()
    # TODO make lang a user-input parameter,
    #  maybe with st.radio and smaller language set in tessdata and gitlfs?
    ocr_cfg = config.OCRConfig
    st_cfg = config.StreamlitConfig
    extraction_cfg = config.ExtractionConfig

    # initialize necessary variables to None
    image = None
    text = None

    # start Streamlit page setup
    st.header("OCR for Symbaroum Charactersheets with Streamlit")
    selection = get_radiobutton_selection()

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

        if text is not None:
            charname = st.text_input("Enter the character name you want to set attributes for", "Ironman")
            st.write(f"You entered: {charname}. Please copy&paste the following string into your Roll20 chat:")

            attributes = extract_all_attributes_from_text(text, extraction_cfg.attribute_names)
            # TODO add copy paste button
            setattr_str = get_roll20_chat_input_str(charname, attributes)
            st.info(setattr_str)


if __name__ == "__main__":
    main()

#TODO extract more attributes in a roll20-copy-paste-friendly way

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
