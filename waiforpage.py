# coding: utf-8
from appium import webdriver
import time


desired_caps = {
    'platformName': 'Android',  # 测试平台
    'deviceName': '127.0.0.1:62001',  # 手机设备名称，通过adb devices查看
    'platformVersion': '4.0',  # 安卓系统版本号
    'appPackage': 'com.cloudbae.lovenanning',  # apk包名
    'appActivity': 'com.cloudbae.lovenanning.login.view.WelComeActivity',  # apk的launcherActivity
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(10)
ac = driver.current_activity  # APP完全启动后，获取当前页面的activity，用于登录，节省等待时间
print ac