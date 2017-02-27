

import unittest,time,os,re,string,random,sys

from selenium.webdriver.support.ui import Select

#from base_function import BasePage
from . import base_function
from .basetestcase import BaseTestCase
from selenium import webdriver
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException



class TestTrainerAccount(BaseTestCase):


    def test_Trainer(self):


        target=base_function.BasePage(self.driver)
        target.apply_ToBe_Trainer().click()

        assert (self.driver.find_element_by_css_selector("#app-layout > section.apply-flow > div > form > div > div.apply-panel-heading.panel-heading > h3")).text ==  'Apply To Be a Trainer'
        self.driver.implicitly_wait(2)
        target.trainer_account_creation('test1','tester','tester@gmail.com','1234567890','12345678','12345678','90405','4','abc','8')







    def test_createAccount_madatoryfield(self):

        """
         Test case to validate create account section the mandatory fields
        """
        target=base_function.BasePage(self.driver)
        target.apply_ToBe_Trainer().click()
        self.driver.implicitly_wait(2)
        target.register_trainerButton().click()
        d1 = self.driver.find_element_by_css_selector(
            "#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger")
        e1 = (self.driver.execute_script("return arguments[0].textContent", d1))
        print((e1.strip()))
        try:
            assert e1.strip() == "The first name field is required."
        except:
            print((e1.strip()))
        target.firstName_field().send_keys('test')
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d2 = self.driver.find_element_by_css_selector(
            "#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger")

        e2 = (self.driver.execute_script("return arguments[0].textContent", d2))
        print((e2.strip()))
        try:
            assert e2.strip() == "The last name field is required."
        except:
            print((e2.strip()))
        target.lastName_field().send_keys('test')
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d3=self.driver.find_element_by_css_selector('#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e3 = (self.driver.execute_script("return arguments[0].textContent", d3))
        print((e3.strip()))
        try:
            assert e3.strip()  == "The email field is required."
        except:
            print((e3.strip()))
        target.email_field().send_keys('test65@gmail.com')
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d4 = self.driver.find_element_by_css_selector('#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e4 = (self.driver.execute_script("return arguments[0].textContent",d4))
        print((e4.strip()))
        try:
            assert e4.strip() == "The email has already been taken."
        except:
            print((e4.strip()))
        target.email_field().send_keys(random.choice(string.digits)+random.choice(string.digits))
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d5 = self.driver.find_element_by_css_selector('#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e5 = (self.driver.execute_script("return arguments[0].textContent",d5))
        print((e5.strip()))
        try:
            assert e5.strip() == "The phone field is required."
        except:
            print((e5.strip()))
        target.phone_field().send_keys(5)
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d6 =  self.driver.find_element_by_css_selector('#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e6 = (self.driver.execute_script("return arguments[0].textContent",d6))
        print((e6.strip()))
        try:
            assert e6.strip() == "Please Enter a valid Date of Birth. (Month, Day and Year are all required)."
        except:
            print((e6.strip()))
        Select(target.month_field()).select_by_visible_text('May')
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        try:
            assert e6.strip() == "Please Enter a valid Date of Birth. (Month, Day and Year are all required)."
        except:
            print((e6.strip()))
        Select(target.month_field()).select_by_visible_text('Month')
        Select(target.day_field()).select_by_visible_text('01')
        target.register_trainerButton().click()
        try:
            assert e6.strip() == "Please Enter a valid Date of Birth. (Month, Day and Year are all required)."
        except:
            print((e6.strip()))
        Select(target.day_field()).select_by_visible_text('Day')
        Select(target.year_field()).select_by_visible_text('2000')
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        try:
            assert e6.strip() == "Please Enter a valid Date of Birth. (Month, Day and Year are all required)."
        except:
            print((e6.strip()))
        Select(target.day_field()).select_by_visible_text('01')
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        try:
            assert e6.strip() == "Please Enter a valid Date of Birth. (Month, Day and Year are all required)."
        except:
            print((e6.strip()))
        Select(target.day_field()).select_by_visible_text('Day')
        Select(target.month_field()).select_by_visible_text('Month')
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        try:
            assert e6.strip() == "Please Enter a valid Date of Birth. (Month, Day and Year are all required)."
        except:
            print((e6.strip()))
        Select(target.day_field()).select_by_visible_text('01')
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d7 = self.driver.find_element_by_css_selector('#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e7 = (self.driver.execute_script("return arguments[0].textContent",d7))
        print((e7.strip()))
        try:
            assert e7.strip() == "The password field is required."
        except:
            print((e7.strip()))
        target.password_field().send_keys(1)
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d8 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e8 = (self.driver.execute_script("return arguments[0].textContent", d8))
        print((e8.strip()))
        try:
            assert e8.strip() == "The password must be at least 8 characters."
        except:
            print((e8.strip()))
        target.password_field().send_keys(11111111)
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d9 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e9 = (self.driver.execute_script("return arguments[0].textContent", d9))
        print((e9.strip()))
        try:
            assert e9.strip() == "The password confirmation does not match."
        except:
            print((e9.strip()))
        target.password_field().send_keys(11111111)
        target.confirm_password().send_keys(111111)
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        try:
            assert e9.strip() == "The password confirmation does not match."
        except:
            print((e9.strip()))
        target.password_field().send_keys(11111111)
        target.confirm_password().send_keys(11111111)
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d10 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e10 = (self.driver.execute_script("return arguments[0].textContent", d10))
        print((e10.strip()))
        try:
            assert e10.strip() == "Please Select the checkbox to agree that you are over 18 years of age."
        except:
            print((e10.strip()))
        target.password_field().send_keys(11111111)
        target.confirm_password().send_keys(11111111)
        target.term_conditionSelect().click()
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        d11 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e11 = (self.driver.execute_script("return arguments[0].textContent", d11))
        print((e11.strip()))
        try:
            assert e11.strip() == "Ineligible Date of Birth. You must be atleast 18 years or older."
        except:
            print((e11.strip()))
        Select(target.day_field()).select_by_visible_text('01')
        Select(target.month_field()).select_by_visible_text('May')
        Select(target.year_field()).select_by_visible_text('1989')
        target.password_field().send_keys(11111111)
        target.confirm_password().send_keys(11111111)
        target.term_conditionSelect().click()
        target.register_trainerButton().click()
        self.driver.implicitly_wait(1)
        # d12 = self.driver.find_element_by_css_selector(
        #     "#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger")
        # e12 = (self.driver.execute_script("return arguments[0].textContent", d12))
        # print(e12.strip())
        # try:
        #     assert e12.strip() == "Please enter a 10-digit phone number."
        # except:
        #     print(e12.strip())
        # target.phone_field().send_keys(444344444)
        # target.password_field().send_keys(11111111)
        # target.confirm_password().send_keys(11111111)
        # target.term_conditionSelect().click()
        # target.register_trainerButton().click()
        # self.driver.implicitly_wait(2)
        target.submit_button().click()
        self.driver.implicitly_wait(1)
        d13 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e13 = (self.driver.execute_script("return arguments[0].textContent", d13))
        print((e13.strip()))
        try:
            assert e13.strip() == "The zip code field is required."
        except:
            print((e13.strip()))
        target.zipcode().send_keys(90)
        target.submit_button().click()
        self.driver.implicitly_wait(1)
        d14 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e14 = (self.driver.execute_script("return arguments[0].textContent", d14))
        print((e14.strip()))
        try:
            assert e14.strip() == "The distance field is required."
        except:
            print((e14.strip()))
        self.driver.find_element_by_id("inlineRadio3").click()
        target.submit_button().click()
        self.driver.implicitly_wait(1)
        d15 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e15 = (self.driver.execute_script("return arguments[0].textContent", d15))
        print((e15.strip()))
        try:
            assert e15.strip() == "The certifications field is required."
        except:
            print((e15.strip()))
        target.accolades_certifications().send_keys(8)
        target.submit_button().click()
        self.driver.implicitly_wait(1)
        d16 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e16 = (self.driver.execute_script("return arguments[0].textContent", d16))
        print((e16.strip()))
        try:
            assert e16.strip() == "The about field is required."
        except:
            print((e16.strip()))
        target.accolades_certifications().send_keys(8)
        target.aboutMe().send_keys('good certified trainer')
        target.submit_button().click()
        self.driver.implicitly_wait(1)
        d17 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e17 = (self.driver.execute_script("return arguments[0].textContent", d17))
        print((e17.strip()))
        try:
            assert e17.strip() == "The experience field is required."
        except:
            print((e17.strip()))
        print((e17.strip()))
        target.accolades_certifications().send_keys(8)
        target.aboutMe().send_keys('good certified trainer')
        target.years_experience().send_keys(8)
        target.submit_button().click()
        self.driver.implicitly_wait(1)
        d18 = self.driver.find_element_by_css_selector(
            '#app-layout > section.apply-flow > div > form > div > div.panel-body > div.alert.alert-danger')
        e18 = (self.driver.execute_script("return arguments[0].textContent", d18))
        print((e18.strip()))
        try:
            assert e18.strip() == "Sorry this zip code doesn't appear to be valid."
        except:
            print((e18.strip()))
        print((e18.strip()))
        target.zipcode().clear()
        target.zipcode().send_keys(90405)
        target.accolades_certifications().send_keys(8)
        target.aboutMe().send_keys('good certified trainer')
        target.years_experience().send_keys(8)
        target.submit_button().click()
        self.driver.implicitly_wait(1)
        specialtieslist = self.driver.find_elements_by_xpath(
            ".//*[@id='app-layout']/section/div/form/div/div[2]/div/div")
        try:
            for i in range(1, len(specialtieslist)):
                specialtieslist[i].click()
        except:
            pass
        target.submit_button().click()
        target.savechanges_button().click()













    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(os.getcwd() + '/screenshots/' + test_method_name + "-" + now + ".png")
    # close browser window
        self.driver.quit()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


if __name__ == "__main__":
        unittest.main()







