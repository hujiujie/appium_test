# coding=utf-8

import pytest
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class Appium(object):


    loaded = False

    def setUp(self):
        print("setup")
        caps = {"platformName": "Android",
                "deviceName": "GWY0217207001917",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "autoGrantPermissions": True,  # 权限弹窗关闭
                "unicodeKeyboard": True,  # 支持中文输入
                "resetKeyboard": True,  # 键盘恢复
                "automationName": "UiAutomator2"
                }

        if Appium.loaded == True:
            caps["noReset"] == "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)  # 隐式等待
        loaded = True
