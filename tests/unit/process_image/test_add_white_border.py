from src.process_image import ImageProcessor


def test_add_white_border(prep_grayscale_img_arr):
    IP = ImageProcessor(bordersize=25)
    IP.img = prep_grayscale_img_arr
    IP.add_white_border()
    assert IP.img.shape == (150, 150)
