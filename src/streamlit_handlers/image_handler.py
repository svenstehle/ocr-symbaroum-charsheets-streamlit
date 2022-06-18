# License: APACHE LICENSE, VERSION 2.0
#
import numpy as np
import streamlit as st
from omegaconf import DictConfig
from src.process_image import accepted_image_types, processed_image_types
from src.utils import get_processed_image_file


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


def display_selected_image(image: np.ndarray) -> None:
    """Displays the input image with a set width.

    Args:
        image (np.ndarray): the image to display.
    """
    st.subheader("This is the (already preprocessed!) Image you uploaded")
    st.image(image, width=450)
