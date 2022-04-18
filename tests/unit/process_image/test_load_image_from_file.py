from src.process_image import load_image_from_file


def test_load_image_from_file():
    image_path = "tests/unit/process_image/cat.jpeg"
    image = load_image_from_file(image_path)
    assert image.size == (1000, 1497)
    assert image.layers == 3
