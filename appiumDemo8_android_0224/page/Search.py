# coding = utf-8

'''
搜索
'''
from appiumDemo8_android_0224.driver.Appium import Appium


class Search(object):
    # 搜索股票
    def search(self,keyword):
        Appium.getDriver().find_element_by_id("search_input_text").send_keys(keyword)
        # 搜索结果还是在当前页,所以返回自己即可
        return self
    # 获取股票名称
    def get_stock(self):
        stock_name = Appium.getDriver().find_element_by_id("stockName").text
        return stock_name