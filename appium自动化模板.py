#!/usr/bin/python
# -*- coding: UTF -8 -*-
import os
import time
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
driver.find_element_by_xpath("//*[@text='高级']").click()
driver.find_element_by_xpath("//*[@text='私人 DNS']").click()
tiaojian = driver.find_element_by_xpath("//*[@text='自动']").get_attribute("checked")
if tiaojian == "true":
    print("当前选择为：Automatic")
else:
    print("fail")