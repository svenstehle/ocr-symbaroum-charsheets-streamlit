# License: APACHE LICENSE, VERSION 2.0
from typing import Union

import numpy as np
import streamlit as st
from ocr import OCR
from omegaconf import DictConfig    # pylint: disable=wrong-import-order


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


def display_ocr_output(text: str) -> None:
    """Displays the OCR output text in a code block.

    Args:
        text (str): the OCR output text.
    """
    st.subheader("OCR output")
    st.code(text)
