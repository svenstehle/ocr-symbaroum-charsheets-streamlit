from src.process_image import load_image_from_file


def test_load_image_from_file(prep_image_path):
    image_path = prep_image_path
    image = load_image_from_file(image_path)
    assert image.size == (1000, 1497)
    assert image.layers == 3
