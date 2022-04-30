import pytest
from hydra import compose, initialize
from omegaconf import OmegaConf
from src.process_image import ImageProcessor


@pytest.fixture(scope="session")
def prep_ocr_image():
    image_path = "tests/unit/ocr/easy_img.png"
    IP = ImageProcessor()
    IP.get_processed_image(image_path)
    yield IP.img
    del IP


@pytest.fixture(scope="module")
def prep_hydra_config():
    # context initialization
    with initialize(config_path="../src/conf", job_name="test_app"):
        cfg = compose(config_name="config", overrides=["testing=enabled"])
        print(OmegaConf.to_yaml(cfg))
        yield cfg
        del cfg
