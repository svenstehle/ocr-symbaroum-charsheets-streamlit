# License: APACHE LICENSE, VERSION 2.0
#
import streamlit as st
from omegaconf import DictConfig
from process_text.extract_info import InformationExtractor


def information_extraction_handler(cfg: DictConfig) -> None:
    """Handles the information extraction based on the user input.
    Only appears as an option if OCR has been run at least once during the session
    and is detected in cache.

    Args:
        cfg (DictConfig): hydra config object.
    """
    text = st.session_state.get(cfg.streamlit.ocr_cache_key)
    if isinstance(text, str):
        st.header("Roll 20 info extraction")
        with st.form("roll20-setattr"):
            charname = st.text_input("Enter the character name you want to set attributes for", "Ironman")
            button_clicked = st.form_submit_button(
                "Create Roll20 chat string for selected character; using cached OCR output"
            )
            if button_clicked:
                extract_and_display_info(cfg, text, charname)
            else:
                st.info("Click the button to create the chat string with provided character name")


def extract_and_display_info(cfg: DictConfig, text: str, charname: str) -> None:
    """Extracts information from the OCR text and displays it in the streamlit app.
    Handles exceptions if the provided text is not of sufficient quality or expected content.

    Args:
        cfg (DictConfig): hydra config object.
        text (str): the raw OCR text.
        charname (str): the character name to display the roll20 information for.
    """
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


def display_information_extraction_exception(e: Exception) -> None:
    """Displays the information extraction exception.

    Args:
        e (Exception): Exception to display at the end of the string.
    """
    st.error(
        (
            "Cannot safely extract information. "
            "OCR quality might be inferior. "
            "Try different settings or a higher resolution image. "
            f"Original exception: {repr(e)}"
        )
    )


def display_charname_info(charname: str) -> None:
    """Displays the info string for the chosen character name.

    Args:
        charname (str): chosen character name.
    """
    charname_info = f"Created string for character _**{charname}**_. " +\
                        "Click on the button on the top right of the below cell to copy. " +\
                        "Paste into Roll20 chat."
    st.write(charname_info)


def display_tactics(tactics: str) -> None:
    """Displays the extracted tactics string.

    Args:
        tactics (str): the string to display.
    """
    st.subheader("Tactics")
    st.code(tactics)


def display_abilities(abilities: dict) -> None:
    """Displays the extracted abilities dictionary.

    Args:
        abilities (dict): the dictionary to display
    """
    st.subheader("Abilities")
    st.write(abilities)
