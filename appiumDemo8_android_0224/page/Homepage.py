# coding = utf-8
'''
雪球首页
'''
from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.Search import Search


class Homepage(object):

    def toSearch(self):
        # 雪球首页点击搜索
        Appium.getDriver().find_element_by_id("home_search").click()

        # 点击事件后,进入新的页面, 所以下面返回一个新的对象(这个对象需要新定义)
        return Search()