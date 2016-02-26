__author__ = 'Chennareddy'
import unittest
import HTMLTestRunner
import os
from user_signup_login import TestAccount
from bookingsession import BookHandstand
dir = os.getcwd()
tests1 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
tests2 = unittest.TestLoader().loadTestsFromTestCase(BookHandstand)
all_tests = unittest.TestSuite([tests1,tests2])

outfile = open(dir+"/TestReport.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       verbosity=1,
                                       title="Selenium Test Report",
                                       description="Testing Web Project 1")
runner.run(all_tests)
#unittest.TextTestRunner(verbosity=2).run(all_tests)
