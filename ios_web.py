import os,time
from appium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains



desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.2.1'
desired_caps['deviceName'] = 'ipod'

desired_caps['browserName'] = 'safari'
#time.sleep(100)
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

driver.get("https://handstandapp.com/")
driver.quit()
