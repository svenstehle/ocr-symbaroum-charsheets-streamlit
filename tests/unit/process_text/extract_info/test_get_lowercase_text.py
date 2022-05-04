from src.process_text.extract_info import get_lowercase_text


def test_get_lowercase_text():
    lower = get_lowercase_text("Fähigkeiten, test, gRosS ist blablablabla Waffen")
    assert lower == "fähigkeiten, test, gross ist blablablabla waffen"
