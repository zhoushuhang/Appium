# coding: utf-8
from appium import webdriver
import time
import common


desired_caps = {
    'platformName': 'Android',  # 测试平台
    'deviceName': '127.0.0.1:62001',  # 手机设备名称，通过adb devices查看
    'platformVersion': '4.0',  # 安卓系统版本号
    'appPackage': 'com.cloudbae.lovenanning',  # apk包名
    'appActivity': 'com.cloudbae.lovenanning.login.view.WelComeActivity',  # apk的launcherActivity
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.wait_activity(".home.view.HomeActivity", 30)  # 智能等待指定页面出现，超时时间30秒
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
username = driver.find_element_by_id("com.cloudbae.lovenanning:id/tvUserName").text
print username
if username == u"测试":
    print(u"登陆成功！")
driver.find_element_by_id("com.cloudbae.lovenanning:id/menu_home").click()
time.sleep(5)
a = driver.find_element_by_id("com.cloudbae.lovenanning:id/search_bg").location.get("x")
b = driver.find_element_by_id("com.cloudbae.lovenanning:id/search_bg").location.get("y")
print a, b
c = driver.find_element_by_id("com.cloudbae.lovenanning:id/linearLayoutHomeApply3").location.get("x")
d = driver.find_element_by_id("com.cloudbae.lovenanning:id/linearLayoutHomeApply3").location.get("y")
print c, d
driver.swipe(c, d, a, b, 1000)

# driver.scroll("com.cloudbae.lovenanning:id/search_bg", "com.cloudbae.lovenanning:id/linearLayoutHomeApply3")
time.sleep(3)
common.logout(driver)
common.is_logout_success(driver)
