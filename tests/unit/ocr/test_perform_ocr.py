from src.ocr import OCR


def test_perform_ocr(create_ocr_test_setup):
    cfg, image, psm = create_ocr_test_setup
    ocr = OCR(cfg, image, psm)
    assert ocr.text == "EMPTY DUMMY: OCR was not yet performed!"
    assert ocr.lang == "deu+eng"
    ocr.perform_ocr()
    out = ocr.text.strip()
    assert "Das ist ein Test" == out
    assert ocr.lang == "deu+eng"    # since we dont update the languages here
