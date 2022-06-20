import time

from seleniumbase import BaseCase
from tests.testing_utils import compare_baseline_actual


class FunctionalityTest(BaseCase):
    def test_app_radiobutton(self):
        """Check if we can use our radiobutton without error."""
        test_group = "test_app_radiobutton"
        test_name = f"{test_group}_click"

        self.open("http://localhost:8501")

        # check bottom radiobutton option, top one should be selected by default
        # more info on visual testing and selection of elements:
        # https://gitter.im/seleniumbase/SeleniumBase?at=5b889f49d457a1406c87dac9
        # and https://github.com/seleniumbase/SeleniumBase/blob/master/examples/my_first_test.py

        # click on the XPATH of the radiobutton
        self.click(
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[6]/div/div/label[2]/div[1]'
        )
        time.sleep(4)
        self.check_window(name=test_name, level=2)
        compare_baseline_actual(test_group, test_name)

    def test_app_file_uploader(self):
        """Check if we can click our uploader without error."""
        test_group = "test_app_file_uploader"
        test_name = f"{test_group}_upload"

        self.open("http://localhost:8501")

        # click on "Browse files" button
        self.click(
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[2]/div/section/button'
        )
        time.sleep(3)
        self.check_window(name=test_name, level=2)

    def test_slider(self):
        """Check if slider movement updates the value as expected."""
        test_group = "test_slider"
        test_name = f"{test_group}_movement"

        self.open("http://localhost:8501")

        xpath_slider_knob = (
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[4]/div/div/div[1]/div/div'
        )
        xpath_slider_current_value = (
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]'
            '/div[1]/div[2]/div/div[1]/div/div[4]/div/div/div[1]/div/div/div'
        )
        # check default slider value is 3.00
        self.assert_text("3.00", f'{xpath_slider_current_value}')

        # move slider 14 times to the left, expected value is 0.50
        self.press_left_arrow(f"{xpath_slider_knob}", times=14)
        self.assert_text("0.50", f'{xpath_slider_current_value}')

        # from that left position move slider 2 + 20 = 22 times to the right, expected value is 5.00
        self.press_right_arrow(f"{xpath_slider_knob}", times=22)
        self.assert_text("5.00", f'{xpath_slider_current_value}')

        time.sleep(2)
        self.check_window(name=test_name, level=2)
        compare_baseline_actual(test_group, test_name)
