# License: APACHE LICENSE, VERSION 2.0

import streamlit as st

from ocr import text_detection_and_recognition
from process_image import get_image_as_rgb_array_from_file
from process_text import extract_information_from_text
from spock_config import load_configuration
from streamlit_helper import (
    display_abilities, display_charname_info, display_information_extraction_exception, display_ocr_output,
    display_selected_image, display_tactics, is_ocr_cache_present, setup_image_selection, setup_language_selection,
    setup_ocr_mode_selection
)


def main():
    config = load_configuration()

    # initialize necessary variables to None
    image = None
    text = None
    ocr_cache_key = "ocr_output"

    # start Streamlit page setup
    st.title("OCR for Symbaroum Charactersheets with Streamlit")

    # setup sidebar with selections
    image_file = setup_image_selection(config)
    if image_file is not None:
        image = get_image_as_rgb_array_from_file(image_file)
        display_selected_image(image)
        st.info(config.StreamlitConfig.success_response)
    else:
        st.info(config.StreamlitConfig.failure_response)

    lang = setup_language_selection()
    psm = setup_ocr_mode_selection()

    # OCR part
    if image is not None:
        st.subheader("Perform OCR on selected image?")
        performed_ocr = st.button("Yes, start OCR", key="OCR")
        if performed_ocr:
            with st.spinner("Performing OCR on image ..."):
                text = text_detection_and_recognition(config.OCRConfig, lang, psm, image)
                st.session_state[ocr_cache_key] = text
            display_ocr_output(text)
        elif is_ocr_cache_present(ocr_cache_key) and not performed_ocr:
            st.info("Using cached OCR output. Rerun OCR to update.")

    # information extraction part - create roll20 string
    if is_ocr_cache_present(ocr_cache_key):
        text = st.session_state.get(ocr_cache_key)

        st.header("Roll 20 info extraction")
        with st.form("roll20-setattr"):

            if text is not None:
                charname = st.text_input("Enter the character name you want to set attributes for", "Ironman")
                button_clicked = st.form_submit_button(
                    "Create Roll20 chat string for selected character; using cached OCR output"
                )
                #TODO work on mode_b for adventure book and do try/except
                #  between those two modes for info extraction
                if button_clicked:
                    try:
                        information = extract_information_from_text(
                            text,
                            config.ExtractionConfig.attribute_names_ger,
                            config.ExtractionConfig.attribute_names_eng,
                            charname,
                        )
                    except IndexError as e:
                        display_information_extraction_exception(e)
                    except ValueError as e:
                        display_information_extraction_exception(e)

                    st.subheader("Roll20 !setattr chat string")
                    display_charname_info(charname)
                    st.code(information["setattr_str"])
                    display_tactics(information["tactics"])
                    display_abilities(information["abilities"])
                else:
                    st.info("Click the button to create the chat string with provided character name")


if __name__ == "__main__":
    main()

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
