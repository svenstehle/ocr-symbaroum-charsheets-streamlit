from src.ocr import text_detection_and_recognition


def test_text_detection_and_recognition(prep_text_detection_and_recognition):
    ocr_config, lang, psm, image = prep_text_detection_and_recognition
    text = text_detection_and_recognition(ocr_config, lang, psm, image)
    assert "HEALTHCARE\n" in text
