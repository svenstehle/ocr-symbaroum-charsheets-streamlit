from seleniumbase import BaseCase


class ComponentsTest(BaseCase):
    """Basic test to debug and make sure we can display a webpage at all."""
    def test_app_startup(self):
        self.open("http://www.google.com")
        self.assert_text("Google")
