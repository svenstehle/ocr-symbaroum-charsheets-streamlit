#
# License: APACHE LICENSE, VERSION 2.0
#

from typing import Tuple

import streamlit as st
from omegaconf import DictConfig
from PIL import ImageGrab
from src.process_image import (CLIPBOARD_IMAGE_TYPES, FILE_UPLOADER_IMAGE_TYPES, accepted_image_types)


def sidebar_handler(cfg: DictConfig) -> Tuple[accepted_image_types, float, int]:
    """Sidebar setup in streamlit app.
    1. Can load an image from the file_uploader
    2. Can set the rescale factor for the image for zoom/shrink operations during processing.
        Returns default if no user action is taken.
    3. Can set the tesseract OCR page segmentation mode.
        Returns default if no user action is taken.

    Args:
        cfg (DictConfig): hydra config object

    Returns:
        Tuple[accepted_image_types, float, int]: the image file (None if no image is loaded),
        the rescale factor, and the OCR page segmentation mode.
    """
    image_uploaded, image_pasted = setup_image_selection(cfg)
    image_file = get_selected_image(image_uploaded, image_pasted)
    factor = get_rescale_factor()
    psm = setup_ocr_mode_selection()
    return image_file, factor, psm


def setup_image_selection(cfg: DictConfig) -> Tuple[FILE_UPLOADER_IMAGE_TYPES, accepted_image_types]:
    """Sets up the image uploader.

    Args:
        cfg (DictConfig): hydra config object

    Returns:
        Tuple[FILE_UPLOADER_IMAGE_TYPES, accepted_image_types]: the image files returned by file_uploader
            and the clipboard handler.
    """
    with st.sidebar:
        st.header("Image selection for OCR")
        image_pasted = clipboard_handler()
        image_uploaded = st.file_uploader("Upload an Image", type=cfg.streamlit.supported_image_types)
    return image_uploaded, image_pasted


def get_selected_image(
    image_uploaded: FILE_UPLOADER_IMAGE_TYPES, image_pasted: accepted_image_types
) -> accepted_image_types:
    """Returns either the image returned by file_uploader or the image pasted from the clipboard,
    depending on the user's radiobutton selection. Defaults to image from clipboard.

    Args:
        image_uploaded (FILE_UPLOADER_IMAGE_TYPES): the file returned from the file_uploader.
        image_pasted (accepted_image_types): the file returned from clipboard_handler.

    Returns:
        accepted_image_types: the image file.
    """
    image_selection = get_image_type_radiobutton_selection()
    if image_selection == "Copied from clipboard":
        image_file = image_pasted
    else:
        image_file = image_uploaded
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
            max_value=5.0,
            value=3.0,
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
        mode_selection = get_ocr_mode_radiobutton_selection()
        if mode_selection == "Assume a single column of text of variable sizes":
            psm = 4
        elif mode_selection == "Assume a single uniform block of text":
            psm = 6
        else:
            raise ValueError("Invalid OCR mode selection")
    return psm


def clipboard_handler() -> accepted_image_types:
    """On the press of a button, loads whatever is currently in the clipboard.
    Returns the image if it is of accepted type. Otherwise returns None.
    Also stores the content in streamlit session_state.

    Returns:
        accepted_image_types: the image present in the clipboard or None.
    """
    clipboard_cache_key = "clipboard_image"
    image = st.session_state.get(clipboard_cache_key)

    copy_paste = st.button("Paste new image from clipboard")
    if copy_paste:
        image = copy_content_from_clipboard()
        st.session_state[clipboard_cache_key] = image

    return image


def get_image_type_radiobutton_selection() -> str:
    """Captures the radiobutton selection for the kind of image to use for OCR.
    Defaults to 'Copied from clipboard'.

    Returns:
        str: the radiobutton selection.
    """
    options = ("Copied from clipboard", "Uploaded from disk")
    with st.sidebar:
        selection = st.radio(
            label="Which kind of image do you want to use?",
            options=options,
        )
    return selection


def get_ocr_mode_radiobutton_selection() -> str:
    """Gets the user selected OCR mode. Defaults to options[0].

    Returns:
        str: the selected option.
    """
    options = ("Assume a single uniform block of text", "Assume a single column of text of variable sizes")
    selection = st.radio(
        label="Choose one that works best for your image.",
        options=options,
    )
    return selection


def copy_content_from_clipboard() -> accepted_image_types:
    """Captures the information present in the clipboard.
    We check if this is an image of accepted type. If it is, we return it.
    Otherwise we return None.

    Returns:
        accepted_image_types: the image of accepted type or None.
    """
    try:
        content = ImageGrab.grabclipboard()
    except NotImplementedError:
        st.info("Only works when you run app.py on your local Windows or macOS")
        content = ImageGrab.grab()

    if not isinstance(content, CLIPBOARD_IMAGE_TYPES):
        response_types = list(t.__module__.split(".")[1][:-6] for t in CLIPBOARD_IMAGE_TYPES)
        st.info(f"No compatible image type in clipboard. Types allowed: \n {response_types}")
        content = None
    return content
