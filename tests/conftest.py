import pytest
from spock import SpockBuilder
from src.process_image import ImageProcessor
from src.spock_config import ExtractionConfig, OCRConfig


@pytest.fixture(scope="session")
def prep_ocr_image():
    image_path = "tests/unit/ocr/easy_img.png"
    IP = ImageProcessor()
    IP.get_processed_image(image_path)
    yield IP.img
    del IP


@pytest.fixture(scope="session")
def prep_spock_config():
    config = SpockBuilder(
        OCRConfig,
        ExtractionConfig,
        desc="OCR config",
        no_cmd_line=True,
        configs=['tests/testing_config.yaml'],
    ).generate()
    ocr_cfg = config.OCRConfig
    yield ocr_cfg
    del ocr_cfg
