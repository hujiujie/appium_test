# coding=utf-8
import pytest

from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.homepage import Homepage


class PortfolioTestBase(object):
    @classmethod
    def setup_class(cls):
        Appium().initDriver()
        cls.homepage = Homepage()
        cls.stocks = cls.homepage.toPortfolio()