from src.process_image import ImageProcessor


def test_load_image_from_file(prep_image_path):
    image_path = prep_image_path
    IP = ImageProcessor()
    IP.load_image_from_file(image_path)
    result = IP.img
    assert result.size == (1000, 1497)
    assert result.layers == 3
