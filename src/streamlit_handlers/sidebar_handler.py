# License: APACHE LICENSE, VERSION 2.0
#
from typing import Tuple

import streamlit as st
from omegaconf import DictConfig
from process_image import upload_image_types


def sidebar_handler(cfg: DictConfig) -> Tuple[upload_image_types, float, int]:
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
