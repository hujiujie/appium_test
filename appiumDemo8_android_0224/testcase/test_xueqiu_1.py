# coding = utf-8
import pytest

from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.homepage import Homepage


class TestXueqiu:
    @pytest.fixture(scope="function", autouse=True)
    def init_base(self):
        Appium().initDriver()

    def test_search(self):
        # 链式调用
        assert Homepage().toSearch().search("pdd").get_stock() == "拼多多"

    def test_search_username(self):
        assert Homepage().toSearch().search("天长地久").getUserName() == "天长地久"

    # 添加股票到自选
    @pytest.mark.parametrize("stockName",["百度","阿里巴巴","拼多多","腾讯"])
    def test_add_stocks(self,stockName):
        Homepage().toSearch().search(stockName).add_stocks()
        assert stockName in Appium.getDriver().page_source




