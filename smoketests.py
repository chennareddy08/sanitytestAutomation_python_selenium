import unittest
from xmlrunner import xmlrunner

#from user_signup_login import TestAccount

from user_signup_login import TestAccount
from bookingsession import BookHandstand


# get all tests from SearchProductTest and HomePageTest class
test1 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
test2 = unittest.TestLoader().loadTestsFromTestCase(BookHandstand)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([test1, test2])

# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)

