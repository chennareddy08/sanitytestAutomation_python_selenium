
import unittest,os,time
from selenium import webdriver
os.environ["SELENIUM_SERVER_JAR"] = "/usr/local/bin/selenium-server-standalone-2.52.0.jar"
path=os.getcwd() + '/IEDriverServer'
chrome_driver_path = os.getcwd() + "/chromedriver"
opera_path=os.getcwd() + "/operadriver"

class BaseTestCase(unittest.TestCase):
    # @classmethod
    # def setUp(cls):
    # #create a new Firefox session
    #     cls.driver = webdriver.Firefox()
    #
    #
    #     cls.driver.implicitly_wait(30)
    #     cls.driver.maximize_window()
    #
    #     # navigate to the application home page
    #     cls.driver.get('https://www.handstandapp.com/')

    #
    @classmethod
    def setUp(cls):
        #create a new chrome session
        cls.driver = webdriver.Chrome(chrome_driver_path)
        # cls.options = webdriver.ChromeOptions()

        # cls.options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # cls.driver = webdriver.Chrome(chrome_options=cls.options)
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

        #navigate to the application home page

        cls.driver.get('https://stage.handstandapp.com/')
        #cls.driver.get('http://handstandapp.com/')
        try:
            cls.driver.find_element_by_css_selector("#sumome-welcomemat > input").send_keys("tes1@gmail.com")
            cls.driver.find_element_by_css_selector(".sumome-welcomemat-action-submit.sumome-welcomemat-button").click()
        except:
            pass
        try:
            cls.driver.find_element_by_css_selector("#top-nav > div > nav.left > a:nth-child(1)").click()
        except:pass

    #
    #
    # @classmethod
    # def setUp(cls):
    # #create a new safari session
    #       cls.driver = webdriver.Safari()
    #
    #       cls.driver.implicitly_wait(30)
    #       cls.driver.maximize_window()
    #
    #     # navigate to the application home page
    #       cls.driver.get('https://www.handstandapp.com/')
    # @classmethod
    # def setUp(cls):
    #     # create a new ie session
    #
    #     cls.driver = webdriver.Ie(path)
    #
    #
    #     cls.driver.implicitly_wait(30)
    #     cls.driver.maximize_window()
    #
    #     #navigate to the application home page
    #     cls.driver.get('https://www.handstandapp.com/')
    #
    # @classmethod
    # def setUp(cls):
    #     # create a new opera session
    #
    #     cls.driver = webdriver.Opera(opera_path)
    #     cls.driver.implicitly_wait(30)
    #     cls.driver.maximize_window()
    #
    #     # navigate to the application home page
    #     cls.driver.get('https://www.handstandapp.com/')





    @classmethod
    def tearDown(cls):

        #close browser window
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
