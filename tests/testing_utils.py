import cv2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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


def set_browser_window_size():
    """"Sets the browser window size to a fixed value so we can have reliable visual tests."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:8501")
    print("Headless Chrome Initialized")
    print(driver.get_window_size())
    driver.set_window_size(1920, 1080)
    size = driver.get_window_size()
    print(f"Window size: width = {size['width']}px, height = {size['height']}px")
    driver.quit()
