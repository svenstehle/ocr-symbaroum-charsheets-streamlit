from os import environ

from spock import SpockBuilder

from src.image_processing import load_image
from src.ocr import text_detection_and_recognition
from src.spock_config import OCRConfig


def main():
    save_path = f"{environ.get('PWD')}/runs"
    config = SpockBuilder(OCRConfig, desc="OCR config", configs=['src/config.yaml']).save(
        file_extension=".toml",
        user_specified_path=save_path,
        file_name='ocr_config',
        create_save_path=True,
    ).generate()

    ocr_cfg = config.OCRConfig
    image = load_image(ocr_cfg.image)
    text = text_detection_and_recognition(ocr_cfg, image)

    print("ORIGINAL")
    print("========")
    print(text)
    print("")


if __name__ == "__main__":
    main()
