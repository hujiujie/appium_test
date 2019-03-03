# coding=utf-8
import pytest
import unittest
from appium import webdriver

class TestApiDemo(unittest.TestCase):
    def setUp(self):
        caps = {"platformName": "Android",
                "deviceName": "demo",
                "appPackage": "com.example.android.apis",
                "appActivity": ".ApiDemos",
                "autoGrantPermissions": True,  # 权限弹窗关闭
                "unicodeKeyboard": True,  # 支持中文输入
                "resetKeyboard": True,  # 键盘恢复
                "automationName": "UiAutomator2"
                }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_webdriver(self):
        print()

    def tearDown(self):
        self.driver.quit()