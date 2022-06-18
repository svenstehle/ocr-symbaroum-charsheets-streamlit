import time

from seleniumbase import BaseCase
from tests.testing_utils import compare_baseline_actual


class StartupTest(BaseCase):
    def test_app_startup(self):
        """Basic test to check if we can connect to our running streamlit app on localhost."""
        test_group = "test_app_startup"
        test_name = f"{test_group}_title"

        self.open("http://localhost:8501")
        time.sleep(5)

        self.check_window(name=test_name, level=2)

        # mid page
        self.assert_text(
            "OCR for Symbaroum Charactersheets with Streamlit",
            '//*[@id="ocr-for-symbaroum-charactersheets-with-streamlit"]'
        )
        self.assert_text(
            "No supported Image file selected!",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]'
            '/div/div[1]/div/div[2]/div/div/div/div/div/p',
        )
        ###
        # sidebar
        ###
        # image selection
        self.assert_text(
            "Image selection for OCR",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[1]/div/div/h2',
        )
        self.assert_text(
            "Upload an Image",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[2]/div/label',
        )
        self.assert_text(
            "Drag and drop file here",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[2]/div/section/div/div/span',
        )
        self.assert_text(
            "PNG, TIFF",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[2]/div/section/div/div/small',
        )
        # image rescaling
        self.assert_text(
            "Image rescale factor selection",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[3]/div/div/h2',
        )
        self.assert_text(
            "Change if OCR results are poor.",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[4]/div/label',
        )
        # ocr mode selection
        self.assert_text(
            "Mode selection for OCR",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[5]/div/div/h2',
        )
        self.assert_text(
            "Choose one that works best for your image.",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[6]/div/label',
        )
        self.assert_text(
            "Assume a single column of text of variable sizes",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[6]/div/div/label[1]/div[2]',
        )
        self.assert_text(
            "Assume a single uniform block of text",
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[6]/div/div/label[2]/div[2]',
        )

        compare_baseline_actual(test_group, test_name)
