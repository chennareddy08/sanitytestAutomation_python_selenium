import unittest,time,os,csv,re
import string
import random
from ddt import ddt, data, unpack
from selenium import webdriver
from . import  booking_functions
from .basetestcase import BaseTestCase
from . import base_function,booking_functions
from selenium.webdriver.support.ui import Select


class Zipcodetest(BaseTestCase):

    # def test_zipcodehs(self):
    #     """
    #      Test case to verify zipcode
    #     """
    #     target=booking_functions.Booking(self.driver)
    #     filename = 'zipcodehs.csv'
    #
    #     with open(filename, 'rb') as f:
    #         mycsv = csv.reader(f)
    #         mycsv = list(mycsv)
    #         for j in range(0, 6831):
    #             line_number = j
    #             try:
    #                 for i in range(line_number):
    #                     a = mycsv[line_number][i]
    #                     self.driver.find_element_by_id("home-zip-code").clear()
    #                     target.zipcode_field().send_keys(a)
    #                     self.driver.find_element_by_xpath("//button[@type='submit']").click()
    #                     self.driver.implicitly_wait(2)
    #                     url = self.driver.current_url
    #                     b1 = url.split('/')[3]
    #                     b2 = re.sub(r'[^\w]', ' ', b1)
    #                     #b3 = re.sub("\d+", "", b2)
    #
    #                     try:
    #                         e1=self.driver.find_element_by_css_selector("#app-layout > section.lost > h1")
    #                         if self.driver.find_element_by_css_selector("#app-layout > section.lost > h1").is_displayed():
    #                             print ("e1.txt",'-',a)
    #
    #                         else:    pass
    #                     except:
    #                         print(b2,'--',a)
    #                         self.driver.back()
    #                     #self.driver.find_element_by_css_selector("#omkar1589top-nav > div > nav.left > a:nth-child(1)").click()
    #
    #             except:
    #                 pass
    # #
    # def test_zipcodeoc(self):
    #     """
    #      Test case to verify zipcode
    #     """
    #     target = booking_functions.Booking(self.driver)
    #     filename = 'zipcode.csv'
    #
    #     with open(filename, 'rb') as f:
    #         mycsv = csv.reader(f)
    #         mycsv = list(mycsv)
    #         for j in range(0, 297):
    #             line_number = j
    #             try:
    #                 for i in range(line_number):
    #                     a = mycsv[line_number][i]
    #                     self.driver.find_element_by_id("home-zip-code").clear()
    #                     target.zipcode_field().send_keys(a)
    #                     self.driver.find_element_by_xpath("//button[@type='submit']").click()
    #                     self.driver.implicitly_wait(2)
    #                     url = self.driver.current_url
    #                     b1 = url.split('/')[3]
    #                     b2 = re.sub(r'[^\w]', ' ', b1)
    #                     #b3 = re.sub("\d+", "", b2)
    #
    #                     try:
    #                         e1 = self.driver.find_element_by_css_selector("#app-layout > section.lost > h1")
    #                         if self.driver.find_element_by_css_selector("#app-layout > section.lost > h1").is_displayed():
    #                             print ("e1.txt", '-', a)
    #                         else:
    #                             pass
    #                     except:
    #                         print(b2, '--', a)
    #                         self.driver.back()
    #             except:
    #                 pass
    #
    #
    # def test_zipcode_boston(self):
    #     """
    #      Test case to verify zipcode
    #     """
    #     target=booking_functions.Booking(self.driver)
    #     filename = 'zpcodes_boston.csv'
    #
    #     with open(filename, 'rb') as f:
    #         mycsv = csv.reader(f)
    #         mycsv = list(mycsv)
    #         for j in range(0, 1634):
    #             line_number = j
    #             try:
    #                 for i in range(line_number):
    #                     a = mycsv[line_number][i]
    #                     self.driver.find_element_by_id("home-zip-code").clear()
    #                     target.zipcode_field().send_keys(a)
    #                     self.driver.find_element_by_xpath("//button[@type='submit']").click()
    #                     #target.findTrainer_button().click()
    #                     self.driver.implicitly_wait(2)
    #                     url = self.driver.current_url
    #                     print(url)
    #                     b1 = url.split('/')[3]
    #                     b2 = re.sub(r'[^\w]', ' ', b1)
    #                     #b3 = re.sub("\d+", "", b2)
    #
    #                     try:
    #                         e1=self.driver.find_element_by_css_selector("#app-layout > section.lost > h1")
    #                         if self.driver.find_element_by_css_selector("#app-layout > section.lost > h1").is_displayed():
    #                             print ("e1.txt",'-',a)
    #
    #                         else:    pass
    #                     except:
    #                         print(b2,'--',a)
    #                         self.driver.back()
    #             except:
    #                 pass
    # def test_zipcodehs(self):
    #     """
    #      Test case to verify zipcode
    #     """
    #     target=booking_functions.Booking(self.driver)
    #     filename = 'zipcodehs.csv'
    #
    #     with open(filename, 'rb') as f:
    #         mycsv = csv.reader(f)
    #         mycsv = list(mycsv)
    #         for j in range(0, 6831):
    #             line_number = j
    #             try:
    #                 for i in range(line_number):
    #                     a = mycsv[line_number][i]
    #                     self.driver.find_element_by_id("home-zip-code").clear()
    #                     target.zipcode_field().send_keys(a)
    #                     self.driver.find_element_by_xpath("//button[@type='submit']").click()
    #                     self.driver.implicitly_wait(2)
    #                     url = self.driver.current_url
    #                     b1 = url.split('/')[3]
    #                     b2 = re.sub(r'[^\w]', ' ', b1)
    #                     #b3 = re.sub("\d+", "", b2)
    #
    #                     try:
    #                         e1=self.driver.find_element_by_css_selector("#app-layout > section.lost > h1")
    #                         if self.driver.find_element_by_css_selector("#app-layout > section.lost > h1").is_displayed():
    #                             print ("e1.txt",'-',a)
    #
    #                         else:    pass
    #                     except:
    #                         print(b2,'--',a)
    #                         self.driver.back()
    #                     #self.driver.find_element_by_css_selector("#omkar1589top-nav > div > nav.left > a:nth-child(1)").click()
    #
    #             except:
    #                 pass
    #
    def test_zipcodehs(self):
        """
         Test case to verify zipcode
        # """
        target = booking_functions.Booking(self.driver)
        filename = 'zip.csv'

        with open(filename, 'rb') as f:
            mycsv = csv.reader(f)
            mycsv = list(mycsv)
            for j in range(0, 191):
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
                        self.driver.find_element_by_id("phone").send_keys(1234567890)
                        self.driver.find_element_by_id("password").send_keys(11111111)
                        self.driver.find_element_by_id("password-confirm").send_keys(11111111)
                        self.driver.find_element_by_id("field-agree").click()
                        self.driver.find_element_by_xpath(".//*[@id='app-layout']/section[1]/div/form/div/div[3]/button").click()
                        self.driver.implicitly_wait(2)
                        self.driver.find_element_by_name("zip_code").send_keys(a)

                        #self.driver.find_element_by_id("field-agree").click()
                        self.driver.find_element_by_id("inlineRadio1").click()
                        self.driver.find_element_by_id("submit").click()
                        self.driver.implicitly_wait(2)
                        self.driver.find_element_by_xpath("(//input[@name='specialties[]'])[14]").click()
                        self.driver.find_element_by_id("submit").click()
                        self.driver.find_element_by_id("base-nav-link-toggle").click()
                        self.driver.find_element_by_link_text("Logout").click()


                except:
                    pass



    # def test_zipcodehs(self):
    #     """
    #      Test case to verify zipcode
    #     """
    #     target=booking_functions.Booking(self.driver)
    #     filename = 'newyork.csv'
    #
    #     with open(filename, 'rb') as f:
    #         mycsv = csv.reader(f)
    #         mycsv = list(mycsv)
    #         for j in range(0, 1666):
    #             line_number = j
    #             try:
    #                 for i in range(line_number):
    #                     a = mycsv[line_number][i]
    #                     self.driver.find_element_by_id("home-zip-code").clear()
    #                     target.zipcode_field().send_keys(a)
    #                     self.driver.find_element_by_xpath("//button[@type='submit']").click()
    #                     self.driver.implicitly_wait(2)
    #                     url = self.driver.current_url
    #                     b1 = url.split('/')[3]
    #                     b2 = re.sub(r'[^\w]', ' ', b1)
    #                     #b3 = re.sub("\d+", "", b2)
    #
    #                     try:
    #                         e1=self.driver.find_element_by_css_selector("#app-layout > section.lost > h1")
    #                         if self.driver.find_element_by_css_selector("#app-layout > section.lost > h1").is_displayed():
    #                             print ("e1.txt",'-',a)
    #
    #                         else:    pass
    #                     except:
    #                         print(b2,'--',a)
    #                         self.driver.back()
    #                     #self.driver.find_element_by_css_selector("#omkar1589top-nav > div > nav.left > a:nth-child(1)").click()
    #
    #             except:
    #                 pass
    def tearDown(self):
    # close browser window
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()