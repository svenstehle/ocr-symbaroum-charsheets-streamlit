from src.image_processing import load_image


def test_load_image():
    image_path = "tests/unit/image_processing/cat.jpeg"
    image = load_image(image_path)
    assert image.shape == (1497, 1000, 3)
