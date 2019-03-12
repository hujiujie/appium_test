# coding=utf-8

import pytest

from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.homepage import Homepage


class TestPortfolio:
    @pytest.fixture(scope="function", autouse=True)
    def init_base(self):
        Appium().initDriver()
        self.homepage = Homepage()
        self.stocks = self.homepage.toPortfolio()

    def test_stocks_list(self):
        print(self.stocks.getNameByUS())

    def test_stocks_add(self):
        self.stocks.toSearch().search("特斯拉").followFrist().cancel()
        assert "特斯拉" in self.stocks.getNameByUS()
