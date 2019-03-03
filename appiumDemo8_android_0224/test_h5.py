# coding=utf-8

import unittest


# H5页面 定位元素 触发事件自动化测试
# 打开一个网址 蛋卷基金，使用用户名+密码登录
from appium import webdriver


class TestH5(unittest.TestCase):
    def setUp(self):
        caps={}
        caps["platformName"] = "Android",
        caps["deviceName"]  = "GWY0217207001917",
        #caps["browserName"] = "Chrome",
        caps["browserName"] = "Browser",
        caps["noRest"] = "true",
        caps["fullRest"] = "false"
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implictitly_wait(1000)

    def test_main(self):
        # 打开一个网址
        self.driver.get("https://danjuanapp.com/my-money?channel=1300100158&refer=xq_trade").click()
        # 使用css定位  可以在谷歌浏览器中打开这个网址 右键检查 ，查看页面源代码
        self.driver.find_element_by_css_selector(".btns .blank").click()  #父类class 子类class ，两级定位
        self.driver.find_element_by_css_selector(".pass_switch").click()

        self.driver.find_element_by_id("telno").sendkeys("18810054187")
        self.driver.find_element_by_id("pass").sendkeys("666666")
        self.driver.find_element_by_id("text").click()
