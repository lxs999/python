#!/usr/bin/python
# -*- coding: UTF -8 -*-
import unittest
import time
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'V7LB14BB7LC000T'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.swipe(362, 1052, 334, 268, 500)
        self.driver.find_element_by_xpath("xpath=//*[@text='Settings']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Network & internet']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Advanced']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Private DNS']").click()
        attribute1 = self.driver.find_element_by_xpath("xpath=//*[@text='Automatic']").get_attribute("checked")
        print (attribute1)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
