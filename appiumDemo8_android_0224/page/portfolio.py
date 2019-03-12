# coding=utf-8

# 进入自选
from selenium.webdriver.common.by import By

from appiumDemo8_android_0224.page.search import Search
from appiumDemo8_android_0224.page.base_page import BasePage


class Portfolio(BasePage):
    _search_button = (By.ID,"action_create_cube")

    def toSearch(self):
        self.find(self._search_button).click()
        return Search()



