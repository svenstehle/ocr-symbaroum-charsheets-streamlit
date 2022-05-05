from src.process_text.extract_info import InformationExtractor


def test_get_lowercase_text():
    IE = InformationExtractor("dummy")
    lower = IE.get_lowercase_text("Fähigkeiten, test, gRosS ist blablablabla Waffen")
    assert lower == "fähigkeiten, test, gross ist blablablabla waffen"
