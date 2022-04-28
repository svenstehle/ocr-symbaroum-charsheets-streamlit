# License: APACHE LICENSE, VERSION 2.0

from ocr import perform_ocr
from process_image import ImageProcessor
from spock_config import load_configuration


def main():
    """loads an image, performs OCR on it and prints the result."""
    config = load_configuration()
    ocr_cfg = config.OCRConfig
    IP = ImageProcessor()
    image = IP.get_processed_image(ocr_cfg.image)
    text = perform_ocr(ocr_cfg, ocr_cfg.debug_lang, ocr_cfg.debug_psm, image)

    print("ORIGINAL")
    print("========")
    print(text)
    print("")


if __name__ == "__main__":
    main()
