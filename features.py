import requests
import time,unittest
from selenium import webdriver
from .basetestcase import BaseTestCase
from .base_function import BasePage
from .basetestcase import BaseTestCase
from . import base_function,booking_functions

class Transaction(BaseTestCase):


    def test_run(self):
        target = booking_functions.Booking(self.driver)
        BP = base_function.BasePage(self.driver)
        r	=	requests.get("https://www.handstandapp.com/")
        r.raw.read()
        target.zipcode_entry('90405')
        self.driver.implicitly_wait(8)
        t1	=	time.time()
        r	=	requests.get("https://www.handstandapp.com/b")
        r.raw.read()
        latency	=	time.time()	-	t1
        print(latency)

    def tearDown(self):

        #close browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
