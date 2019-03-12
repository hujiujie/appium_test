# coding = utf-8
'''
雪球首页
'''
from selenium.webdriver.common.by import By
from appiumDemo8_android_0224.page.search import Search
from appiumDemo8_android_0224.page.base_page import BasePage
from appiumDemo8_android_0224.page.stock import Stock

# 继承BasePage类
class Homepage(BasePage):
    _search = (By.ID,"home_search")
    _portfolio = (By.XPATH,"//*[@text='自选']")

    def __init__(self):
        self.loaded()

    def toSearch(self):
        # 雪球首页点击搜索
        self.find(self._search).click()
        # 点击事件后,进入新的页面, 所以下面返回一个新的对象(这个对象需要新定义)
        return Search()

    def toPortfolio(self):
        # 雪球首页点击自选
        self.find(self._portfolio).click()
        return Stock()

    # 动态页面，连续定位
    def loaded(self):
        locations = ["x", "y"]
        while locations[-1] != locations[-2]:
            element = self.find(self._portfolio)
            print(element)
            locations.append(element.location)
            print(locations)