# coding: utf-8
import time
from appium import webdriver


def login(username, password):
    desired_caps = {
        'platformName': 'Android',  # 测试平台
        'deviceName': '127.0.0.1:62001',  # 手机设备名称，通过adb devices查看
        'platformVersion': '4.0',  # 安卓系统版本号
        'appPackage': 'com.cloudbae.lovenanning',  # apk包名
        'appActivity': 'com.cloudbae.lovenanning.login.view.WelComeActivity',  # apk的launcherActivity
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    driver.wait_activity(".home.view.HomeActivity", 30)  # 智能等待指定页面出现Activity，超时时间30秒
    driver.find_element_by_id("com.cloudbae.lovenanning:id/menu_my").click()
    time.sleep(3)
    driver.find_element_by_id("com.cloudbae.lovenanning:id/tvUserGoLogin").click()
    time.sleep(2)
    # driver.find_element_by_class_name("android.widget.TextView").click()
    driver.find_element_by_name(u"账号密码登录").click()
    driver.find_element_by_id("com.cloudbae.lovenanning:id/etInputPhoneNum").send_keys(username)
    driver.find_element_by_id("com.cloudbae.lovenanning:id/etInputPwd").send_keys(password)
    driver.find_element_by_id("com.cloudbae.lovenanning:id/tvLogin").click()
    time.sleep(3)


def is_login_success(driver):
    username = driver.find_element_by_id("com.cloudbae.lovenanning:id/tvUserName").text
    print username
    if username == u"测试":
        print(u"登陆成功！")
    else:
        print(u"登录失败！")


def logout(driver):
    driver.find_element_by_id("com.cloudbae.lovenanning:id/menu_my").click()
    driver.find_element_by_class_name("android.widget.ImageView").click()
    time.sleep(0.5)
    driver.find_element_by_name(u"退出登录").click()
    time.sleep(0.5)


def is_logout_success(driver):
    buttonname = driver.find_element_by_id("com.cloudbae.lovenanning:id/tvUserGoLogin").text
    print buttonname
    if buttonname == u"登录":
        print(u"退出登录成功！")
    else:
        print(u"退出登录失败！")