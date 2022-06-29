from src.process_text.process_ocr import TextProcessor


def test_get_lowercase_text():
    TP = TextProcessor("dummy")
    # pylint: disable=protected-access
    lower = TP._get_lowercase_text("Fähigkeiten, test, gRosS ist blablablabla Waffen")
    assert lower == "fähigkeiten, test, gross ist blablablabla waffen"
