import time, string, random

# from base_function import BasePage
from . import base_function
from .basetestcase import BaseTestCase

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class TestB(BaseTestCase):


    def test_2(self):
        pass

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
