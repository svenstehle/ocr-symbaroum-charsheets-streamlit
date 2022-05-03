import time

from seleniumbase import BaseCase
from tests.testing_utils import compare_baseline_actual


class ComponentsTest(BaseCase):
    def test_app_radiobutton(self):
        """Check if we can use our radiobutton without error."""
        test_group = "test_app_radiobutton"
        test_name = f"{test_group}_click"

        self.open("http://localhost:8501")

        # check radiobutton
        # more info on visual testing and selection of elements:
        # https://gitter.im/seleniumbase/SeleniumBase?at=5b889f49d457a1406c87dac9
        # and https://github.com/seleniumbase/SeleniumBase/blob/master/examples/my_first_test.py

        self.click('//*[@id="root"]/div[1]/div/div/div/div/section[1]/div[1]/div[2]/div[1]/div/div[6]/div/div/label[2]')
        time.sleep(4)
        self.check_window(name=test_name, level=2)

        compare_baseline_actual(test_group, test_name)
