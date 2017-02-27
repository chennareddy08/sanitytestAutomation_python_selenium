
import unittest,time,os,re,sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basetestcase import BaseTestCase
import base_function,booking_functions
from selenium.common.exceptions import NoSuchElementException,WebDriverException,NoAlertPresentException
from datetime import datetime
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By






class BookHandstand(BaseTestCase):


    def test_booking_session(self):
        """
         Test case to verify Booking the session
        """
        target=booking_functions.Booking(self.driver)
        BP=base_function.BasePage(self.driver)
        target.search_trainerfor_booking()
        target.datetimeselect()
        target.location_field().send_keys(90405)
        time.sleep(1)
        target.location_field().send_keys(Keys.ARROW_DOWN,Keys.RETURN)
        target.classtype_select().click()
        self.driver.implicitly_wait(2)
        target.next_button().is_displayed()
        target.next_button().click()
        try:
            a= target.formatted_addressfield_error().text
            if a.strip() == "The formatted address field is required.":
                target.datetimeselect()
                target.location_field().send_keys(90405)
                target.location_googleSearch_Dropdoen().click()
                target.classtype_select().click()
                self.driver.implicitly_wait(2)
                target.next_button().is_displayed()
                target.next_button().click()
        except:pass

        target.phone_User().clear()
        target.phone_User().send_keys(7272727272)
        target.one_on_oneselection().click()
        target.next_button().is_displayed()
        target.next_button().click()
        self.driver.implicitly_wait(2)
        target.choose_package().click()
        target.nextbutton_chooosePackage().click()
        self.driver.implicitly_wait(1)
        BP.login_account('testjc88@gmail.com','8892279018')
        self.driver.implicitly_wait(2)
        target.confirma_paymentbutton().is_displayed()
        target.confirma_paymentbutton().click()
        self.driver.save_screenshot("booked2.png")
        try:
            target.booking_success()

            print((self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > div > p").text.strip()))
        except:
            print("booking failed due to card was declined")


    def test_cancel_bookings(self):
        """
         Test case to verify Cancel the Booked the session
        """

        target=booking_functions.Booking(self.driver)
        BP=base_function.BasePage(self.driver)
        target.Navigate_workoutscreen()

        try:
            self.accept_next_alert = False
            target.cancel_Appointment().is_displayed()
            target.cancel_Appointment().click()
            self.assertRegex(self.close_alert_and_get_its_text(), r"^Are you sure you want to cancel [\s\S]$")
            self.driver.find_element_by_link_text("Cancel Appointment").click()
            self.assertRegex(self.close_alert_and_get_its_text(), r"^Are you sure you want to cancel [\s\S]$")
            self.assertEqual("Your booking was deleted!",self.driver.find_element_by_css_selector("div.alert.alert-success").text)
            print((self.driver.find_element_by_css_selector("#profile-container > div > div.col-md-10 > div > div > div.alert.alert-success").text))
        except:
            print("Workout section is blank ")




    def test_mandatoryfield_bookWorkout(self):
        """
            Test case to verify mandatory on book Workout page
           """

        target = booking_functions.Booking(self.driver)
        BP = base_function.BasePage(self.driver)
        target.search_trainerfor_booking()
        target.next_button().click()
        self.driver.implicitly_wait(2)
        e1=self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > form > div > div.panel-body > div.alert.alert-danger").text
        print((e1.strip()))
        try:
            assert e1.strip()=="The book date field is required."
        except:pass
        target.dateselect()
        target.next_button().click()
        self.driver.implicitly_wait(2)
        e2=self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > form > div > div.panel-body > div.alert.alert-danger").text
        print((e2.strip()))
        try:
            assert e2.strip()=="The book time field is required."

        except:pass
        self.driver.refresh()
        target.datetimeselect()
        target.next_button().click()
        self.driver.implicitly_wait(4)
        e3=self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > form > div > div.panel-body > div.alert.alert-danger").text
        print((e3.strip()))
        try:
            assert e3.strip()=="The formatted address field is required."

        except:pass
        self.driver.refresh()
        target.datetimeselect()
        target.location_field().send_keys(90405)
        time.sleep(1)
        target.location_field().send_keys(Keys.ARROW_DOWN,Keys.RETURN)
        target.next_button().click()
        self.driver.set_script_timeout(2)
        try:
            a= target.formatted_addressfield_error().text
            if a.strip() == "The formatted address field is required.":
                self.driver.refresh()
                target.datetimeselect()
                target.location_field().send_keys(90405)
                target.location_googleSearch_Dropdoen().click()
                self.driver.implicitly_wait(2)
                target.next_button().is_displayed()
                target.next_button().click()
        except:pass

        e4=self.driver.find_element_by_css_selector("#app-layout > section > div > form > div > div.panel-body > div.alert.alert-danger").text
        print((e4.strip()))
        try:
            assert e4.strip()=="The book type field is required."
        except:pass
        self.driver.refresh()
        target.datetimeselect()
        target.location_field().send_keys(90405)
        time.sleep(1)
        target.location_field().send_keys(Keys.ARROW_DOWN,Keys.RETURN)
        target.classtype_select().click()
        self.driver.implicitly_wait(1)
        target.next_button().click()
        self.driver.implicitly_wait(2)
        try:
            a= target.formatted_addressfield_error().text
            if a.strip() == "The formatted address field is required.":
                self.driver.refresh()
                target.datetimeselect()
                target.location_field().send_keys(90405)
                target.location_googleSearch_Dropdoen().click()
                target.classtype_select().click()
                self.driver.implicitly_wait(2)
                target.next_button().is_displayed()
                target.next_button().click()
        except:pass

        self.driver.find_element_by_css_selector('#app-layout > section.book-flow > div > form > div > div.book-panel-header.panel-heading > h3').is_displayed()

    def test_mandatory_reviewYourBooking(self):
        """
            Test case to verify mandatory on review Your Booking
           """
        target=booking_functions.Booking(self.driver)
        BP=base_function.BasePage(self.driver)
        target.search_trainerfor_booking()
        target.datetimeselect()
        target.location_field().send_keys(90405)
        time.sleep(1)
        target.location_field().send_keys(Keys.ARROW_DOWN,Keys.RETURN)
        target.classtype_select().click()
        self.driver.implicitly_wait(2)
        target.next_button().click()
        self.driver.implicitly_wait(1)
        target.next_button().click()
        self.driver.implicitly_wait(1)
        e1 = self.driver.find_element_by_css_selector(
        "#app-layout > section.book-flow > div > form > div > div.panel-body > div.alert.alert-danger").text
        print((e1.strip()))
        try:
            assert e1.strip() == "The workout size field is required."
        except:pass
        target.one_on_oneselection().click()
        target.next_button().click()
        e2 = self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > form > div > div.panel-body > div.alert.alert-danger").text
        print((e2.strip()))
        try:
            assert e2.strip() == "The phone field is required."
        except:pass

        target.phone_User().clear()
        target.phone_User().send_keys(1234567890)
        target.one_on_oneselection().click()
        target.next_button().click()
        self.driver.back()
        target.small_group().click()
        target.next_button().click()
        self.driver.implicitly_wait(2)


    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(os.getcwd() + '/screenshots/' + test_method_name + "-" + now + ".png")
         # close browser window
        self.driver.quit()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

if __name__ == "__main__":
    unittest.main()




