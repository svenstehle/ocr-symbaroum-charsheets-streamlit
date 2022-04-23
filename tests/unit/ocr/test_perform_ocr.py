from src.ocr import perform_ocr


def test_perform_ocr(prep_perform_ocr):
    ocr_config, lang, psm, image = prep_perform_ocr
    text = perform_ocr(ocr_config, lang, psm, image)
    assert "Das ist ein Test" in text
