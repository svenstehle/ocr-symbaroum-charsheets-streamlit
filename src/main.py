# License: APACHE LICENSE, VERSION 2.0

import hydra
from omegaconf import DictConfig

from ocr import OCR
from process_image import ImageProcessor


@hydra.main(config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    """loads an image, performs OCR on it and prints the result."""
    IP = ImageProcessor()
    image = IP.get_processed_image(cfg.ocr.pytesseract.image)
    ocr = OCR(cfg, image, cfg.ocr.pytesseract.debug_psm)
    ocr.lang = cfg.ocr.pytesseract.debug_lang
    text = ocr.detect_text_from_image()

    print("ORIGINAL")
    print("========")
    print(text)


if __name__ == "__main__":
    main()    # pylint: disable=no-value-for-parameter
