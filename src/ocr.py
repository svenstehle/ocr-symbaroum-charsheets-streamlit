from os import environ

import cv2
import pytesseract
from spock import SpockBuilder

from src.spock_config import OCRConfig


def main():
    save_path = f"{environ.get('PWD')}/runs"
    config = SpockBuilder(OCRConfig, desc="OCR config", config=['src/config.yaml']).save(
        file_extension=".toml",
        user_specified_path=save_path,
        file_name='ocr_config',
        create_save_path=True,
    ).generate()
    ocr_cfg = config.OCRConfig

    # load the input image and convert it from BGR to RGB channel
    # ordering
    image = cv2.imread(ocr_cfg.image)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # OCR the image, supplying the country code as the language parameter
    options = f'-l {ocr_cfg.lang} --psm {ocr_cfg.psm} --oem {ocr_cfg.oem}'

    text = pytesseract.image_to_string(rgb, config=options)
    # show the original OCR'd text
    print("ORIGINAL")
    print("========")
    print(text)
    print("")


if __name__ == "__main__":
    main()
