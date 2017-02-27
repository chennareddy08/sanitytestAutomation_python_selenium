import unittest,time,os,re,string,random,sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
#from base_function import BasePage
import base_function,booking_functions
from basetestcase import BaseTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException





class settingscreen(BaseTestCase):

    def test_updateBasicsSettings(self):
        """
                Test case to update basic settings
               """
        target = base_function.BasePage(self.driver)
        BP=booking_functions.Booking(self.driver)
        BP.Navigate_workoutscreen()
        self.driver.back()
        assert self.driver.find_element_by_css_selector('#settingsForm > p:nth-child(1)').text == 'Basics'
        target.update_basicdetails('testc1','b','testjc88@gmail.com','8557871111')

    def test_updateDefaultZipcode(self):
        """
        Test case to update default zipcode in settings
         """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_workoutscreen()
        self.driver.back()
        assert self.driver.find_element_by_css_selector('#settingsForm > p:nth-child(5)').text == 'Default Zip Code'
        self.driver.find_element_by_link_text("change").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_css_selector('#zipSearchPanel > a').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_link_text("change").click()


        #driver.find_element_by_xpath("//button[@type='submit']").click()
        target.defaultzipcode().clear()
        target.defaultzipcode().send_keys('90405')
        time.sleep(1)
        target.defaultzipcode().send_keys(Keys.ARROW_DOWN)
        target.savechange_setting().click()
        self.driver.find_element_by_css_selector("#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:pass

    def test_updateCreditCardInfo(self):
        """
        Test case to update CreditCardInfo in settings
        """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_workoutscreen()
        self.driver.back()
        assert self.driver.find_element_by_css_selector('#settingsForm > p:nth-child(8)').text == 'Credit Card Info'
        self.driver.find_element_by_css_selector('#ccPreviewPanel > div > div > div > a.pull-right').click()
        self.driver.find_element_by_link_text('cancel').click()
        self.driver.find_element_by_css_selector('#ccPreviewPanel > div > div > div > a.pull-right').click()
        self.driver.find_element_by_id('creditNumber').send_keys('5105105105105100')
        Select(self.driver.find_element_by_id('creditMonth')).select_by_visible_text('September')
        Select(self.driver.find_element_by_id('creditYear')).select_by_visible_text('2018')
        self.driver.find_element_by_id('creditCVC').send_keys('123')
        self.driver.implicitly_wait(1)
        target.savechange_setting().click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector( '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:pass

    def test_passportPlanChange(self):
        """
        Test case to update CreditCardInfo in settings
                """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_workoutscreen()
        self.driver.back()
        assert self.driver.find_element_by_css_selector('#settingsForm > p:nth-child(11)').text == 'Passport Plan'
        self.driver.find_element_by_css_selector('#PassportPreviewPanel > div > div > a').click()
        self.driver.find_element_by_css_selector('#PassportSelectPanel > a').click()
        self.driver.find_element_by_css_selector('#PassportPreviewPanel > div > div > a').click()
        self.driver.find_element_by_css_selector('#PassportSelectPanel > div > ul > li:nth-child(2) > label').click()
        target.savechange_setting().click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        assert self.driver.find_element_by_css_selector(
            '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        self.driver.find_element_by_css_selector('#PassportPreviewPanel > div > div > a').click()
        self.driver.find_element_by_css_selector('#PassportSelectPanel > div > ul > li:nth-child(1) > label').click()
        target.savechange_setting().click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        assert self.driver.find_element_by_css_selector(
            '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"


    def test_changePassword(self):
        """
               Test case to change the password in settings
                       """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_workoutscreen()
        self.driver.back()
        assert self.driver.find_element_by_css_selector('#settingsForm > p:nth-child(14)').text == 'Change Password'
        target.password_field().send_keys('8892279018')
        target.confirm_password().send_keys('8892279018')


    def test_uploadphoto(self):
        """
        Test case to change the password in settings
        """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_workoutscreen()
        self.driver.find_element_by_link_text('Change Photo').click()
        target.fileToChoose().send_keys(os.getcwd() + "/chad.png")
        target.uploadPhoto_button().click()
        self.driver.implicitly_wait(2)

    def test_traineZipcode_whereToOperate(self):
        """
                Test case to change the zipocde in settings
                """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_TrainerprofileScreen('test65@gmail.com','123456')
        assert self.driver.find_element_by_css_selector('#profileForm > div:nth-child(1) > label').text == 'The zip code where you operate'
        self.driver.find_element_by_link_text("change").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_css_selector('#zipSearchPanel > div > div > a').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_link_text("change").click()
        self.driver.implicitly_wait(5)
        BP.location_field_trainer().send_keys(90405)
        time.sleep(1)
        BP.location_field_trainer().send_keys(Keys.ARROW_DOWN)
        target.savchange_trainerProfile().click()
        self.driver.find_element_by_css_selector("#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:pass

    def test_miles_toTravel(self):
        """test case to update the mile to travel """

        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_TrainerprofileScreen('test65@gmail.com', '123456')
        assert self.driver.find_element_by_css_selector("#profileForm > div:nth-child(2) > label").text == "How many miles are you willing to travel?"
        buttonlist = self.driver.find_elements_by_xpath( "//*[@id='app-layout']/section[1]/div/form/div/div[2]/div[2]/div/label")
        try:
            for i in range(1, len(buttonlist)):
                print(('The Number of radio buttons are', buttonlist[i].text))
                buttonlist[i].click()
        except:
            pass
        target.savchange_trainerProfile().click()
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector(
                '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:
            pass

    def test_aboutMe(self):
        """testcase to update the About Me"""

        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_TrainerprofileScreen('test65@gmail.com', '123456')
        assert self.driver.find_element_by_css_selector('#profileForm > div:nth-child(3) > label').text == 'About me'
        target.aboutMe().clear()
        target.aboutMe().send_keys("""
        I've been a meditation and holistic lifestyle guide for the past
        5 years, my rock bottom launched me into a deep spiritual exploration.
        I learned all different modalities and found myself very attracted to kundalini yoga and meditation.
        I practice is not limited to kundalini though, I love guiding people using mantra and visualization as well.
        I believe a good yoga practice is not only physically stretching but mentally stretching
        so I love that kundalini pairs asanas and meditations. """)
        target.savchange_trainerProfile().click()
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector(
                '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:
            pass

    def test_YearsOfExperience(self):
        """
        test case to update year of experirnce
        """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_TrainerprofileScreen('test65@gmail.com', '123456')
        assert self.driver.find_element_by_css_selector('#profileForm > div:nth-child(4) > label').text == 'Years of experience'
        target.years_experience().clear()
        target.years_experience().send_keys(8)
        target.savchange_trainerProfile().click()
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector(
                '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:
            pass


    def test_AccoladesCertifications(self):
        """
        testcase to update AccoladesCertifications

        """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_TrainerprofileScreen('test65@gmail.com', '123456')
        assert self.driver.find_element_by_css_selector('#profileForm > div:nth-child(5) > label').text == 'Accolades or Certifications'
        target.accolades_certifications().clear()
        target.accolades_certifications().send_keys("""
        Kundalini Yoga and Meditation Teacher
        New Moon Full Moon Meditation Guide at Unplugged
        Certified Holistic Health Coach
        Author of Eat with Intention
        Healthy Happy Living Guru from ABC's The Taste
        Founder of Aprecity a mind body soul support """)

        target.savchange_trainerProfile().click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector(
                '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:
            pass

    def test_Specialties(self):
        """
        testcase to update specilites
        """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_TrainerprofileScreen('test65@gmail.com', '123456')
        assert self.driver.find_element_by_css_selector('#profileForm > div:nth-child(6) > label').text == "Specialties"
        specialtieslist = self.driver.find_elements_by_xpath(
            ".//*[@id='app-layout']/section/div/form/div/div[2]/div/div")
        try:
            for i in range(1, len(specialtieslist)):
                specialtieslist[i].click()
        except:
            pass
        target.savchange_trainerProfile().click()
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector(
                '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:
            pass

    def test_trainerAvailability(self):
        """
        testcase to update trainer availability
        """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_TrainerprofileScreen('test65@gmail.com', '123456')
        self.driver.find_element_by_link_text('My Availability').click()
        assert self.driver.find_element_by_css_selector('#availabilityForm > div > div > h3').text == 'Availability'

        checkboxes = self.driver.find_elements_by_css_selector("#availabilityForm > div > div > div > table > tbody > tr:nth-child(n) > td")
        for checkbox in checkboxes:
            checkbox.click()
        target.savchange_availability().click()
        checkboxes1 = self.driver.find_elements_by_css_selector("#availabilityForm > div > div > div > table > tbody > tr:nth-child(n) > td")

        for checkbox1 in checkboxes1:
            checkbox1.click()
        target.savchange_availability().click()
        self.driver.find_element_by_css_selector(
            "#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        try:
            assert self.driver.find_element_by_css_selector(
                '#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"
        except:
            pass

    def test_NavigationBetweenSetting_screen(self):
        """
                testcase to verify Navigation between setting screen
                """
        target = base_function.BasePage(self.driver)
        BP = booking_functions.Booking(self.driver)
        BP.Navigate_TrainerprofileScreen('test65@gmail.com', '123456')
        self.driver.find_element_by_link_text('My Availability').click()
        self.driver.implicitly_wait(1)
        assert self.driver.find_element_by_css_selector('#availabilityForm > div > div > h3').text == 'Availability'
        self.driver.find_element_by_link_text('Upcoming Bookings').click()
        self.driver.implicitly_wait(1)
        assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > h3').text == 'My Upcoming Bookings'
        self.driver.find_element_by_link_text('Change Photo').click()
        self.driver.implicitly_wait(1)
        assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > div > form > h6:nth-child(1)').text == 'Select image to upload:'
        self.driver.find_element_by_link_text("Settings").click()
        self.driver.implicitly_wait(1)
        assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > h3').text == 'Account Settings'
        self.driver.find_element_by_link_text('My Workouts History').click()
        self.driver.implicitly_wait(1)
        print((self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > h3').text))
        assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > h3').text == 'My Workouts History'
        self.driver.find_element_by_link_text('My Upcoming Workouts').click()
        self.driver.implicitly_wait(1)
        print((self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > h3').text))
        assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > h3').text == 'My Workouts'


    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(os.getcwd() + '/screenshots/' + test_method_name + "-" + now + ".png")
    # close browser window
        self.driver.quit()

    

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


if __name__ == "__main__":
    unittest.main()




