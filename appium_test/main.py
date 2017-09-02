# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import unittest
import xmlrunner

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class AppiumTests(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'Nexus 5X',
            'appPackage': 'com.android.contacts',
            'appActivity': 'activities.PeopleActivity'
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    
    def tearDown(self):
        self.driver.quit()

    def test_app_search_box(self):
        el3 = self.driver.find_element_by_id("com.android.contacts:id/menu_search")
        self.assertIsNotNone(el3)
        el3.click()

        el4 = self.driver.find_element_by_id("com.android.contacts:id/search_view")
        self.assertIsNotNone(el4)
        el4.send_keys("tes")

        #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "com.android.contacts:id/search_view")))
        el5 = self.driver.find_element_by_accessibility_id("テスト端末Eagle")
        self.assertIsNotNone(el5)
        el5.click()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    xmlrunner.XMLTestRunner().run(suite)
    #unittest.TextTestRunner(verbosity=2).run(suite)
