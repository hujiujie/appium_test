# coding=utf-8
from selenium.webdriver.common.by import By

from appiumDemo8_android_0224.page.portfolio import Portfolio


class Stock(Portfolio):
    _stock_name = (By.ID,"portfolio_stockName")
    #_us = (By.XPATH,"//*[@text='美股']")
    _us = (By.XPATH, "//*[@text='美股' and contains(@resource-id, 'text')]")
    _all = (By.XPATH,"//*[@text='全部']")

    # 获取美股列表
    def getNameByUS(self):
        self.find(self._us).click()
        x = []
        for e in self.findAll(self._stock_name):
            x.append(e.text)
        return x

    # 获取全部列表
    def getNameByAll(self):
        self.find(self._all).click()
        x = []
        for e in self.findAll(self._stock_name):
            x.append(e.text)
        return x

    def getNameByGroup(self,name):
        pass