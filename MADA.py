#!/usr/bin/python
# -*- coding: UTF -8 -*-
import os

import self
from appium import webdriver

desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = '24500698313679'
# 应用参数
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings$NetworkDashboardActivity'
desired_caps['noRest'] = 'true'
desired_caps['newCommandTimeout'] = '6000'
# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 定位一组元素CLASS为android:id/title的元素
#  driver.find_element_by_xpath("//*[@text = '网络和互联网']").click()
# 点击titles的第3个元素
# titles[2].click()
# 退出driver
driver.find_element_by_xpath("//*[@text='Advanced']").click()
driver.find_element_by_xpath("//*[@text='Private DNS']").click()

if self.driver.find_elements("//*[@text='Off']") == []:
  print("FAIL")
else:
  print("PASS")

print(driver.find_element_by_xpath("//*[@text='Off']"))
if driver.find_element_by_xpath("//*[@text='Off']") is True:
    if (driver.find_element_by_xpath("//*[@text='Automatic']") is True):
        if (driver.find_element_by_xpath("//*[@text='Private DNS provider hostname']") is True):
            tiaojian = driver.find_element_by_xpath("//*[@text='Automatic']").get_attribute("checked")
            if tiaojian == "true":
                print("当前选择为：Automatic,PASS")
            else:
                print("FAIL,默认没有选择Automatic")
        else:
            print("没有Private DNS provider hostname对象")
    else:
        print("没有Automatic对象")
else:
    print("没有Off对象")