'''
姓名：Mr.Li
邮箱：1362141115@qq.com
'''

# -*-coding:UTF-8 -*-
from time import sleep
from selenium import webdriver

# 选择浏览器
def browser_selection (self,url):
    if self==1:
        driver = Chrome_path()
        url_selection(driver,url)
        return driver
    elif self==2:
        driver = webdriver.Edge()
        url_selection(driver,url)
        return driver
    else:
        print("浏览器选择错误，退出程序")
        exit()

#搜索关键词
def search (driver,url,search_terms):
    if url==1:
        baidu_search(driver,search_terms)
    else:
        JD_search(driver,search_terms)

# 因为不在默认位置，所以需要在代码中手动配置chrome位置，按照这样配置，之后才能完成对chrome的控制
def Chrome_path():
    options = webdriver.ChromeOptions()
    options.binary_location = r"D:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options=options)
    return driver

#网址选择
def url_selection(driver,url):
    if url == 1:
        driver.get("https://www.baidu.com/")
    elif url == 2:
        driver.get("https://www.jd.com/")
    else:
        print("网址选择错误，退出程序")
        exit()

#百度搜索
def baidu_search(driver,search_terms):
    driver.find_element_by_id("kw").send_keys(search_terms)
    driver.find_element_by_class_name("s_btn").click()
    sleep(2)
    driver.find_element_by_class_name("s-tab-item.s-tab-pic").click()  #点击图片
    browser_qiut(driver)

#京东搜索
def JD_search(driver,search_terms):
    driver.find_element_by_id("key").click()
    driver.find_element_by_id("key").send_keys(search_terms)
    sleep(2)
    driver.find_element_by_class_name("button").click()
    browser_qiut(driver)

#等待几秒钟之后退出浏览器
def browser_qiut(driver):
    sleep(10)
    driver.quit()


#主函数
if __name__ == '__main__':
    print("请输入1或2选择要打开的浏览器和网站：")
    self=int(input("1、Chrome浏览器  2、Edge浏览器（Edge驱动暂未找到相应版本）：  "))  #Edge驱动暂未找到
    url=int(input("1、百度搜索  2、京东搜索：  "))
    search_terms = input("请输入需要搜索的东西：  ")
    driver = browser_selection(self,url)   #用什么浏览器打开什么网址
    search(driver,url,search_terms)    #搜索关键字