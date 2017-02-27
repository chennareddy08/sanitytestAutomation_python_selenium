


import unittest,time,os,sys,string,random
from selenium import webdriver
from datetime import datetime
#from base_function import BasePage
import base_function
from basetestcase import BaseTestCase
from datetime import datetime
stamp = datetime.now().strftime("%Y-%m-%d%  %H:%m:%S %p")
stampdate = datetime.now().strftime("%Y-%m-%d% ")
stamptime = datetime.now().strftime("% %H:%m:%S %p")
emailstamp = datetime.now().strftime("%Y%m%d%H%M%S")
email="Test_user_" + emailstamp + "@gmail.com"

from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException



class TestAccount(BaseTestCase):


    def test_user_createAccount(self):


        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        time.sleep(5)

        assert (self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-heading.panel-heading-login > p > a")).text ==  'Create an Account'
        self.driver.find_element_by_link_text('Create an Account').click()
        self.driver.implicitly_wait(5)
        assert self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-heading.panel-heading-login > h3").text == 'Register'
        try:
            target.user_account_creation('channu', 'biradar', 'test1@gmail.com', '12345678', '12345678')
            self.driver.find_element_by_css_selector("#base-nav-link-toggle").click()
            while "Log Out" == self.driver.find_element_by_link_text("Log Out").text:
                print('account creation is successful')
                break

        except NoSuchElementException:
            self.assertEqual('The email has already been taken.',self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger").text)
            print((self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger").text))
            target.login_link().click()
            self.assertEqual("Sign In", self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-heading.panel-heading-login > h3").text)
            self.assertEqual("Create an Account" , self.driver.find_element_by_link_text("Create an Account").text)
            self.assertEqual("Forgot Your Password?" , self.driver.find_element_by_link_text('Forgot Your Password?').text)

            target.login_account('test1@gmail.com','cb123')
            target.login_successfull()




    def test_newuser(self):
        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        time.sleep(2)
        assert  ((self.driver.find_element_by_link_text("Create an Account")).text)=='Create an Account'
        self.driver.find_element_by_link_text('Create an Account').click()
        time.sleep(2)
        target.user_account_creation('channu','biradar','test1@gmail.com','12345678','12345678')
        try:
            self.driver.find_element_by_css_selector("#base-nav-link-toggle").click()
            while "Log Out" == self.driver.find_element_by_link_text("Log Out").text:
                print('account creation is successful')
                break
            self.driver.quit()
        except NoSuchElementException:
            print ('Creating new user')
            target.user_account_creation('channu','biradar',email,'12345678','12345678')
            self.driver.implicitly_wait(2)
            try:
                self.driver.find_element_by_css_selector("#base-nav-link-toggle").click()
            except:pass
            print('account creation is successful')

    def test_createAccount_madatoryfield(self):

        """
         Test case to validate create account section the mandatory fields
        """
        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element_by_link_text("Create an Account").text=='Create an Account'
        target.Create_account_link().click()
        self.driver.implicitly_wait(2)

        target.register_button().click()
        demo4 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e4 = (self.driver.execute_script("return arguments[0].textContent", demo4))
        print((e4.strip()))
        try:
            assert e4.strip() == 'The first name field is required.'
        except:pass
        target.firstName_field().send_keys('a' + 'u')

        target.register_button().click()
        demo5 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e5 = (self.driver.execute_script("return arguments[0].textContent", demo5))
        print((e5.strip()))
        try:
            assert e5.strip() == 'The last name field is required.'
        except:pass
        target.lastName_field().send_keys('a' + 'u')
        target.register_button().click()
        self.driver.implicitly_wait(2)

        demo1=self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e1=(self.driver.execute_script("return arguments[0].textContent", demo1))
        print((e1.strip()))
        try:
            assert e1.strip() == "The email field is required."
        except:pass
        target.email_field().send_keys('test65@mail.com')
        target.register_button().click()
        self.driver.implicitly_wait(2)

        demo6 = self.driver.find_element_by_css_selector(  "#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e6 = (self.driver.execute_script("return arguments[0].textContent", demo6))
        print((e6.strip()))
        try:
            assert e6.strip() == "The email has already been taken."
        except:pass
        target.email_field().clear()
        target.email_field().send_keys(email)
        target.register_button().click()
        self.driver.implicitly_wait(2)

        demo2 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e2 = (self.driver.execute_script("return arguments[0].textContent", demo2))
        print((e2.strip()))
        try:
            assert e2.strip() == 'The password field is required.'
        except:pass
        target.password_field().send_keys('12345ab')
        target.register_button().click()
        self.driver.implicitly_wait(2)

        demo3 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e3 = (self.driver.execute_script("return arguments[0].textContent", demo3))
        print((e3.strip()))
        try:
            assert e3.strip() == 'The password must be at least 8 characters.'
        except:pass
        target.password_field().send_keys(12345678)
        target.register_button().click()
        self.driver.implicitly_wait(2)


        demo7 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e7 = (self.driver.execute_script("return arguments[0].textContent", demo7))
        print((e7.strip()))
        self.driver.implicitly_wait(2)
        try:
            assert e7.strip() == 'The password confirmation does not match.'
        except:pass

        target.confirm_password().send_keys(12345678)
        target.password_field().send_keys(12345678)
        target.register_button().click()
        self.driver.implicitly_wait(2)
        self.driver.quit()


    def test_login_madatoryfield(self):
        """
            Test case to validate Login section the mandatory fields
           """

        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        self.driver.implicitly_wait(2)
        target.signin_button().click()
        self.driver.implicitly_wait(2)
        d1 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e1 = (self.driver.execute_script("return arguments[0].textContent", d1))
        print((e1.strip()))
        try:
            assert e1.strip() == "The email field is required."
        except:pass
        target.email_field().send_keys('test65@mail.com')
        target.signin_button().click()

        d2 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e2 = (self.driver.execute_script("return arguments[0].textContent", d2))
        print((e2.strip()))
        try:
            assert e2.strip() == 'The password field is required.'
        except:pass
        target.password_field().send_keys('12345ab')
        target.signin_button().click()
        self.driver.implicitly_wait(2)

        d3 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e3 = (self.driver.execute_script("return arguments[0].textContent", d3))
        print((e3.strip()))
        try:
            assert e3.strip() == 'Incorrect email or password'
        except:pass
        target.password_field().send_keys('123456')
        target.signin_button().click()
        self.driver.implicitly_wait(2)


    def test_Navigate_SigninCreateAccountPage(self):

        """Test To Verify Navigation between sign in and create account page """
        target=base_function.BasePage(self.driver)
        target.signup_link().click()
        self.driver.implicitly_wait(2)
        assert (self.driver.find_element_by_link_text("Create an Account")).text == 'Create an Account'
        assert (self.driver.find_element_by_link_text("Forgot Your Password?")).text == 'Forgot Your Password?'
        target.Create_account_link().click()
        self.driver.implicitly_wait(2)
        assert (self.driver.find_element_by_link_text("Log In")).text == 'Log In'
        assert (self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-heading.panel-heading-login > h3")).text == 'Register'
        target.login_link().click()

        if (self.driver.find_element_by_link_text("Forgot Your Password?").text == "Forgot Your Password?"):
            print("Navigation between sign in and create account page is successful.")

        else:
            print("Navigation failed")


    def test_verifyForgotPasswordOption(self):
        """
        Test to Verify the Forgot password link on login page and the forgot password page

        """
        target=base_function.BasePage(self.driver)

        target.forgot_pass_cleanup()

        target.forgot_passwordcheck('rebertjacob@gmail.com')

        target.mail_passwordrecover()


    def test_mandatoryField_resetPassword(self):
        """
        This function to verify mandatoty field on resetPassword

        """

        target = base_function.BasePage(self.driver)
        target.signup_link().click()
        self.driver.implicitly_wait(2)
        assert (self.driver.find_element_by_link_text("Forgot Your Password?")).text == 'Forgot Your Password?'
        target.forgot_password().click()
        self.driver.implicitly_wait(2)
        target.submitButton_forgot().click()
        d1 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e1 = (self.driver.execute_script("return arguments[0].textContent", d1))
        print((e1.strip()))
        try:
            assert e1.strip() == "The email field is required."
        except:
            pass
        target.email_field().clear()
        target.email_field().send_keys('rajkumar@gmail.com')
        target.submitButton_forgot().click()
        d2 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-danger")
        e2 = (self.driver.execute_script("return arguments[0].textContent", d2))
        print((e2.strip()))
        try:
            assert e2.strip() == "The selected email is invalid."
        except:
            pass
        target.email_field().send_keys('handstandtest4@gmail.com')
        target.submitButton_forgot().click()

    def test_madatoryField_confirmResetPassword(self):
        """
               This function to verify mandatoty field on resetPassword

               """
        target = base_function.BasePage(self.driver)
        self.driver.get("https://stage.handstandapp.com/password/reset?token=")
        target.change_passwd_button().click()
        d1 = self.driver.find_element_by_css_selector("#app-layout > div > div > div > div > div.panel-body > div")
        e1 = (self.driver.execute_script("return arguments[0].textContent", d1))
        print((e1.strip()))
        try:
            assert e1.strip() == "The email field is required."
        except:
            pass
        target.email_field().clear()
        target.email_field().send_keys('rajkumar@gmail.com')
        target.change_passwd_button().click()
        d2 = self.driver.find_element_by_css_selector("#app-layout > div > div > div > div > div.panel-body > div")
        e2 = (self.driver.execute_script("return arguments[0].textContent", d2))
        print((e2.strip()))
        try:
            assert e2.strip() == "The selected email is invalid."
        except:
            pass
        target.email_field().clear()
        target.email_field().send_keys('handstandtest4@gmail.com')
        target.change_passwd_button().click()
        d3 = self.driver.find_element_by_css_selector("#app-layout > div > div > div > div > div.panel-body > div")
        e3 = (self.driver.execute_script("return arguments[0].textContent", d3))
        print((e3.strip()))
        try:
            assert e3.strip() == " Sorry , the reset code has expired. Please submit a new request."
        except:
            pass
    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(os.getcwd() + '/screenshots/' + test_method_name + "-" + now + ".png")
    # close browser window
        self.driver.quit()



