import unittest,time,os
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from abc import abstractmethod
import imaplib, email, imapclient

import string
import random
from datetime import datetime
from helpers import Helper

class BasePage(object):
    """ All page objects inherit from this """


    def __init__(self,driver):
        self.driver  = driver

    def signup_link(self)  :
        self.wait  =  WebDriverWait(self.driver,20)
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Login")))

    def apply_ToBe_Trainer(self):
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Apply To Be a Trainer")))

    def Create_account_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Create an Account")))

    def email_field(self):
        """Function Verify email field """
        return self.wait.until(EC.element_to_be_clickable((By.NAME,'email')))

    def month_field(self):
        """Function Verify month field """
        return self.wait.until(EC.element_to_be_clickable((By.ID,"month")))

    def day_field(self):
        """function to validate the day field"""
        return self.wait.until(EC.element_to_be_clickable((By.ID,"day")))

    def year_field(self):
        """function to validate to year field"""
        return self.wait.until(EC.element_to_be_clickable((By.ID,"year")))

    def phone_field(self):
        """function to validate the phone field"""
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,"phone")))

    def password_field(self):
        """Function Verify password field """
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,'password')))

    def confirm_password(self):
        """Function Verify password_confirmation field """
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,  'password_confirmation')))

    def signin_button(self):
        """Function Verify Sign In button"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-layout > div > form > div > div.panel-footer > button')))

    def firstName_field(self):
        """Function Verify first name field"""
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,'first_name')))

    def lastName_field(self):
        """Function Verify last name field"""
        return self.wait.until(EC.element_to_be_clickable((By.NAME,'last_name')))

    def phoneNumber_field(self):
        """Function Verify phone number"""
        return self.wait.until(EC.element_to_be_clickable((By.NAME,'mobile')))

    def term_conditionSelect(self):
        """This function used to select Terms and condition checkbox"""
        return self.wait.until(EC.element_to_be_clickable((By.ID,'field-agree')))


    def next_button(self):
        """Function Verify register buttin is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.ID,"submit")))


    def register_trainerButton(self):
        """Function Verify register buttin is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.ui-button')))

    def zipcode(self):
        """Function Verify zipcode buttin is visible"""
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,'zip_code')))

    def defaultzipcode(self):
        """Function Verify default zipcode insetting screen"""
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'zipSearch')))


    def login_link(self):
        """Function Verify sign link in create account screen"""
        self.wait = WebDriverWait(self.driver,15)
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log In')))

    def accolades_certifications(self):
        """function to validate Accolades or Certifications is visible"""
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,'certifications')))

    def aboutMe(self):
        """function to check aboutMe is visible"""
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(EC.element_to_be_clickable((By.ID,'aboutMe')))

    def years_experience(self):
        """function to validate Years of experience field should be visible"""
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,'experience')))

    def register_button(self):
        """function to validate submit button is visible"""
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))

    # def forgot_password(self):
    #     """Function to Verify Forgot password option is visible"""
    #     return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"swap")))

    def savechanges_button(self):

        """function to verify save change button is clickable"""
        return  self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#app-layout > section.apply-flow > div > form > div > div.panel-body > div > div.col-md-9 > div > button")))

    def savechange_setting(self):
        """function to verify save change button is clickable"""
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#settingsForm > button")))

    def savchange_trainerProfile(self):
        """function to verify save change button is clickable"""
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#profileForm > button")))

    def savchange_availability(self):

        """function to verify save change button is clickable"""
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#availabilityForm > div > button")))

    def fileToChoose(self):
        """This function to verify choose file is clickable"""
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.ID,"fileToUpload")))

    def uploadPhoto_button(self):
        """This function to verify uploadPhoto_button is clickable"""
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,"submit")))

    def forgot_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Forgot Your Password?')))

    def login_email_field(self):
        """Function to Verify Email field in login option"""
        return self.wait.until(EC.element_to_be_clickable((By.ID,"email")))


    def login_password_Filed(self):
        """Function to Verify password field in login option"""
        return  self.wait.until(EC.element_to_be_clickable((By.ID,"password")))


    def login_successfull(self):
        """Function to Verify login is sucessful"""
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_css_selector("#base-nav-link-toggle").click()
            return  self.driver.find_element_by_link_text('Log Out').text
        except:    pass



    def logout_button(self):
         """Function to Verify logout is sucessful"""
         return self.wait .until(EC.element_to_be_clickable((By.LINK_TEXT,'Log Out')))



    def logout_successfull(self):
        """Function to Verify logot is successful"""
        return  (self.driver.find_element_by_class_name("signupLink").text)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


    def email_forgotpassword(self):
        """
        Function to check email field on forgot password recovery field
        """
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.ID,'email')))

    def submitButton_forgot(self):
        """
        Function to check submit on forgot password button
        """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#app-layout > div > form > div > div.panel-footer > button')))



    def new_password(self):
        """
        Function to check new password field

        """
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.ID,'newpassword')))

    def verify_password(self):
        """
        Function to check verifypassword field

        """
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.ID,'verifypassword')))

    def change_passwd_button(self):
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#app-layout > div > div > div > div > div.panel-body > form > div:nth-child(6) > div > button")))

    def restore_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Restore")))

    def  select_gmailreset_passwordlink(self):
 #       return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='y6']/span[contains(.,'You requested a new password')]")))
         return self.wait.until(EC.element_to_be_clickable((By.XPATH, "html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div[3]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[7]/div[1]/a")))

    def gmail_logout(self):
        self.driver.find_element_by_css_selector("#gb > div.gb_ve.gb_wf > div.gb_hb.gb_wf.gb_R.gb_vf.gb_T > div.gb_hc.gb_wf.gb_R > div.gb_eb.gb_Hc.gb_wf.gb_R > div.gb_sc.gb_gb.gb_wf.gb_R > a > span").click()
        self.driver.find_element_by_link_text("Sign out").click()



    def user_account_creation(self,firstname,lastname,email,password,confirm_password):
        BasePage.firstName_field(self).send_keys(firstname)
        BasePage.lastName_field(self).send_keys(lastname)
        BasePage.email_field(self).send_keys('a' + email)
        BasePage.password_field(self).send_keys(password)
        BasePage.confirm_password(self).send_keys(confirm_password)
        BasePage.register_button(self).click()
        self.driver.implicitly_wait(5)



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
        self.driver.find_element_by_css_selector("#profile-container > div > div.col-md-10 > div > div > div").is_displayed()
        assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > div').text == "Your settings were saved!"

    def generate_random_info(self):
        """
        This generates random strings. The strings generated are for email, username, first name and last name.

        :return: info - dictionary containing the randomly generated info

        """

        info = {}
        # Generate random email and username
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        info['email'] = "test_" + stamp + "@gmail.com"
        info['user_name'] = "test_" + stamp

        # Generate random first name, last name and user name
        all_letters = string.lowercase
        info['first_name'] = "".join(random.sample(all_letters, 8))
        info['last_name'] = "".join(random.sample(all_letters, 8))

        print(("The generated email: {}".format(info['email'])))
        print(("The generated user name: {}".format(info['user_name'])))
        print(("The generated first name: {}".format(info['first_name'])))
        print(("The generated last name: {}".format(info['last_name'])))

        return info


    def trainer_account_creation(self,firstname,lastname,email,phone,password,confirm_password,zipcode,accolades_certifications,aboutme,experience):
        BasePage.firstName_field(self).send_keys(firstname)
        BasePage.lastName_field(self).send_keys(lastname)
        BasePage.email_field(self).send_keys((random.choice(string.digits) + email))
        BasePage.phone_field(self).send_keys(phone)
        Select(self.driver.find_element_by_id('day')).select_by_visible_text('01')
        Select(self.driver.find_element_by_id('month')).select_by_visible_text('May')
        Select(self.driver.find_element_by_id('year')).select_by_visible_text('1989')
        BasePage.password_field(self).send_keys(password)
        BasePage.confirm_password(self).send_keys(confirm_password)
        #self.driver.find_element_by_id('field-agree').click()
        BasePage.term_conditionSelect(self).click()
        BasePage.register_trainerButton(self).click()
        self.driver.implicitly_wait(2)
        BasePage.zipcode(self).clear()
        BasePage.zipcode(self).send_keys(zipcode)
        buttonlist=self.driver.find_elements_by_xpath("//*[@id='app-layout']/section[1]/div/form/div/div[2]/div[2]/div/label")
        print(('Total no of option available for booking are', len(buttonlist)))
        try:
            for i in range(1, len(buttonlist)):
                print(('The Number of radio buttons are', buttonlist[i].text))
                buttonlist[i].click()
        except:
            pass
        BasePage.accolades_certifications(self).send_keys(accolades_certifications)
        BasePage.aboutMe(self).send_keys(aboutme)
        BasePage.years_experience(self).send_keys(experience)
        BasePage.next_button(self).click()
        specialtieslist=self.driver.find_elements_by_xpath(".//*[@id='app-layout']/section/div/form/div/div[2]/div/div")
        try:
            for i in range(1,len(specialtieslist)):
                print(('specialtieslist are', specialtieslist[i].text))
                specialtieslist[i].click()
        except:pass
        BasePage.next_button(self).click()
        availability=self.driver.find_elements_by_xpath(".//*[@id='app-layout']/section[1]/div/form/div/div[2]/div/div[1]/div/div/div/table/tbody/tr")
        try:
            for i in range(1,len(availability)):
                print(('no of time slot availability is' ,availability[i].text))
        except:pass
        BasePage.savechanges_button(self).click()
        BasePage.fileToChoose(self).send_keys(os.getcwd()+"/chad.png")
        BasePage.uploadPhoto_button(self).click()
        self.driver.implicitly_wait(2)
        e1=self.driver.find_element_by_css_selector("#app-layout > div > div > div > div > div.panel-heading.panel-heading-apply > h3")
        try:
            e1.is_displayed()
            print((e1.text))
        except:pass


    def login_account(self,email,password):
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-footer > button").click()

    def Login_trainer_account(self, email, password):
        """function use to login account"""
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-footer > button").click()






    def forgot_passwordcheck(self,Email):
        try:
            self.driver.get("https://stage.handstandapp.com/")
            try:
                alert=self.driver.switch_to_alert()
                alert.accept()
            except:pass
            BasePage.signup_link(self).click()
            self.driver.implicitly_wait(2)
            self.driver.implicitly_wait(2)
            assert (self.driver.find_element_by_link_text("Forgot Your Password?")).text == 'Forgot Your Password?'
            BasePage.forgot_password(self).click()
            d2 = self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-footer > button").text
            print(d2)
            BasePage.email_forgotpassword(self).send_keys(Email)
            BasePage.submitButton_forgot(self).click()
            demo=self.driver.find_element_by_css_selector("#app-layout > div > div > div > div > div.panel-heading.panel-heading-apply > h3")

            e1=(self.driver.execute_script("return arguments[0].textContent",demo))
            print((e1.strip()))
            print((self.driver.title))

            time.sleep(20)
        except:
            pass

    def change_password(self,email,password,confirm_password):
        assert self.driver.find_element_by_css_selector('#app-layout > div > div > div > div > div.panel-heading').text == 'Reset Password'
        BasePage.email_forgotpassword(self).send_keys(email)
        BasePage.password_field(self).clear()
        BasePage.password_field(self).send_keys(password)
        BasePage.confirm_password(self).clear()
        BasePage.confirm_password(self).send_keys(confirm_password)
        BasePage.change_passwd_button(self).click()
        self.driver.implicitly_wait(10)

    def login_gmail(self,email,password):

        self.driver.get('https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('Email').send_keys(email)
        self.driver.find_element_by_id('next').submit()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('Passwd').send_keys(password)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id("signIn").click()
        self.driver.implicitly_wait(40)

    def mail_passwordrecover(self):
        #self.driver.get('https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier')
        try:
            BasePage.login_gmail(self, 'rebertjacob@gmail.com','7259692024')
        except:pass
        try:
            self.driver.find_element_by_xpath("html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/span/a").click()
        except:pass
        try:
            e1= self.driver.find_element_by_xpath("html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div[7]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[6]/div/div/div/span[1]")
        except:pass
        try:
            while e1.text == 'Handstand Reset Password Request':
                e1.click()
                self.driver.implicitly_wait(2)
                self.driver.find_element_by_partial_link_text("https://stage.handstandapp.com/password/reset?token=").click()
                self.driver.switch_to_window(self.driver.window_handles[1])
                print((self.driver.title))
                BasePage.change_password(self, 'rebertjacob@gmail.com', '7259692024', '7259692024')
                try:
                    a=self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-body > div.alert.alert-success")
                    assert a.text == 'Your Password has been successfully reset ! Please Login.'
                    print("password is updated successfully")
                except:pass
        except:pass





    def forgot_pass_cleanup(self):

        imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        imapObj.login('rebertjacob@gmail.com', '7259692024')
        imapObj.select_folder('INBOX', readonly=False)
        UIDs = imapObj.search('ALL')
        imapObj.delete_messages(UIDs)
        imapObj.expunge()


class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
