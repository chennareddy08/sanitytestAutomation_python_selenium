
import unittest,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from basetestcase import BaseTestCase
import base_function,booking_functions
from selenium.common.exceptions import NoSuchElementException,WebDriverException
from selenium.webdriver.common.keys import Keys


class BookHandstand(BaseTestCase):


    def test_booking_zipcode_first(self):
        """
         Test case to verify Booking the session  first and login
        """
        self.driver.set_window_size(1250,1024)
        target=booking_functions.Booking(self.driver)
        BP=base_function.BasePage(self.driver)
        target.zipcode_entry('90405')
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_name("search").send_keys("chad")
        target.searcIcon().send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        try:
            target.booking_button().is_displayed()
            target.booking_button().click()
        except WebDriverException:
            print "Element is not clickable"
            target.booking_button().click()

        #target.validate_startbookingPage()
        target.startBookingButton().is_displayed()
        target.startBookingButton().click()
        #target.validate_datepage()
        target.currentdate().is_displayed()
        target.currentdate().click()
        target.currenttime().is_displayed()
        target.currenttime().click()
        #target.location_verifypage()
        target.location_entry('11200')
        #target.verify_classtypepage()
        target.classtype_select()
        self.driver.implicitly_wait(5)
        #target.verify_reviewpage()
        target.click_book_nowbutton().is_displayed()
        target.click_book_nowbutton().click()
        BP.login_link().is_displayed()
        BP.login_link().click()
        BP.login_account('testhandapp1@gmail.com','123456')
        #BP.login_successfull()
        self.driver.implicitly_wait(20)
        self.driver.save_screenshot("booked1.png")
        #target.verify_sessionbooked_confirmation()
        try:
            target.click_done_sessionconfirmation().click()
            self.driver.save_screenshot("booked2.png")
            print("Booking session is successfull")
        except:
            print("booking failed due to card was declined)")


  
   
  


    def cancel_bookings(self):
        """
         Test case to verify Booking the session  first and login
        """
        self.driver.set_window_size(1250,1024)
        target=booking_functions.Booking(self.driver)
        BP=base_function.BasePage(self.driver)
        BP.signup_link().is_displayed()
        BP.signup_link().click()
        BP.login_link().is_displayed()
        BP.login_link().click()
        BP.login_account('handstandtest4@gmail.com','123456')
        BP.login_successfull()
        self.driver.implicitly_wait(20)

        target.zipcode_entry('90405')

        try:
            while target.profileimage().is_displayed():
                target.profileimage().click()
        except:
            target.profileimage().click()
            pass
        try:
            while target.profiletab().is_displayed():
                target.profiletab().click()
        except:
            target.profiletab().click()
            pass

        target.workouttab().is_displayed()
        target.workouttab().click()
        self.driver.implicitly_wait(10)
        try:
            while target.cancel_bookingbutton().is_displayed():
                target.cancel_bookingbutton().click()
                target.verify_cancelworkoutpage_confirmation()
                target.cancel_Nevermindbutton().is_displayed()
                target.cancel_Nevermindbutton().click()
                self.driver.implicitly_wait(10)
                target.cancel_bookingbutton().is_displayed()
                target.cancel_bookingbutton().click()
                target.cancel_workoutbutton().is_displayed()
                target.cancel_workoutbutton().click()
                target.cancel_Nevermindbutton().is_displayed()
                target.cancel_Nevermindbutton().click()
                target.cancel_bookingbutton().is_displayed()
                target.cancel_bookingbutton().click()
                target.cancel_workoutbutton().is_displayed()
                target.cancel_workoutbutton().click()
                target.verify_workoutblocked_popup()
                target.cancel_workoutbutton().is_displayed()
                target.cancel_workoutbutton().click()

            else:
                self.wait = WebDriverWait(self.driver, 15)
                self.wait.until(EC._element_if_visible(target.booking_button()))
                target.cancel_bookingbutton().click()
                target.cancel_workoutbutton().click()
                target.cancel_workoutbutton().click()
        except:
            print("No Booked session available to cancel")
            pass


    def tearDown(self):

        #close browser window
        self.driver.quit()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


if __name__ == "__main__":
    unittest.main()




