# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.portfolio import Portfolio
from appiumDemo8_android_0224.page.stock_group import StockGroup


class Stock(Portfolio):
    _stock_name = (By.ID, "portfolio_stockName")
    _us = (By.XPATH, "//*[@text='美股']")
    _all = (By.XPATH, "//*[@text='全部']")

    _edit_group = (MobileBy.ID, "edit_group")
    _m_group = (MobileBy.XPATH, "//*[@text='管理分组']")

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

    def getNameByGroup(self, name):
        pass

    # 进入美股 ，长按删除股票
    def delete(self, name, group_name=""):
        if group_name != "":
            self.find((By.XPATH, self.byAttribute(text=group_name))).click()

        element = self.find((MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiSelector().resourceId("com.xueqiu.android:id/portfolio_stockName").text("' + name + '")'))
        TouchAction(Appium.getDriver()).long_press(el=element).perform()
        self.find((By.XPATH, self.byAttribute(text='删除'))).click()

    # 自选页面 点击分组 ，返回对象到管理分组页面
    def toGroup(self):
        self.find(self._edit_group).click()
        self.find(self._m_group).click()
        return StockGroup()
