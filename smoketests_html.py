__author__ = 'Chennareddy'

import unittest
import HTMLTestRunner
import os

from user_signup_login import TestAccount
from bookingsession import BookHandstand
from bookingsession_groups import Book_small_group
from city_classtype import city_classtypelinks
from all_link import links
from setting_screen_validation import settingscreen
from apply_tobe_trainer import  TestTrainerAccount

dir = os.getcwd()
tests1 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
tests2 = unittest.TestLoader().loadTestsFromTestCase(BookHandstand)
tests3 = unittest.TestLoader().loadTestsFromTestCase(Book_small_group)
tests4 = unittest.TestLoader().loadTestsFromTestCase(city_classtypelinks)
tests5 = unittest.TestLoader().loadTestsFromTestCase(links)
tests6 = unittest.TestLoader().loadTestsFromTestCase(settingscreen)
tests7 = unittest.TestLoader().loadTestsFromTestCase(TestTrainerAccount)

all_tests = unittest.TestSuite([tests1,tests2,tests3,tests4,tests5,tests6,tests7])

outfile = open(dir+"/Reports/TestReport.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       verbosity=1,
                                       title="Handstand Web Automation Test Report",
                                       description="Test Automation Report")
runner.run(all_tests)
#unittest.TextTestRunner(verbosity=2).run(all_tests)
