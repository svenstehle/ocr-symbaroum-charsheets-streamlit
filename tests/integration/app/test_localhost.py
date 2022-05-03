from seleniumbase import BaseCase


class ComponentsTest(BaseCase):
    """Basic test to check if we can connect to our running streamlit app on localhost."""
    def test_app_startup(self):
        self.open("http://localhost:8501")
        self.assert_text(
            "OCR for Symbaroum Charactersheets with Streamlit",
            '//*[@id="ocr-for-symbaroum-charactersheets-with-streamlit"]'
        )
