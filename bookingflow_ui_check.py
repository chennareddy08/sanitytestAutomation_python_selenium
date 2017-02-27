
import unittest,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from .basetestcase import BaseTestCase
from . import base_function,booking_functions
from selenium.common.exceptions import NoSuchElementException,WebDriverException
from selenium.webdriver.common.keys import Keys


class BookHandstand(BaseTestCase):


    def test_BookWorkout_check(self):
        """
         Test case to verify Book a Workout page
        """
        self.driver.set_window_size(1250,1024)
        target=booking_functions.Booking(self.driver)
        BP=base_function.BasePage(self.driver)
        target.search_trainerfor_booking()
        assert self.driver.find_element_by_css_selector\
            ("#app-layout > section.book-flow > div > form > div > div.book-panel-header.panel-heading > h3").text== 'Book a Workout'
        assert self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > form > div > div.panel-body > div.panel.panel-default > div > div").is_displayed()
        assert self.driver.find_element_by_css_selector\
            ("#app-layout > section.book-flow > div > form > div > div.panel-body > div.panel.panel-default > div > h4").text=="Handstand"
        assert self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > form > div > div.panel-body > div.choose-date > div > label").text=='Choose a Date'
        assert self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > form > div > div.panel-body > div.choose-date > div > div > div").is_displayed()

    def tearDown(self):

        #close browser window
        self.driver.quit()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


if __name__ == "__main__":
    unittest.main()




