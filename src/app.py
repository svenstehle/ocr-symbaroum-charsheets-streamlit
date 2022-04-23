# License: APACHE LICENSE, VERSION 2.0

import streamlit as st

from ocr import perform_ocr
from process_image import ImageProcessor
from process_language import detect_languages, language_mapper_for_tesseract
from process_text import InformationExtractor
from spock_config import load_configuration
from streamlit_helper import (
    display_abilities, display_charname_info, display_information_extraction_exception, display_ocr_output,
    display_selected_image, display_tactics, get_rescale_factor, is_ocr_cache_present, setup_image_selection,
    setup_ocr_mode_selection
)


def main():
    config = load_configuration()

    # initialize necessary variables to None
    image = None
    text = None

    # start Streamlit page setup
    st.title("OCR for Symbaroum Charactersheets with Streamlit")

    # setup sidebar with selections
    image_file = setup_image_selection(config)
    factor = get_rescale_factor()
    if image_file is not None:
        IP = ImageProcessor(factor)
        IP.get_processed_image(image_file)
        image = IP.img
        display_selected_image(image)
        st.info(config.StreamlitConfig.success_response)
    else:
        st.info(config.StreamlitConfig.failure_response)

    psm = setup_ocr_mode_selection()

    # OCR part
    if image is not None:
        st.subheader("Perform OCR on selected image?")
        performed_ocr = st.button("Yes, start OCR", key="OCR")
        if performed_ocr:
            with st.spinner("Performing OCR on image ..."):
                lang = "deu+eng"
                text = perform_ocr(config.OCRConfig, lang, psm, image)
                languages = detect_languages(text)
                languages = language_mapper_for_tesseract(languages)
                if len(languages) == 1:
                    text = perform_ocr(config.OCRConfig, languages[0], psm, image)
                st.session_state[config.StreamlitConfig.ocr_cache_key] = text
            display_ocr_output(text)
        elif is_ocr_cache_present(config.StreamlitConfig.ocr_cache_key) and not performed_ocr:
            st.info("Using cached OCR output. Rerun OCR to update.")

    # information extraction part - create roll20 string
    if is_ocr_cache_present(config.StreamlitConfig.ocr_cache_key):
        text = st.session_state.get(config.StreamlitConfig.ocr_cache_key)

        st.header("Roll 20 info extraction")
        with st.form("roll20-setattr"):

            if text is not None:
                charname = st.text_input("Enter the character name you want to set attributes for", "Ironman")
                button_clicked = st.form_submit_button(
                    "Create Roll20 chat string for selected character; using cached OCR output"
                )
                if button_clicked:
                    try:
                        IE = InformationExtractor(text)
                        IE.extract_information_from_text(
                        # TODO move attributes to one config object and handle inside functions
                            charname,
                            config.ExtractionConfig.attribute_names_ger,
                            config.ExtractionConfig.attribute_names_eng,
                        )
                    except (IndexError, ValueError, KeyError) as e:
                        display_information_extraction_exception(e)
                    else:
                        st.subheader("Roll20 !setattr chat string")
                        display_charname_info(charname)
                        #TODO implement getters so we dont expose object attributes
                        st.code(IE.setattr_str)
                        display_tactics(IE.tactics)
                        display_abilities(IE.abilities)
                else:
                    st.info("Click the button to create the chat string with provided character name")


if __name__ == "__main__":
    main()

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
