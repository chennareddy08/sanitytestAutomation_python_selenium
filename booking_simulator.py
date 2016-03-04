import os,time,unittest
from appium import webdriver




class iosbooking(unittest.TestCase):

    def __init__(self):
        print ('hi sir')
        self.setUp()

    def setUp(self):
        time.sleep(110)
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
             #'app': app,
             'autoAcceptAlerts':'true',
            'platformName': 'iOS',
            'platformVersion': '9.0',
             'deviceName': 'iPhone 6s' })

    def booking_ios(self):
        self.driver.find_element_by_name("SKIP").click()
        self.driver.find_element_by_name("Log In").click()
        time.sleep(5)
        self.driver.find_element_by_class_name("UIATextField").send_keys('handstandtest3@gmail.com')
        self.driver.find_element_by_class_name("UIASecureTextField").send_keys('123456')
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
        time.sleep(10)
        #driver.find_element_by_name("OK").click()
        self.driver.find_element_by_name("Where do you want to workout?").click()
        try:
            self.driver.find_element_by_name("Allow").click()
        except:
            pass
        self.driver.find_element_by_name("Search Address").send_keys("US")
        self.driver.find_element_by_name("USA").click()
        self.driver.find_element_by_name("Set Location").click()
        self.driver.find_element_by_name("Date  /  Time").click()
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 73, "y": 282 })
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 64, "y": 280 })
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 77, "y": 282 })
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 66, "y": 282 })
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAPicker[1]/UIAPickerWheel[1]").click()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAPicker[1]/UIAPickerWheel[2]").click()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAPicker[1]/UIAPickerWheel[3]").click()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAPicker[1]/UIAPickerWheel[4]").click()
        self.driver.find_element_by_name("Class Type (Choose up to 5)").click()
        self.driver.find_element_by_name("Lean Body Coaching").click()
        self.driver.find_element_by_name("Tone Up! Butt Legs & Core").click()
        self.driver.find_element_by_name("Weight Loss Coaching").click()
        self.driver.find_element_by_name("Apply").click()
        time.sleep(5)
        self.driver.find_element_by_name("Handstand's Choice").click()
        time.sleep(5)
        self.driver.find_element_by_name("Start Booking").click()
        self.driver.find_element_by_name("Edit Class Type").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]").click()
        time.sleep(5)
        self.driver.find_element_by_name("Confirm Booking").click()
        time.sleep(5)
        #driver.find_element_by_css_selector("#nav-box > nav:nth-of-type(2) > a.signupLink").click()



    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)