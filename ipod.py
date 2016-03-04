import os,time
from appium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
success = True
desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.2.1'
desired_caps['deviceName'] = 'iPod'
desired_caps['autoAcceptAlerts'] = 'true'
desired_caps['app'] = os.path.abspath('/Users/chennareddy/ios_automation/apps/TestApp/build/release-iphonesimulator/Handstand/Handstand.app')
time.sleep(110)
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
alert = driver.switch_to_alert()
alert.accept()
driver.find_element_by_name("SKIP").click()
driver.find_element_by_name("Log In").click()
driver.find_element_by_class_name("UIATextField").send_keys('handstandtest3@gmail.com')
driver.find_element_by_class_name("UIASecureTextField").send_keys('123456')
driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
time.sleep(10)
driver.find_element_by_name("OK").click()
driver.find_element_by_name("Where do you want to workout?").click()
try:
    driver.find_element_by_name("Allow").click()
except:pass

driver.find_element_by_name("Search Address").send_keys("US")
driver.find_element_by_name("USA").click()
driver.find_element_by_name("Set Location").click()
driver.find_element_by_name("Date  /  Time").click()
driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 73, "y": 282 })
driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 64, "y": 280 })
driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 77, "y": 282 })
driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 66, "y": 282 })
driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAPicker[1]/UIAPickerWheel[1]").click()
driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAPicker[1]/UIAPickerWheel[2]").click()
driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAPicker[1]/UIAPickerWheel[3]").click()
driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAPicker[1]/UIAPickerWheel[4]").click()
driver.find_element_by_name("Class Type (Choose up to 5)").click()
driver.find_element_by_name("Lean Body Coaching").click()
driver.find_element_by_name("Tone Up! Butt Legs & Core").click()
driver.find_element_by_name("Weight Loss Coaching").click()
driver.find_element_by_name("Apply").click()
time.sleep(5)
driver.find_element_by_name("Handstand's Choice").click()
time.sleep(5)
driver.find_element_by_name("Start Booking").click()
driver.find_element_by_name("Edit Class Type").click()
time.sleep(5)
driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]").click()

time.sleep(5)
driver.find_element_by_name("Confirm Booking").click()
time.sleep(5)
#driver.find_element_by_css_selector("#nav-box > nav:nth-of-type(2) > a.signupLink").click()
driver.quit