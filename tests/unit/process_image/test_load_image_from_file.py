from PIL import Image
from src.process_image import ImageProcessor


def test_load_image_from_file(prep_image_path):
    image_path = prep_image_path
    IP = ImageProcessor()
    IP.load_image_from_file(image_path)
    result = IP.img
    assert result.size == (1000, 1497)
    assert result.layers == 3


def test_load_image_from_file_clipboard(prep_image_path):
    image_path = prep_image_path
    IP = ImageProcessor()
    image = Image.open(image_path)
    # in this case we already loaded a PIL image from clipboard
    IP.load_image_from_file(image)
    result = IP.img
    assert result.size == (1000, 1497)
    assert result.layers == 3
