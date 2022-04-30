import cv2


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
    assert original.shape == duplicate.shape

    difference = cv2.subtract(original, duplicate)
    blue, green, red = cv2.split(difference)
    assert cv2.countNonZero(blue) <= thresh * blue.sum()
    assert cv2.countNonZero(green) <= thresh * green.sum()
    assert cv2.countNonZero(red) <= thresh * red.sum()
