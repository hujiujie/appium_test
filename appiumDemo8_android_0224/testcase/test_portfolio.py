# coding=utf-8

import pytest

from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.homepage import Homepage
from appiumDemo8_android_0224.testcase.PortfolioTestBase import PortfolioTestBase


class TestPortfolio(PortfolioTestBase):

    def test_list(self):
        # 打印美股股票列表
        print(self.stocks.getNameByUS())

    def test_add(self):
        # 添加一支股票
        self.stocks.toSearch().search("pdd").followFirst().cancel()
        assert "拼多多" in self.stocks.getNameByUS()

    def test_delete(self):
        # 删除美股中的一个股票，并断言它不在美股列表中
        self.stocks.delete("拼多多","美股")
        assert "拼多多" not in self.stocks.getNameByUS()

    def test_delete_us(self):
        # 删除所有的美股
        stocks= self.stocks.getNameByUS()
        for i in range(len(stocks)):
            self.stocks.delete(stocks[i],"美股")
            assert stocks[i] not in self.stocks.getNameByUS()


    def test_delete_all(self):
        # 删除全部股票
        stocks = []
        while True:
            stocks = self.stocks.getNameByAll()
            if len(stocks)==0:
                break
            stock= stocks[0]
            self.stocks.delete(stock)

        assert len(self.stocks.getNameByAll())== 0







