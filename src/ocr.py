# import the necessary packages
import argparse

import cv2
import pytesseract

from src.translate import translate_text_to


def my_function():
    return 1


def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
    ap.add_argument("-l", "--lang", required=True, help="language that Tesseract will use when OCR'ing")
    ap.add_argument("-t", "--to", type=str, default="en", help="language that we'll be translating to")
    ap.add_argument("-p", "--psm", type=int, default=4, help="Tesseract PSM mode")
    ap.add_argument("-o", "--oem", type=int, default=3, help="Tesseract OCR Engine mode")
    args = vars(ap.parse_args())

    # load the input image and convert it from BGR to RGB channel
    # ordering
    image = cv2.imread(args["image"])
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # OCR the image, supplying the country code as the language parameter
    options = f'-l {args["lang"]} --psm {args["psm"]} --oem {args["oem"]}'

    text = pytesseract.image_to_string(rgb, config=options)
    # show the original OCR'd text
    print("ORIGINAL")
    print("========")
    print(text)
    print("")

    translate_text_to(text, args["to"])


if __name__ == "__main__":
    main()
