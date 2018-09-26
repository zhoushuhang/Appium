# coding:utf-8
import time
import json
from appium import webdriver
# import common

# def changepage(driver):
desired_caps = {
        'platformName': 'Android',  # 测试平台
        'deviceName': '127.0.0.1:62001',  # 手机设备名称，通过adb devices查看
        'platformVersion': '4.0',  # 安卓系统版本号
        'appPackage': 'com.cloudbae.lovenanning',  # apk包名
        'appActivity': 'com.cloudbae.lovenanning.login.view.WelComeActivity',  # apk的launcherActivity
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
driver.find_element_by_id("com.cloudbae.lovenanning:id/menu_home").click()
time.sleep(5)
a = driver.find_element_by_id("com.cloudbae.lovenanning:id/search_bg").location.get("x")
b = driver.find_element_by_id("com.cloudbae.lovenanning:id/search_bg").location.get("y")
print a, b
c = driver.find_element_by_id("com.cloudbae.lovenanning:id/linearLayoutHomeApply3").location.get("x")
d = driver.find_element_by_id("com.cloudbae.lovenanning:id/linearLayoutHomeApply3").location.get("y")
print c, d
driver.swipe(c, d, a, b, 1000)
time.sleep(2)
driver.find_element_by_name(u"驾驶证电子信息").click()
time.sleep(3)
info = driver.find_elements_by_class_name("android.view.View")
print info
e = len(info)
print e
infoname = []
for i in range(0, e):
    infoname.append(info[i].get_attribute("name"))
result = json.dumps(infoname, encoding='UTF-8', ensure_ascii=False)  # 使用json进行格式转换，使输出显示为中文
print(result)
if u"*树杭" in result:
    print(u"驾驶证信息获取成功！")
else:
    print(u"驾驶证信息获取失败！")
print driver.contexts
contexts = driver.contexts
print contexts
# driver.switch_to.context(contexts[1])
# now = driver.current_context
# print now
# driver.switch_to.context(contexts[0])
# now = driver.current_context
# print now




