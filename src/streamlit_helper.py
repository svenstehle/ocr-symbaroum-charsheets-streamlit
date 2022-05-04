# License: APACHE LICENSE, VERSION 2.0

from typing import Tuple

import numpy as np
import streamlit as st
from omegaconf import DictConfig

from process_image import upload_image_types


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


def is_ocr_cache_present(ocr_cache_key: str) -> bool:
    """Checks if the key used to cache OCR results as text is present
    in streamlit session state.

    Args:
        ocr_cache_key (str): the key to check for.

    Returns:
        bool: True if key is present, False otherwise.
    """
    return ocr_cache_key in st.session_state


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
