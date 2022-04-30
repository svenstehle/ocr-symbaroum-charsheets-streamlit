from src.streamlit_helper import display_information_extraction_exception


def test_display_information_extraction_exception():
    """A function to collect a list of test items based on a set of hardcode testitems"""
    exception = ValueError("This is a test exception")
    display_information_extraction_exception(exception)
