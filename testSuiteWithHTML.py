__author__ = 'Chennareddy'
import unittest
from . import HTMLTestRunner
import os
from .test1 import TestA
from .test2 import TestB
dir = os.getcwd()
tests1 = unittest.TestLoader().loadTestsFromTestCase(TestA)
tests2 = unittest.TestLoader().loadTestsFromTestCase(TestB)
all_tests = unittest.TestSuite([tests1,tests2])

outfile = open(dir+"/Reports/TestReport.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       verbosity=1,
                                       title="Selenium Test Report",
                                       description="Testing Web Project 1")
runner.run(all_tests)
#unittest.TextTestRunner(verbosity=2).run(all_tests)
