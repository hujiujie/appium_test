# coding=utf-8
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Appium(object):

    driver: WebDriver = None

    @classmethod
    def getDriver(cls):
        return cls.driver

    @classmethod
    def initDriver(cls):
        caps = {"platformName": "Android",
                "deviceName": "demo",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "autoGrantPermissions": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True,
                }

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
