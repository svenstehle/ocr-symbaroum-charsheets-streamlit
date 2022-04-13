import cv2
import pytesseract
from spock import SpockBuilder

from src.spock_config import CFG
from src.translate import translate_text_to


def my_function():
    return 1


def main():
    config = SpockBuilder(CFG, desc='OCR config').generate()

    # load the input image and convert it from BGR to RGB channel
    # ordering
    image = cv2.imread(config.CFG.image)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # OCR the image, supplying the country code as the language parameter
    options = f'-l {config.CFG.lang} --psm {config.CFG.psm} --oem {config.CFG.oem}'

    text = pytesseract.image_to_string(rgb, config=options)
    # show the original OCR'd text
    print("ORIGINAL")
    print("========")
    print(text)
    print("")

    translate_text_to(text, config.CFG.to)


if __name__ == "__main__":
    main()
