import unittest
from xmlrunner import xmlrunner

#from user_signup_login import TestAccount

from .user_signup_login import TestAccount
from .bookingsession import BookHandstand
from .bookingsession_groups import Book_small_group
from .city_classtype import city_classtypelinks
from .all_link import links
from .setting_screen_validation import settingscreen

# get all tests from SearchProductTest and HomePageTest class
test1 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
test2 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
test3 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
test4 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
test5 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([test1, test2, test3, test4,test5])

# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)

