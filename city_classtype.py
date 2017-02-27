import unittest,time,os,sys
from selenium import webdriver
from datetime import datetime
from basetestcase import BaseTestCase

class city_classtypelinks(BaseTestCase):

    def test_class_type(self):
        """
         Test case to verify class type links
        """
        links=self.driver.find_elements_by_xpath('html/body/section[2]/div/ul/li/a')

        count=len(links)
        for i in range(0,count):
            links = self.driver.find_elements_by_xpath('html/body/section[2]/div/ul/li/a')
            print(links[i].text)
            try:
                links[i].click()
            except:    pass


    def test_city(self):
            """
             Test case to verify city links
            """
            links1 = self.driver.find_elements_by_xpath('html/body/section[1]/div/ul/li/a')

            count = len(links1)
            for i in range(0,count):
                links1 = self.driver.find_elements_by_xpath('html/body/section[1]/div/ul/li/a')
                print((links1[i].text))
                try:
                    links1[i].click()
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





