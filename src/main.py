# License: APACHE LICENSE, VERSION 2.0

import hydra
from omegaconf import DictConfig

from ocr import perform_ocr
from process_image import ImageProcessor


@hydra.main(config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:

    IP = ImageProcessor()
    image = IP.get_processed_image(cfg.ocr.pytesseract.image)
    text = perform_ocr(cfg.ocr, cfg.ocr.pytesseract.debug_lang, cfg.ocr.pytesseract.debug_psm, image)

    print("ORIGINAL")
    print("========")
    print(text)
    print("")


if __name__ == "__main__":
    main()    # pylint: disable=no-value-for-parameter
