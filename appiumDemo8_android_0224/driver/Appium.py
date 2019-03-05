# coding=utf-8
from appium import webdriver


class Appium(object):
    driver = None

    @classmethod
    def getDriver(cls):
        return cls.driver

    @classmethod
    def initDriver(cls):
        caps = {"platformName": "Android",
                "deviceName": "GWY0217207001917",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "autoGrantPermissions": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True,
                }

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

