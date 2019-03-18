# coding=utf-8
from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.homepage import Homepage


class StockGroupTestBase(object):

    @classmethod
    def setup_class(cls):
        Appium().initDriver()
        cls.homepage = Homepage()
        cls.group = cls.homepage.toPortfolio().toGroup()
