import cv2


def compare_baseline_actual(test_group: str, test_name: str, thresh: float = 0.05) -> None:
    """Compares the baseline to the actual screenshot.
    If the differences in the image channels are too large, fail the test.

    **** NOTE ****
    We need to make visual tests compatible with ubuntu and macos vm in GitHub Actions CI.
    Thus, for all visual_baseline screenshots taken on macos retina display, the following settings are needed:
    - True Tone: off
    - Nightshift: off
    - Colour Profile: sRGB IEC61966-2.1     # still need to double check if standard 'Colour LCD' works
    **** NOTE ****

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
