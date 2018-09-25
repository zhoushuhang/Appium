# coding: utf-8
from appium import webdriver
import time


desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '4.0',
    'appPackage': 'com.cloudbae.lovenanning',
    'appActivity': 'com.cloudbae.lovenanning.login.view.WelComeActivity',
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(10)
driver.find_element_by_id("com.cloudbae.lovenanning:id/menu_my").click()
time.sleep(3)
driver.find_element_by_id("com.cloudbae.lovenanning:id/tvUserGoLogin").click()
time.sleep(2)
# driver.find_element_by_class_name("android.widget.TextView").click()
driver.find_element_by_name(u"账号密码登录").click()
driver.find_element_by_id("com.cloudbae.lovenanning:id/etInputPhoneNum").send_keys("17607885072")
driver.find_element_by_id("com.cloudbae.lovenanning:id/etInputPwd").send_keys("hang0502")
driver.find_element_by_id("com.cloudbae.lovenanning:id/tvLogin").click()
time.sleep(3)
