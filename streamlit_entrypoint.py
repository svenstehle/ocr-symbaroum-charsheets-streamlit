import streamlit as st

from src.image_processing import load_image
from src.ocr import text_detection_and_recognition
from src.spock_config import setup_spock
from src.streamlit_setup import (
    filename_is_supported_image, get_filename_from_user_input, get_image_as_rgb_array_from_file, radio_selector
)


def main():
    config = setup_spock()
    ocr_cfg = config.OCRConfig

    st.header("OCR for Symbaroum Charactersheets with Streamlit")

    failure_response = "No supported Image file selected!"
    success_response = "Compatible Image file selected!"
    image = None
    filename = "dummy"
    # include in SpockConfig
    supported_image_types = ["png", "jpg", "jpeg", "webp"]

    selection = radio_selector()

    if selection == "Select Image from Explorer/Finder":
        image_file = st.file_uploader("Upload an Image", type=supported_image_types)
        if image_file is not None:
            image = get_image_as_rgb_array_from_file(image_file)
            st.write(success_response)
        else:
            st.write(failure_response)

    if selection == "Enter path to Image":
        filename = get_filename_from_user_input()
        if filename_is_supported_image(filename, supported_image_types):
            st.write(success_response)
        else:
            st.write(failure_response)

    if image is not None or filename_is_supported_image(filename, supported_image_types):
        st.write("Do you want to perform OCR on the selected image?")
        if st.button("Yes, start OCR"):
            with st.spinner("Performing OCR on image ..."):
                if image is None:
                    image = load_image(filename)

                text = text_detection_and_recognition(ocr_cfg, image)

            st.write("OCR OUTPUT")
            st.info(text)


if __name__ == "__main__":
    main()

#TODO format text on streamlit for roll20 charsheet creation with one attribute
#TODO extract more attributes in a roll20-copy-paste-friendly way

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
