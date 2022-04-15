from src.utils import is_filename_supported_image


def test_is_filename_supported_image(prep_is_filename_supported_image):
    filename, supported_image_types, expected_result = prep_is_filename_supported_image
    result = is_filename_supported_image(filename, supported_image_types)
    assert result == expected_result
