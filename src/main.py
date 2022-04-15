from src.image_processing import load_image
from src.ocr import text_detection_and_recognition
from src.spock_config import setup_spock


def main():
    config = setup_spock()
    ocr_cfg = config.OCRConfig
    image = load_image(ocr_cfg.image)
    text = text_detection_and_recognition(ocr_cfg, image)

    print("ORIGINAL")
    print("========")
    print(text)
    print("")


if __name__ == "__main__":
    main()

#TODO run this on streamlit
#TODO format text on streamlit for roll20 charsheet creation with one attribute
#TODO extract more attributes in a roll20-copy-paste-friendly way
#TODO easy image selection functionality for streamlit or even drag'n'drop

#TODO anywhere along the road: integrate OpenCV bounding boxes or
# image_to_data from tesseract if we need it for better OCR
