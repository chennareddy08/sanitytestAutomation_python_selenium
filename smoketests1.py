import unittest
from xmlrunner import xmlrunner

#from user_signup_login import TestAccount

from .user_signup_login import TestAccount
from .bookingsession import BookHandstand
from .bookingsession_groups import Book_small_group
from .city_classtype import city_classtypelinks
from .test1 import TestA
from .all_link import links
from .test2 import TestB
from .setting_screen_validation import settingscreen
from .apply_tobe_trainer import  TestTrainerAccount

# get all tests from SearchProductTest and HomePageTest class
test1 = unittest.TestLoader().loadTestsFromTestCase(TestA)
test2 = unittest.TestLoader().loadTestsFromTestCase(TestB)


# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([test1, test2])

# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)

