import unittest,time,string,random,os,sys
from selenium import webdriver
from basetestcase import BaseTestCase
from datetime import datetime

#from base_function import BasePage
import base_function
from basetestcase import BaseTestCase
import base_function,booking_functions



class links(BaseTestCase):

    def test_alllinks(self):
        """
         Test case to verify class type links
        """


        links=self.driver.find_elements_by_tag_name('a')

        count=len(links)
        for i in range(0,count):
            links = self.driver.find_elements_by_tag_name('a')

            try:
                print(links[i].text)
                links[i].click()
                self.driver.implicitly_wait('5')
                self.driver.get("https://handstandapp.com/index.php/site/about")
            except:pass

    def test_alllinks_afterlogin(self):

        target = base_function.BasePage(self.driver)
        target.signup_link().click()
        self.driver.implicitly_wait(2)
        target.Login_trainer_account("test65@gmail.com", "123456")
        self.driver.find_element_by_css_selector("#base-nav-link-toggle").click()
        self.driver.find_element_by_link_text("Settings").click()
        links1 = self.driver.find_elements_by_xpath('html/body/section[1]/div/div[1]/div/div[2]/a')
        links2 = self.driver.find_elements_by_xpath('html/body/section[1]/div/div[1]/div[2]/div/a')

        count = len(links1)
        for i in range(0, count):
            links1 =  self.driver.find_elements_by_xpath('html/body/section[1]/div/div[1]/div/div[2]/a')

            try:
                print(links1[i].text)
                links1[i].click()
            except:pass

        count = len(links2)
        for i in range(0, count):
            links2 = self.driver.find_elements_by_xpath('html/body/section[1]/div/div[1]/div[2]/div/a')

            try:
                print(links2[i].text)
                links2[i].click()
            except:
                pass





    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(os.getcwd() + '/screenshots/' + test_method_name + "-" + now + ".png")
    # close browser window
        self.driver.quit()




if __name__ == "__main__":
    unittest.main()
