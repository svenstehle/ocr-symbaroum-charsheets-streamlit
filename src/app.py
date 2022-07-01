# License: APACHE LICENSE, VERSION 2.0
#

import hydra
from omegaconf import DictConfig

from src.streamlit_handlers.image_handler import image_handler
from src.streamlit_handlers.information_extraction_handler import \
    information_extraction_handler
from src.streamlit_handlers.ocr_handler import ocr_handler
from src.streamlit_handlers.sidebar_handler import sidebar_handler


@hydra.main(config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    """Entry point for the streamlit OCR app.
    You can upload an image with the streamlit file_uploader that is part of the 'setup_sidebar'.
    OCR will be performed on this image.
    Then, the text will be processed and roll20 symbaroum relevant information
    will be extracted and presented to the user.
    """
    # setup the Streamlit sidebar
    image_file, factor, psm = sidebar_handler(cfg)

    # handle image processing and display results in Streamlit
    image = image_handler(cfg, image_file, factor)

    # OCR part
    ocr_handler(cfg, image, psm)

    # information extraction part - create roll20 string
    information_extraction_handler(cfg)

    # TODO ~add block of text with everything from weapons till tactics, corrected
    # (english only) with blank lines -> roll20 gm_notes can be filled with everything!?


if __name__ == "__main__":
    main()    # pylint: disable=no-value-for-parameter
