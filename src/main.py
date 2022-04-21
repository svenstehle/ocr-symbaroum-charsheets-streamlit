# License: APACHE LICENSE, VERSION 2.0

from ocr import text_detection_and_recognition
from process_image import ImageProcessor
from spock_config import load_configuration


def main():
    config = load_configuration()
    ocr_cfg = config.OCRConfig
    IP = ImageProcessor()
    image = IP.get_processed_image(ocr_cfg.image)
    text = text_detection_and_recognition(ocr_cfg, ocr_cfg.debug_lang, ocr_cfg.debug_psm, image)

    print("ORIGINAL")
    print("========")
    print(text)
    print("")


if __name__ == "__main__":
    main()
