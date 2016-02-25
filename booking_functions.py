# -*- coding: utf-8 -*-
import unittest,time
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from abc import abstractmethod
from selenium.webdriver.common.by import By
from datetime import date, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from base_function import BasePage







class Booking(object):
    """ All page objects inherit from this """


    def __init__(self,driver):
        self.driver  = driver
        self.wait = WebDriverWait(self.driver, 15)


    def findTrainer_button(self):
        """Function Verify find trainer buttin is visible"""
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"submit\"]")));


    def zipcode_field(self):
        """Function Verify zipcode field is visible"""
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(EC.element_to_be_clickable((By.ID,'zip-code')))

    def passportadd(self):
        self.wait = WebDriverWait(self.driver, 30)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#passport-ad > div.box")))

    def select_trainer(self):
        """Function Verify trainer list  is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='1887']/a/div[1]/img")))

    def trainer_passport_selection(self):
        """Function Verify try passport is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Try Passport")))

    def handstandchoicelist(self):
        """Function Verify thandstandchoice list is visible"""
        #self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.box > div:nth-of-type(1) > a > div.thumb-nail > img"))
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.box > div:nth-of-type(1) > a > div.thumb-nail > img")))

    def Book_button_trainers(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.jscroll-inner > div:nth-of-type(1) > div.box > div.caption > div.trainer-button > div.cta-traininglist > a > div.cta")))



    def HomeTab(self):
        """Function Verify Home Tab is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Home")))

    def ApplyToTrainerTab(self):
        """Function Verify Home Tab is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Apply to be a trainer")))

    def startBookingButton(self):
        """Function Verify startBookingButton is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-details > div.box > div.cta-row > div.cta")))
    def booking_button(self):

        """Function Verify BookingButton is visible"""
        self.wait = WebDriverWait(self.driver,15)
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='1742']/a/div")))

    def searcIcon(self):
        """Function Verify search icon is visible"""
        self.wait = WebDriverWait(self.driver,15)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type=\"submit\"]")))

    # def booking_button(self):
    #     return self.wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='1742']/a/div")))


    def clearsearch(self):
        """Function Verify clearsearch is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#clear-search")))

    def closebutton_bookingpage(self):
        """Function Verify closebutton on bookingpageis visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-details > div.box > div.close")))

    def closebutton_datepage(self):
         """Function Verify closebutton on datepage is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-when > div.box > div.close")))

    def closebutton_timepage(self):
         """Function Verify closebutton on time page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#trainer-time > div.box > div.close")))

    def closebutton_classtypeepage(self):
         """Function Verify closebutton on classtype page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#trainer-class > div.box > div.close")))

    def closebutton_locationpage(self):
         """Function Verify closebutton on location page page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#trainer-location > div.box > div.close")))

    def closebutton_reviewpage(self):
         """Function Verify closebutton on review page page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#trainer-review > div.box > div.close")))

    def forward_arrowbutton_bookingpage(self):
        """Function Verify forward arrowbutton on bookingpage is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-details > div.box > div.trainer-nav.forward")))

    def forward_arrowbutton_datepage(self):
        """Function Verify forward arrowbutton on datepage is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-when > div.box > div.trainer-nav.forward")))

    def forward_arrowbutton_timepage(self):
        """Function Verify forward arrowbutton on time page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR," #trainer-time > div.box > div.trainer-nav.forward")))


    def forward_arrowbutton_locationpage(self):
        """Function Verify forward arrowbutton on location page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-location > div > div.trainer-nav.forward")))

    def forward_arrowbutton_classtypepage(self):
        """Function Verify forward arrowbutton on class type page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-class > div.box > div.trainer-nav.forward")))


    def backwardarrowbutton_datepage(self):
        """Function Verify fbackward arrowbutton on datepage is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-when > div.box > div.trainer-nav.back")))


    def backwardarrowbutton_timepage(self):
        """Function Verify fbackward arrowbutton on datepage is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-time > div.box > div.trainer-nav.back")))

    def backwardarrowbutton_locationpage(self):
        """Function Verify backward arrowbutton on location page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-location > div > div.trainer-nav.back")))

    def backwardarrowbutton_classtypepage(self):
        """Function Verify backward arrowbutton on class type page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-class > div.box > div.trainer-nav.back")))

    def backwardarrowbutton_reviewpage(self):
        """Function Verify backward arrowbutton on review page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-review > div.box > div.trainer-nav.back")))

    def location_field(self):
         """Function Verify  on location field page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#session_location")))

    def nextbutton_locationpage(self):
        """Function Verify  on location field page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-location > div > article > div.cta-row > div")))

    def promo_field(self):
        """Function Verify  on promo field page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#promo")))

    def click_book_nowbutton(self):
        """Function Verify  on click on book now is visible"""
        return self.wait.until((EC.element_to_be_clickable((By.CSS_SELECTOR,"#bookBtn"))))


    def click_done_sessionconfirmation(self):
        """Function Verify  Done button is visible"""
        return self.wait.until((EC.element_to_be_clickable((By.LINK_TEXT,"Done"))))


    def individual_checbox(self):
        """Function Verify  on individual checkbox is visible"""
        return self.wait.until((EC.element_to_be_clickable((By.ID,"individual"))))


    def profileimage(self):
        """
        Function Verify  on profile image is visible
        """
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='profile-pic']/img")))



    def profiletab(self):

        """
        Function Verify  on profile tab is visible
        """
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='profile-dropdown']/ul/a[1]/li")))


    def workouttab(self):
        """
        Function Verify  on workout tab is visible
        """
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='profile-nav']/ul/a[1]/li")))


    def cancel_bookingbutton(self):
        """
        Function Verify  on cancel button is visible on workout section
        """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.cancel-cta.trainer-cancel")))

    def cancel_Nevermindbutton(self):
        """
        Function Verify  on Never mind  button is visible on cancel confirmation screen
        """
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cancel-close']")))

    def cancel_workoutbutton(self):

        """
        Function Verify  on cancel workout  button is visible on cancel confirmation screen
        """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#cancel-workoutBtn")))


    def group_checkbox(self):
         """Function Verify  on group checkbox is visible"""
         return self.wait.until((EC.element_to_be_clickable((By.ID,"group"))))

    def currentdate(self):
        """Function Verify currentdate on datepage """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#day-list > div:nth-of-type(1)")))

    def seconddate(self):
        """Function Verify seconddate on datepage """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#day-list > div:nth-of-type(2)")))

    def thirddate(self):
        """Function Verify thirddate on datepage """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#day-list > div:nth-of-type(3)")))

    def fourthdate(self):
        """Function Verify fourthdate on datepage """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#day-list > div:nth-of-type(4)")))

    def fifthdate(self):
        """Function Verify fifthdate on datepage """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#day-list > div:nth-of-type(5)")))

    def sixthdate(self):
        """Function Verify sixthdate on datepage """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#day-list > div:nth-of-type(6)")))

    def currenttime(self):
        """Function Verify currentdate on datepage """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#time-list > div:nth-of-type(1)")))

    def dateselect(self):
        datelist=self.driver.find_elements_by_xpath(".//*[@id='day-list']/div")
        print('Total no of dates available for booking are',len(datelist))
        try:
            for i in range(1,len(datelist)):
                print('The user selected date is',datelist[i].text)
                user_date=datelist[i].text
                #datelist[i].click()
        except:
            pass

    def classtype_select(self):
        classlist=self.driver.find_elements_by_xpath(".//*[@id='class-list']/div")
        print('Total no of class type available for booking are',len(classlist))
        try:
            for i in range(1,len(classlist)):
                classlist[i].click()
                #global user_class=classlist[i].text
        except:
            pass


    def leavemsg_widget(self):
        """Function Verify leavemsg widget is visisble """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.meshim_widget_widgets_BorderOverlay")))




    def time_list(self):
        datelist=self.driver.find_elements_by_xpath(".//*[@id='day-list']/div")
        #datelist=self.wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='day-list']/div")))
        #datelist=self.driver.find_elements_by_xpath(".//*[@id='day-list']/div")
        timelist=self.driver.find_elements_by_xpath(".//*[@id='time-list']/div")

        #e1 = (self.driver.execute_script("arguments[0].click()",timelist))
        print(len(timelist))





        from datetime import datetime, timedelta
        hours_from_now = datetime.now() + timedelta(hours=2)
        a='{:%I:%M%p}'.format(hours_from_now)

        #print(a)

        try:
            for i in range(1,6):
                print(datelist[i].text)
                cdate=datelist[i].text
                if (cdate==Booking.seconddate(self).text):
                    datelist[i].click()
                    (self.driver.execute_script("arguments[0].click()",timelist))

                    try:
                        for i in range(len(timelist)+1,64):
                            #print(timelist[i].text)
                           (self.driver.execute_script("arguments[0].click();",timelist))

                    except:
                        pass

                elif (cdate==Booking.currentdate(self).text):
                    datelist[i].click()
                    try:
                        for i in range(1,len(timelist)):
                            #print(timelist[i].text)
                            timelist[i].click()
                    except:
                        pass


                elif (cdate==Booking.thirddate(self).text):
                    datelist[i].click()
                    try:
                        for i in range(96):
                            #print(timelist[i].text)
                            timelist[i].click()
                    except:    pass


                elif (cdate==Booking.fourthdate(self).text):
                    datelist[i].click()
                    try:
                        for i in range(122):
                            #print(timelist[i].text)
                            timelist[i].click()
                    except:    pass

                elif (cdate==Booking.fifthdate(self).text):
                    datelist[i].click()
                    try:
                        for i in range(142):
                           # print(timelist[i].text)
                            timelist[i].click()
                    except:    pass

                elif(cdate==Booking.sixthdate(self).text):
                    datelist[i].click()
                    try:
                        for i in range(171):
                            #print(timelist[i].text)
                            timelist[i].click()
                    except:    pass


        except:
           for i in range(1,6):
               datelist[i].click()
               e1.click()
           # Booking.backwardarrowbutton_timepage(self).click()
           # Booking.currentdate(self).click()
           # Booking.currenttime(self).click()
           pass










    def zipcode_entry(self,zipcode):
        """Function Verify zipcode entry and navigate to trainer list screen """
        Booking.zipcode_field(self).clear()
        Booking.zipcode_field(self).send_keys(zipcode)
        Booking.findTrainer_button(self).click()


    def location_entry(self,location):
        """Function Verify location entry and navigate to class type screen list screen """
        Booking.location_field(self).clear()
        Booking.location_field(self).send_keys(location)
        Booking.nextbutton_locationpage(self).click()


    def login_slackVerify(self,email,password):

        self.driver.get("https://scienceinc.slack.com/messages/handstandapp/")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("signin_btn").click()
        self.driver.implicitly_wait(40)


    def booking_cleanup(self):
        BasePage.login_gmail(self,'handstandtest3@gmail.com','7259692024')
        self.driver.implicitly_wait(10)
        try:
            while self.driver.find_element_by_xpath("//div[@class='y6']/span[contains(.,'HandStand Booking Confirmation')]").text=="HandStand Booking Confirmation":
                self.driver.find_element_by_xpath("//div[@id=':3f']/div").click()
                self.driver.implicitly_wait(5)
                BasePage.gmail_logouttabdisplay(self).click()
        except NoSuchElementException:
             self.driver.find_element_by_css_selector("span.gb_Za.gbii").click()
             self.driver.find_element_by_id("gb_71").click()


    def promocode_entry_reviewpage(self,promo):
        """Function to Verify promo entry  """
        Booking.promo_field(self).clear()
        Booking.promo_field(self).send_keys(promo)

    def verify_sessionbooked_confirmation(self):
        """Function to Verify booking confirmation pop up msg  """

        self.assertTrue(self.is_element_present(By.XPATH, ".//*[@id='trainer-booked']"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-booked > div > header > h5"))
        self.driver.save_screenshot("booked1.png")
#        assert "Session Booked"==self.driver.find_element_by_css_selector("#trainer-booked > div > header > h5").text
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, " #final-review"))
        assert "Done"==self.driver.find_element_by_link_text("Done").text










    def trainerlistpagecheck(self):
        """
        This will check display of all element on trainer list screen

        """
        assert self.driver.find_element_by_css_selector("#logo").is_displayed()
        assert self.driver.find_element_by_css_selector("#top-nav > div.box").is_displayed()
        assert self.driver.find_element_by_css_selector("div.box > form").is_displayed()
        assert self.driver.find_element_by_css_selector("h4.label").is_displayed()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#date > object.calendar.filter-icon"))

        # assert self.driver.find_element_by_css_selector("#date > object.calendar.filter-icon")=={}
        assert self.driver.find_element_by_css_selector("#date-filter").is_displayed()
       # assert self.driver.find_element_by_css_selector("#time > object.clock.filter-icon")=={}
        assert self.driver.find_element_by_css_selector("#time-filter").is_displayed()
       # assert self.driver.find_element_by_css_selector("#class > object.mountain.filter-icon")=={}
        assert self.driver.find_element_by_css_selector("#class-filter").is_displayed()
        assert self.driver.find_element_by_css_selector("[name='search']").is_displayed()
        assert Booking.clearsearch(self).is_displayed()
        assert Booking.passportadd(self).is_displayed()
        assert self.driver.find_element_by_css_selector("div.jscroll-inner > div.box").is_displayed()
        assert self.driver.title=="Handstand"
        assert self.driver.find_element_by_css_selector("input[type=\"submit\"]").is_displayed()
        assert self.driver.find_element_by_css_selector("h2").is_displayed()
        assert self.driver.find_element_by_css_selector("h2").text=='PASSPORT'
        assert self.driver.find_element_by_css_selector("p").is_displayed()
        assert (self.driver.find_element_by_css_selector("p")).text=='Handstand Passport keeps you on track. Pay one membership fee a month and use all trainers and instructors at any time and any place. Try Handstand Passport today for one week absolutely free!'
        assert Booking.HomeTab(self).text =='Home'
        assert Booking.ApplyToTrainerTab(self).text=="Apply to be a trainer"
        assert self.driver.find_element_by_css_selector("img[alt=\"logomark.png\"]").is_displayed()
        assert self.driver.find_element_by_link_text("Sign Up/Log In").text=='Sign Up/Log In'
        assert self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > h4").text== "Handstand's Choice"
        # coding: cp1252
        assert self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul").text== "Lean Body Coaching, Tone Up! Butt Legs & Core, Weight Loss Coaching, Boxing, Hardcore Abs, Lean ‘n Mean Pilates,"
        demo=self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul")
        e1 = (self.driver.execute_script("return arguments[0].textContent",demo))
        print (e1)
        #assert e1=="""          Lean Body Coaching, Tone Up! Butt Legs & Core, Weight Loss Coaching, Boxing, Hardcore Abs, Lean ‘n Mean Pilates, Bootcamp, Power Yoga, Ballet, Cardio Dance Fit, Stretch and Recovery, Tennis							   """
        #assert self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul > li:nth-of-type(7)").text == "Bootcamp"
        self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul > li:nth-of-type(7)"))

        #a=self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul > li:nth-of-type(7)")

        # assert self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul > li:nth-of-type(8)").text=="Power Yoga,"
        # assert self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul > li:nth-of-type(9)").text=="Ballet,"
        # assert self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul > li:nth-of-type(10)").text=="Cardio Dance Fit,"
        # assert self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul > li:nth-of-type(11)").text=="Stretch and Recovery,"
        # assert self.driver.find_element_by_css_selector("div.box > div:nth-of-type(1) > a > div.caption > ul > li:nth-of-type(12)").text=="Tennis"
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"passport.png\"]"))

        assert self.driver.find_element_by_css_selector("img[alt=\"Handstand's Choice.jpg\"]").is_displayed()
        assert self.driver.find_element_by_xpath("//div[@id='1887']/a/div[2]/ul/li[4]").text=="Boxing,"
        assert self.driver.find_element_by_css_selector("img[alt=\"Handstand's Choice.jpg\"]").is_displayed()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe[src='about:blank']"))
        assert Booking.leavemsg_widget(self).is_displayed()
        self.driver.switch_to.default_content()











    def validate_startbookingPage(self):
        """
        This function to validate element present on start booking page
        """



        #self.assertTrue(self.driver.find_element_by_css_selector("#trainer-details > div.box > header > div:first-child > img").is_enabled())
        # demo3 = self.driver.find_element_by_css_selector("#trainer-details > div.box > header > h5")
        # e3 = (self.driver.execute_script("return arguments[0].textContent",demo3))
        # print (e3)
        # assert e3== "Handstand's Choice"
        #assert "Handstand's Choice"==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("#trainer-details > div > header > h5"))
        assert Booking.startBookingButton(self).text=="Start Booking"
        assert self.driver.find_element_by_css_selector("div.description > span").text=="Price:"
        assert self.driver.find_element_by_css_selector("div.descriptions > div:first-child > p").text=="$69"
        assert self.driver.find_element_by_css_selector("div.descriptions > div:nth-of-type(2) > span").text=="Workout Types:"
#        assert self.driver.find_element_by_css_selector("div.descriptions > div:nth-of-type(2) > p").text=="Lean Body Coaching,Tone Up! Butt Legs & Core,Weight Loss Coaching,Boxing,Hardcore Abs,Lean ‘n Mean Pilates,Bootcamp,Power Yoga,Ballet,Cardio Dance Fit,Stretch and Recovery,Tennis"
        assert self.driver.find_element_by_css_selector("#data > div > div:nth-child(3) > span").text=="About Me:"
        assert self.driver.find_element_by_css_selector("div.descriptions > div:nth-of-type(3) > p").text=="Book me to have Handstand " \
                                                                                                           "book a trainer of their choice for you"
        assert self.driver.find_element_by_css_selector("div.descriptions > div:nth-of-type(4) > span").text=="What to Expect:"
        assert self.driver.find_element_by_css_selector("div.descriptions > div:nth-of-type(4) > p").text=="I will bring all the equipment necessary and send you a text an hour before our appointment. Don't move a muscle until I get there! When I arrive, we'll start with a friendly introduction and then review any injuries you may have so I can accommodate for you! Then we can move right into our stretch, warm up, and our workout!"
        assert Booking.closebutton_bookingpage(self).is_displayed()
        assert Booking.forward_arrowbutton_bookingpage(self).is_displayed()

        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe[src='about:blank']"))
        assert Booking.leavemsg_widget(self).is_displayed()
        self.driver.switch_to.default_content()


    def validate_datepage(self):
        """This function validate the element present on date page"""

        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-when > div.box > header > div:first-child > img"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-when > div > header > h5"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-when > div > header > div.ranking.ranking-rated"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-when > div.box > div.description-row > ul.progressbar"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-when > div.box > div.description-row > h5 > span"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-when > div > div.description-row > h5"))
        print(self.driver.find_element_by_css_selector("#trainer-when > div.box > div.description-row > h3").text)
        assert "When"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#trainer-when > div.box > div.description-row > h3"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-when > div.box > div.description-row > h3 "))

        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#day-list"))

        start = date.today()
        current_day= "{:%m/%d/%Y}".format(start).lstrip('0')


              # getting second day
        future = start + timedelta(days=1)
        second_day="{:%m/%d/%Y}".format(future).lstrip('0')


             #getting 3rd day
        start = date.today()
        future = start + timedelta(days=2)
        third_day="{:%m/%d/%Y}".format(future).lstrip('0')


        #getting 4th day
        start = date.today()
        future = start + timedelta(days=3)
        fourth_day="{:%m/%d/%Y}".format(future).lstrip('0')


            #getting 5th day
        start = date.today()
        future = start + timedelta(days=4)
        fifth_day="{:%m/%d/%Y}".format(future).lstrip('0')


        #getting 6 th day
        start = date.today()
        future = start + timedelta(days=5)
        sixth_day="{:%m/%d/%Y}".format(future).lstrip('0')

        # assert Booking.currentdate(self).text==current_day
        # assert Booking.seconddate(self).text==second_day
        # assert Booking.thirddate(self).text==third_day
        # assert Booking.fourthdate(self).text==fourth_day
        # assert Booking.fifthdate(self).text==fifth_day
        # assert Booking.sixthdate(self).text==sixth_day
        assert Booking.backwardarrowbutton_datepage(self).is_displayed()
        assert Booking.forward_arrowbutton_datepage(self).is_displayed()
        assert Booking.closebutton_datepage(self).is_displayed()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe[src='about:blank']"))
        assert Booking.leavemsg_widget(self).is_displayed()
        self.driver.switch_to.default_content()
        assert Booking.currentdate(self).is_displayed()
        assert Booking.seconddate(self).is_displayed()
        assert Booking.thirddate(self).is_displayed()
        assert Booking.fourthdate(self).is_displayed()
        assert Booking.fifthdate(self).is_displayed()
        assert Booking.sixthdate(self).is_displayed()


    def verifytimepage(self):

        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-time > div.box > header > div:first-child > img"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-time > div.box > header > h5"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-time > div > header > div.ranking.ranking-rated"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-time > div.box > div.description-row > ul.progressbar"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR," #trainer-time > div.box > div.description-row > h5"))
        assert "Time"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#trainer-time > div.box > div.description-row > h3"))
        print(self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#trainer-time > div.box > div.description-row > h3")))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR," #trainer-time > div.box > article.bottom-section"))
        a=self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#time-list"))
        #print(a)
        assert a==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#time-list"))
        # # a[59:67].click()
        # # print(a[59:67])
        # x1=".//*[@id='time-list']/div["
        #
        # for i in range(1,158):
        #
        #     print(self.driver.find_element_by_xpath(".//*[@id='time-list']/div[156]"))
        #     b=self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(self.driver.find_element_by_xpath(".//*[@id='time-list']/div[i]")))
        #     print(b)
        assert Booking.closebutton_timepage(self).is_displayed()
        assert Booking.backwardarrowbutton_timepage(self).is_displayed()
        assert Booking.forward_arrowbutton_timepage(self).is_displayed()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe[src='about:blank']"))
        assert Booking.leavemsg_widget(self).is_displayed()
        self.driver.switch_to.default_content()


    def location_verifypage(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-location > div.box > header > div:first-child > img"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, " #trainer-location > div.box > header > h5"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-location > div > header > div.ranking.ranking-rated"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-location > div.box > div.description-row > ul.progressbar"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR," #trainer-location > div.box > div.description-row > h5"))
        assert Booking.closebutton_locationpage(self).is_displayed()
        assert Booking.forward_arrowbutton_locationpage(self).is_displayed()
        assert Booking.backwardarrowbutton_locationpage(self).is_displayed()
        assert "Location"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#trainer-location > div.box > div.description-row > h3"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR," #trainer-location > div.box > article.bottom-section"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#location-search"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#location-search > svg"))
        assert "Next"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#trainer-location > div > article > div.cta-row > div"))
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe[src='about:blank']"))
        assert Booking.leavemsg_widget(self).is_displayed()
        self.driver.switch_to.default_content()

    def verify_classtypepage(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-class > div.box > header > div:first-child > img"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, " #trainer-class > div.box > header > h5"))

        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-class > div > header > div.ranking.ranking-rated"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-class > div.box > div.description-row > ul.progressbar"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-class > div.box > div.description-row > h5"))
        assert "Class Type"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#trainer-class > div.box > div.description-row > h3"))

        assert "Lean Body Coaching"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='0']"))
        assert "Tone Up! Butt Legs & Core"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='1']"))
        assert "Weight Loss Coaching"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='2']"))
        assert "Boxing"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='3']"))
        assert "Hardcore Abs"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='4']"))
        assert "Lean ‘n Mean Pilates"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='5']"))
        assert "Bootcamp"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='6']"))
        assert "Power Yoga"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='7']"))

        #assert "Ballet"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='8']"))
        assert "Cardio Dance Fit"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='8']"))
        assert "Stretch and Recovery"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='9']"))
        assert "Tennis"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_xpath(".//*[@id='10']"))
        self.driver.find_elements_by_css_selector("#class-list")
        assert Booking.closebutton_classtypeepage(self).is_displayed()
        assert Booking.forward_arrowbutton_classtypepage(self).is_displayed()
        assert Booking.backwardarrowbutton_classtypepage(self).is_displayed()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe[src='about:blank']"))
        assert Booking.leavemsg_widget(self).is_displayed()
        self.driver.switch_to.default_content()

    def verify_reviewpage(self):
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-review > div.box > header > div:first-child > img"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-review > div.box > header > h5"))

        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-review > div > header > div.ranking.ranking-rated"))

        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-review > div.box > div.description-row > ul.progressbar"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#trainer-review > div.box > div.description-row > h5"))
        #assert "Review"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#trainer-review > div.box > div.description-row > h3"))
        #assert "When:" == self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#reviews > div:nth-child(1) > span"))
        #assert "Where:"==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#reviews > div:nth-of-type(2) > span.title"))
        # assert "Workout Type:"==self.driver.execute_script("return argument[0].textContent" ,self.driver.find_element_by_css_selector("#reviews > div:nth-of-type(3) > span.title"))
        # assert "Workout Size:"==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("#reviews > div:nth-of-type(4) > span.title"))
        # assert "Promo:"==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("#reviews > div:nth-of-type(5) > span.title"))
        # assert "Additional Comments:"==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("#reviews > div:nth-of-type(6) > span"))
        # assert "List any injuries, concerns, or instructions for your trainer"==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("#comments"))

        # assert Booking.dateselect(self)==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("p > span:first-child"))
        # assert Booking.timelist(self)==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("p > span:nth-of-type(2)"))
        # assert Booking.classtype_select(self).user_class==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("#class-type"))
        # a=self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("#reviews > div:nth-of-type(4) > p:nth-of-type(1)"))
        # print(a)
        # assert "Small group + $10"==self.driver.execute_script("return argument[0].textContent",self.driver.find_element_by_css_selector("#reviews > div:nth-of-type(4) > p:nth-of-type(2)"))
        # #assert "1:1 $69"=
        assert Booking.closebutton_reviewpage(self).is_displayed()
        assert Booking.backwardarrowbutton_reviewpage(self).is_displayed()
        assert Booking.individual_checbox(self).is_selected()
        assert Booking.group_checkbox(self).is_displayed()

        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe[src='about:blank']"))
        assert Booking.leavemsg_widget(self).is_displayed()
        self.driver.switch_to.default_content()




    def verify_cancelworkoutpage_confirmation(self):
        assert 'Cancel Workout' == self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#workout-cancel > div.box > header > h5"))
        e3=self.driver.find_element_by_css_selector("form > div.details")
        print(self.driver.execute_script("return arguments[0].textContent",e3))
        #assert "Are you sure you want to cancel this workout ?"== self.driver.execute_script("return arguments[0].textContent",e3)

    def verify_workoutblocked_popup(self):
        assert 'Workout Blocked'==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#workout-cancel > div.box > header > h5"))


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
