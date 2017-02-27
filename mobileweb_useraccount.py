import unittest
from appium import webdriver
import time
from selenium.webdriver.common.keys import Keys


#from base_function import BasePage
from . import base_function
from .basetestcase import BaseTestCase

from selenium.common.exceptions import NoSuchElementException



class TestAccount(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        # platform
        desired_caps['deviceName'] = 'emulator-5554'
        # platform version
        desired_caps['platformVersion'] = '5.1.1'
        #desired_caps['and'] = 'you'

        # mobile browser
        desired_caps['browserName'] = 'Browser'
        desired_caps['platformName']="Android"
        # to connect to Appium server use RemoteWebDriver
        # and pass desired capabilities
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.get('https://www.handstandapp.com/')
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element_by_css_selector("#sumome-welcomemat > input").send_keys("tes1@gmail.com")
            self.driver.find_element_by_css_selector("#sumome-welcomemat > div.sumome-welcomemat-action-submit.sumome-welcomemat-button").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_css_selector("#handstandsapp > div.ui-header.ui-bar-a > a.ui-btn-left.ui-btn.ui-btn-up-.ui-shadow.ui-btn-corner-all.ui-btn-icon-left > span > span.ui-icon.ui-icon-arrow-down-green.ui-icon-shadow").click()
            self.driver.find_element_by_css_selector('#test > div > ul > li:nth-child(1) > a').click()
            self.driver.implicitly_wait(5)
        except:
            pass



    def test_user(self):

        self.driver.find_element_by_css_selector('#mobile-nav-box>button')

        self.driver.find_element_by_css_selector('#mobile-nav-box>ul>a').click()
        self.driver.implicitly_wait(5)
        a=self.driver.find_element_by_css_selector("#signupForm > div.description-row > h3")
        print((a.text))
        self.driver.find_element_by_name('email').send_keys('tes1@gmail.com')
        self.driver.find_element_by_name('password').send_keys('cb123')
        self.driver.find_element_by_name('firstname').send_keys('channu')
        self.driver.find_element_by_name('lastname').send_keys('biradar')
        self.driver.find_element_by_name('mobile').send_keys('8767898760')

        try:
            while "Log Out" == self.driver.find_element_by_link_text("Log Out").text:
                print('account creation is successful')
                break
                self.driver.quit()
        except NoSuchElementException:
            print ('email already exest so login to user account')
            self.driver.find_element_by_css_selector('#signupForm > div.description-row > h5 > i').click()
            self.assertEqual("Sign In",
                             self.driver.find_element_by_css_selector("#loginForm > div.description-row > h3").text)
            self.assertEqual("Create Account", self.driver.find_element_by_css_selector(
                "#loginForm > div.description-row > h5 > i").text)
            self.assertEqual("Forgot your password?", self.driver.find_element_by_css_selector("#user-information > a").text)
            self.driver.find_element_by_name('email').send_keys('tes1@gmail.com')
            self.driver.find_element_by_name('password').send_keys('cb123')

            for i in range(60):
                try:
                    if "You are successfully logged in! Redirecting please wait..." == self.driver.find_element_by_xpath("//body/div[5]").text:
                        break
                except:
                    pass
            else:
                self.driver.implicitly_wait(5)
                return self.driver.find_element_by_link_text('Log Out').text

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
