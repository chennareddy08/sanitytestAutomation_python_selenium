

import time


#from base_function import BasePage
import base_function
from basetestcase import BaseTestCase

from selenium.common.exceptions import NoSuchElementException



class TestAccount(BaseTestCase):


    def test_user(self):


        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        time.sleep(5)

        assert  ((self.driver.find_element_by_xpath(".//*[@id='signupForm']/div[1]/h3")).text)=='Create Account'
        target.user_account_creation('tes1@gmail.com','cb123','channu','biradar','8767898760')
        try:
            while "Log Out" == self.driver.find_element_by_link_text("Log Out").text:
                print('account creation is successful')
                break
                self.driver.quit()
        except NoSuchElementException:
            print ('email already exest so login to user account')
            target.login_link().click()
            self.assertEqual("Sign In", self.driver.find_element_by_css_selector("#loginForm > div.description-row > h3").text)
            self.assertEqual("Create Account", self.driver.find_element_by_css_selector("#loginForm > div.description-row > h5 > i.swap").text)
            self.assertEqual("Forgot your password?", self.driver.find_element_by_css_selector("a.swap").text)
            target.login_account('test1@gmail.com','cb123')
            target.login_successfull()


    def test_newuser(self):
        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        time.sleep(5)
        assert  ((self.driver.find_element_by_xpath(".//*[@id='signupForm']/div[1]/h3")).text)=='Create Account'
        target.user_account_creation('tes1@gmail.com','cb123','channu','biradar','8767898760')
        try:
            while "Log Out" == self.driver.find_element_by_link_text("Log Out").text:
                print('account creation is successful')
                break
                self.driver.quit()
        except NoSuchElementException:
            print ('Creating new usr')
            target.user_account_creation('a+tes1@gmail.com','cb123','channu','biradar','8767898760')

    def test_madatoryfield(self):

        """
         Test case to validate the mandatory field
        """
        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath(".//*[@id='signupForm']/div[1]/h3").text=='Create Account'
        target.create_account_button().click()
        demo1=self.driver.find_element_by_xpath("//div[5]/li")
        e1=(self.driver.execute_script("return arguments[0].textContent", demo1))
        print (e1)
        assert e1 == 'Invalid email format'
        target.email_field().send_keys('a'+'ggggg@mail.com')
        demo2=self.driver.find_element_by_xpath("//div[5]/li[2]")
        e2=(self.driver.execute_script("return arguments[0].textContent",demo2))
        print (e2)
        self.driver.implicitly_wait(1)
        assert e2 == 'Password cannot be blank.'
        target.passowrd_field().send_keys('akk'+'u')
        self.driver.implicitly_wait(1)
        demo3 = self.driver.find_element_by_xpath("//div[5]/li[3]")
        e3 = (self.driver.execute_script("return arguments[0].textContent",demo3))
        print (e3)
        assert e3 == 'Mobile must be valid.'
        target.phoneNumber_field().send_keys('222222222')
        demo4 = self.driver.find_element_by_xpath("//div[5]/li[4]")
        e4 = (self.driver.execute_script("return arguments[0].textContent",demo4))
        print(e4)
        assert e4 == 'First name cannot be blank.'
        target.firstName_field().send_keys('a'+'u')
        demo5= self.driver.find_element_by_xpath("//div[5]/li[5]")
        e5 = (self.driver.execute_script("return arguments[0].textContent",demo5))
        print(e5)
        assert e5 == 'Last name cannot be blank.'
        target.lastName_field().send_keys('a'+'u')


        demo6 = self.driver.find_element_by_xpath("//li[6]")
        e6 = (self.driver.execute_script("return arguments[0].textContent",demo6))
        print(e6)
        assert e6 == 'Please provide a valid mobile number'
        target.phoneNumber_field().send_keys('222222222')
        target.create_account_button().click()



    def test_Navigate_SigninCreateAccountPage(self):

        """Test To Verify Navigation between sign in and create account page """
        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        time.sleep(5)
        assert (self.driver.find_element_by_css_selector("#signupForm > div.description-row > h3")).text == 'Create Account'
        target.login_link().click()
        time.sleep(5)
        assert (self.driver.find_element_by_css_selector("#loginForm > div.description-row > h3")).text == 'Sign In'
        assert (self.driver.find_element_by_css_selector("#loginForm > div.description-row > h5 > i.swap")).text == 'Create Account'
        assert (self.driver.find_element_by_css_selector("a.swap")).text == 'Forgot your password?'
        if (self.driver.find_element_by_css_selector("a.swap").text == 'Forgot your password?'):
            print("Navigation between sign in and create account page")

        else:
            print("Navigation failed")


    # def test_verifyForgotPasswordOption(self):
    #     """
    #     Test to Verify the Forgot password link on login page and the forgot password page
    #
    #     """
    #     target=base_function.BasePage(self.driver)
    #
    #     target.forgot_pass_cleanup()
    #     self.driver.get("https://handstandapp.com/")
    #     target.forgot_passwordcheck('rebertjacob@gmail.com')
    #     target.mail_passwordrecover()
    #     target.Homepage_check()




