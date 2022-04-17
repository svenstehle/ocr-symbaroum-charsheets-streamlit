# License: APACHE LICENSE, VERSION 2.0

from image_processing import load_image
from ocr import text_detection_and_recognition
from spock_config import load_configuration


def main():
    config = load_configuration()
    ocr_cfg = config.OCRConfig
    image = load_image(ocr_cfg.image)
    text = text_detection_and_recognition(ocr_cfg, image)

    print("ORIGINAL")
    print("========")
    print(text)
    print("")


if __name__ == "__main__":
    main()
