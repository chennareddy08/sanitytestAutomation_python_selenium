import unittest,time,os
from .base_function import BasePage
from .booking_functions import Booking


class scriptfn(object):



    def __init__(self, driver):
        self.driver = driver

    def update_basicdetails(self, firstname, lastname, email, phone):
        """function to update basic details"""

        BasePage.firstName_field(self).clear()
        BasePage.firstName_field(self).send_keys(firstname)
        BasePage.lastName_field(self).clear()
        BasePage.lastName_field(self).send_keys(lastname)
        BasePage.email_field(self).clear()
        BasePage.email_field(self).send_keys(email)
        BasePage.phone_field(self).clear()
        BasePage.phone_field(self).send_keys(phone)
        BasePage.savechange_setting(self).click()
