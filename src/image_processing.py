import cv2


def load_image(image_path: str):
    image = cv2.imread(image_path)
    rgb_channel_ordering = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_channel_ordering
