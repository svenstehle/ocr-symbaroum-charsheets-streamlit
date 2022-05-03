import cv2
from selenium import webdriver
from seleniumbase import BaseCase


def compare_baseline_actual(test_group: str, test_name: str, thresh: float = 0.05) -> None:
    """Compares the baseline to the actual screenshot.
    If the differences in the image channels are too large, fail the test.

    Args:
        test_group (str): the test group name
        test_name (str): name of the test
        thresh (float, optional): percentage of pixels that can be different in each channel. Defaults to 0.05.
    """

    original = cv2.imread(f"visual_baseline/{test_group}/{test_name}/baseline.png")
    duplicate = cv2.imread(f"visual_baseline/{test_group}/{test_name}/latest.png")
    print(f"original shape: {original.shape}")
    print(f"duplicate shape: {duplicate.shape}")
    assert original.shape == duplicate.shape

    difference = cv2.subtract(original, duplicate)
    blue, green, red = cv2.split(difference)
    assert cv2.countNonZero(blue) <= thresh * blue.sum()
    assert cv2.countNonZero(green) <= thresh * green.sum()
    assert cv2.countNonZero(red) <= thresh * red.sum()


class WebDriverSetup(BaseCase):
    def get_new_driver(self, *args, **kwargs):
        """ This method overrides get_new_driver() from BaseCase. """
        options = webdriver.ChromeOptions()
        options.add_argument("--force-device-scale-factor=1")    # fix macos retina displays
        if self.headless:
            options.add_argument("--headless")
            # options.add_argument("--disable-gpu")
            # options.add_argument("--window-size=1250,719")
        driver = webdriver.Chrome(options=options)
        width = 1250
        height = 719
        # width = 2500
        # height = 1438
        driver.set_window_size(width, height)
        print('Window size', driver.get_window_size())
        return driver
