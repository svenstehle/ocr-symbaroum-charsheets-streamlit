from src.ocr import text_detection_and_recognition


def test_text_detection_and_recognition(prep_text_detection_and_recognition):
    ocr_config, image = prep_text_detection_and_recognition
    text = text_detection_and_recognition(ocr_config, image)
    assert text == "HEALTHCARE\n"
