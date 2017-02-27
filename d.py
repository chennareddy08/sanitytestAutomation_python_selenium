import os,time
from selenium import webdriver
os.environ["SELENIUM_SERVER_JAR"] = "/usr/local/bin/selenium-server-standalone-2.52.0.jar"
chrome_driver_path = os.getcwd() + "/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('https://www.handstandapp.com/')
time.sleep(10)
driver.set_window_size(1250,1024)
driver.find_element_by_css_selector("")