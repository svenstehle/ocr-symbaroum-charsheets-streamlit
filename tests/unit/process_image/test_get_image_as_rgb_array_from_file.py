from src.process_image import get_image_as_rgb_array_from_file


def test_get_image_as_rgb_array_from_file():
    image_path = "tests/unit/process_image/cat.jpeg"
    image = get_image_as_rgb_array_from_file(image_path)
    assert image.shape == (1497, 1000, 3)
