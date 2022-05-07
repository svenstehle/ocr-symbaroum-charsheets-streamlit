# License: APACHE LICENSE, VERSION 2.0

import hydra
import streamlit as st
from omegaconf import DictConfig

from process_text.extract_info import InformationExtractor
from streamlit_helper import (
    display_abilities, display_charname_info, display_information_extraction_exception, display_tactics, image_handler,
    is_ocr_cache_present, ocr_handler, setup_sidebar
)


@hydra.main(config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    """Entry point for the streamlit OCR app.
    You can upload an image with the streamlit file_uploader.
    OCR will be performed on this image.
    Then, the text will be processed and roll20 symbaroum relevant information
    will be extracted and presented to the user.
    """
    # initialize necessary variables to None
    image = None
    text = None

    # start Streamlit page setup
    st.title("OCR for Symbaroum Charactersheets with Streamlit")

    # setup the Streamlit sidebar
    image_file, factor, psm = setup_sidebar(cfg)

    # handle image processing and display results in Streamlit
    image = image_handler(cfg, image_file, factor)

    # OCR part
    ocr_handler(cfg, image, psm)

    # information extraction part - create roll20 string
    if is_ocr_cache_present(cfg.streamlit.ocr_cache_key):
        text = st.session_state.get(cfg.streamlit.ocr_cache_key)

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
                        IE.extract_information_from_text(charname, cfg)
                    except (IndexError, ValueError, KeyError) as e:
                        display_information_extraction_exception(e)
                    else:
                        st.subheader("Roll20 !setattr chat string")
                        display_charname_info(charname)
                        st.code(IE.setattr_str)
                        display_tactics(IE.tactics)
                        display_abilities(IE.abilities)
                else:
                    st.info("Click the button to create the chat string with provided character name")


if __name__ == "__main__":
    main()    # pylint: disable=no-value-for-parameter
