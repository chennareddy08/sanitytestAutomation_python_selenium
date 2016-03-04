from multiprocessing import Process
import os,time,unittest
from booking_simulator import iosbooking

from xmlrunner import xmlrunner
def appiumserver():
    os.system("/Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/bin/appium.js --address 127.0.0.1 --chromedriver-port 9516 --bootstrap-port 4725 --no-reset --local-timezone --command-timeout 7200 --session-override --debug-log-spacing  --platform-version 9.0 --platform-name iOS --app Handstand.app  --show-ios-log --native-instruments-lib --orientation Portrait")

if __name__ == '__main__':
    Process(target=appiumserver).start()
    Process(target=iosbooking).start()


xmlrunner.XMLTestRunner(verbosity=2, output='test-reports')._make_result()
