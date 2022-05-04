from src.streamlit_helper import display_information_extraction_exception


def test_display_information_extraction_exception():
    exception = ValueError("This is a test exception")
    display_information_extraction_exception(exception)
