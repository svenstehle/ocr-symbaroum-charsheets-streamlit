# License: APACHE LICENSE, VERSION 2.0
from typing import Tuple, Union

import numpy as np
import streamlit as st
from omegaconf import DictConfig

from ocr import OCR
from process_image import (accepted_image_types, processed_image_types, upload_image_types)
from process_text.extract_info import InformationExtractor
from utils import get_processed_image_file


def setup_sidebar(cfg: DictConfig) -> Tuple[upload_image_types, float, int]:
    """Sidebar setup in streamlit app.
    1. Can load an image from the file_uploader
    2. Can set the rescale factor for the image for zoom/shrink operations during processing.
        Returns default if no user action is taken.
    3. Can set the tesseract OCR page segmentation mode.
        Returns default if no user action is taken.

    Args:
        cfg (DictConfig): hydra config object

    Returns:
        Tuple[upload_image_types, float, int]: the image file (None if no image is loaded),
        the rescale factor, and the OCR mode.
    """
    image_file = setup_image_selection(cfg)
    factor = get_rescale_factor()
    psm = setup_ocr_mode_selection()
    return image_file, factor, psm


def image_handler(cfg: DictConfig, image_file: accepted_image_types, factor: float) -> processed_image_types:
    """Handles the image processing and rescaling based on the factor
    provided by the use via the streamlit slider.

    Args:
        cfg (DictConfig): the hydra config object
        image_file (accepted_image_types): the image file to process.
            Either a file object or a path to an image
        factor (float): the rescale factor to zoom/shrink the image with.

    Returns:
        processed_image_types: the processed image file or at start of the app the default None.
    """
    # Streamlit middle page setup
    st.title("OCR for Symbaroum Charactersheets with Streamlit")

    image = None
    if image_file:
        image = get_processed_image_file(image_file, factor)
        display_selected_image(image)
        st.info(cfg.streamlit.success_response)
    else:
        st.info(cfg.streamlit.failure_response)
    return image


def ocr_handler(cfg: DictConfig, image: Union[None, np.ndarray], psm: int) -> None:
    """Handles the OCR processing. If the user loaded an image,
    the button 'Yes, start OCR' will be present. If the user clicks it, OCR will be performed.
    Output text will be stored in the streamlit session_state (cached).

    Args:
        cfg (DictConfig): hydra config object.
        image (Union[None, np.ndarray]): if provided, the image to perform OCR on.
        psm (int): page segmentation mode for OCR.
    """
    if isinstance(image, np.ndarray):
        st.subheader("Perform OCR on selected image?")
        performed_ocr = st.button("Yes, start OCR", key="OCR")
        if performed_ocr:
            with st.spinner("Performing OCR on image ..."):
                ocr = OCR(cfg, image, psm)
                text = ocr.detect_text_from_image()
                st.session_state[cfg.streamlit.ocr_cache_key] = text
            display_ocr_output(text)
        elif st.session_state.get(cfg.streamlit.ocr_cache_key) and not performed_ocr:
            st.info("Using cached OCR output. Rerun OCR to update.")


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


def get_rescale_factor() -> float:
    """Sets the rescale factor for the image with a slider. Default 1.0

    Returns:
        float: the rescale factor for subsequent image resizing.
    """
    with st.sidebar:
        st.header("Image rescale factor selection")
        rescale_factor = st.sidebar.slider(
            label="Change if OCR results are poor.",
            key="slider_rescale_factor",
            min_value=0.5,
            max_value=3.0,
            value=1.0,
            step=0.25,
        )
    return rescale_factor


def setup_image_selection(cfg: DictConfig) -> upload_image_types:
    """Sets up the image uploader.

    Args:
        cfg (DictConfig): hydra config object

    Returns:
        upload_image_types: the image file returned by file_uploader
    """
    with st.sidebar:
        st.header("Image selection for OCR")
        image_file = st.file_uploader("Upload an Image", type=cfg.streamlit.supported_image_types)
    return image_file


available_options = Tuple[str, str]


def get_ocr_mode_radiobutton_selection() -> Tuple[str, available_options]:
    """Gets the user selected OCR mode. Defaults to options[0].

    Returns:
        Tuple[str, available_options]: tuple of the selected option and the available_options.
    """
    options = ("Assume a single column of text of variable sizes", "Assume a single uniform block of text")
    selection = st.radio(
        label="Choose one that works best for your image.",
        options=options,
    )
    return selection, options


def setup_ocr_mode_selection() -> int:
    """Returns the OCR mode selected by the user. Defaults to 4.

    Returns:
        int: page segmentation mode for OCR that was selected by the user.
    """
    with st.sidebar:
        st.header("Mode selection for OCR")
        mode_selection, mode_options = get_ocr_mode_radiobutton_selection()
        if mode_selection == mode_options[0]:
            psm = 4
        elif mode_selection == mode_options[1]:
            psm = 6
    return psm


def display_selected_image(image: np.ndarray) -> None:
    """Displays the input image with a set width.

    Args:
        image (np.ndarray): the image to display.
    """
    st.subheader("This is the (already preprocessed!) Image you uploaded")
    st.image(image, width=450)


def display_ocr_output(text: str) -> None:
    """Displays the OCR output text in a code block.

    Args:
        text (str): the OCR output text.
    """
    st.subheader("OCR output")
    st.code(text)


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
