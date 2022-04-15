import pytest


def create_input_is_filename_supported_image():
    input_result_pairs = [
        ("somepath/somefile.jpg", True),
        ("somepath/somefile.exe", False),
        ("somepath/somefile.png", True),
        ("somepath/somefile.jpeg", True),
        ("somepath/somefile.webp", True),
        ("somepath/somefile.pdf", False),
        ("somepath/somefile.jp", False),
        ("somepath/somefile.web", False),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_is_filename_supported_image())
def prep_is_filename_supported_image(request):
    filename = request.param[0]
    expected_result = request.param[1]
    supported_image_types = ["png", "jpg", "jpeg", "webp"]
    yield filename, supported_image_types, expected_result
    del filename, supported_image_types, expected_result
