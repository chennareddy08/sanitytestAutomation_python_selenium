import unittest,time,os,csv,re
import string
import random
from .basetestcase import BaseTestCase
from . import base_function,booking_functions
from selenium.webdriver.support.ui import Select


class Zipcodetest(BaseTestCase):


    def test_zipcodehs(self):
        """
         Test case to verify zipcode
        """
        target = booking_functions.Booking(self.driver)
        filename = 'boston.csv'

        with open(filename, 'rb') as f:
            mycsv = csv.reader(f)
            mycsv = list(mycsv)
            for j in range(0, 704):
                line_number = j
                try:
                    for i in range(line_number):
                        a = mycsv[line_number][i]
                        a1=mycsv[line_number][i]+"@gmail.com"
                        self.driver.find_element_by_link_text("Apply to be a trainer").click()
                        self.driver.implicitly_wait(1)
                        self.driver.find_element_by_id("first_name").send_keys(random.choice(string.digits))
                        self.driver.find_element_by_id("last_name").send_keys(random.choice(string.digits))
                        self.driver.find_element_by_id("email").send_keys(a1)
                        self.driver.find_element_by_id("phone").send_keys(11234567890)
                        self.driver.find_element_by_id("password").send_keys(11111111)
                        self.driver.find_element_by_id("password-confirm").send_keys(11111111)
                        self.driver.find_element_by_id("field-agree").click()
                        self.driver.find_element_by_css_selector("button.ui-button").click()
                        self.driver.implicitly_wait(2)
                        self.driver.find_element_by_name("zip_code").send_keys(a)
                        self.driver.find_element_by_id("inlineRadio1").click()
                        self.driver.find_element_by_id("submit").click()
                        self.driver.implicitly_wait(2)
                        self.driver.find_element_by_xpath("(//input[@name='specialties[]'])[10]").click()
                        self.driver.find_element_by_id("submit").click()
                        self.driver.implicitly_wait(2)
                        self.driver.find_element_by_css_selector("#base-nav-link-toggle").click()
                        self.driver.find_element_by_link_text("Logout").click()
                        self.driver.implicitly_wait(2)
                except:
                    pass


    def tearDown(self):
    # close browser window
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()