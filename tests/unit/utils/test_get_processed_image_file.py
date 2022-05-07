import numpy as np
from src.utils import get_processed_image_file


def test_get_processed_image_file(prep_hydra_config):
    cfg = prep_hydra_config
    result = get_processed_image_file(cfg.ocr.pytesseract.image, 1.0)
    assert isinstance(result, np.ndarray)
    assert result.shape == (200, 652)
