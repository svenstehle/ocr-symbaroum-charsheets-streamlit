from src.ocr import OCR


def test_detect_text_from_image(create_ocr_test_setup):
    cfg, image, psm = create_ocr_test_setup
    ocr = OCR(cfg, image, psm)
    assert ocr.text == "EMPTY DUMMY: OCR was not yet performed!"
    assert ocr.lang == "deu+eng"
    text = ocr.detect_text_from_image()
    assert text == "Das ist ein Test\n" == ocr.text
    assert ocr.lang == "deu"
