# License: APACHE LICENSE, VERSION 2.0

from cv2 import COLOR_BGR2RGB, cvtColor, imread
from PIL import Image


def reorder_color_channels(image):
    rgb_channel_ordering = cvtColor(image, COLOR_BGR2RGB)
    return rgb_channel_ordering


def load_image(image_path: str):
    image = imread(image_path)
    rgb_channel_ordering = reorder_color_channels(image)
    return rgb_channel_ordering


def load_image_from_file(image_file):
    img = Image.open(image_file)
    return img
