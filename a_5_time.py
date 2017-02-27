
import unittest
import HTMLTestRunner
import os

from user_signup_login import TestAccount
dir = os.getcwd()


# get all tests from SearchProductTest and HomePageTest class
test1 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
test2 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
# test3 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
# test4 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
# test5 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([test1])



outfile = open(dir+"/Reports/TestReport.html", "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       verbosity=1,
                                       title="Handstand Web Automation Test Report",
                                       description="Test Automation Report")
runner.run(smoke_tests)
