import cv2
from PIL import Image


def reorder_color_channels(image):
    rgb_channel_ordering = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_channel_ordering


def load_image(image_path: str):
    image = cv2.imread(image_path)
    rgb_channel_ordering = reorder_color_channels(image)
    return rgb_channel_ordering


def load_image_from_file(image_file):
    img = Image.open(image_file)
    return img
