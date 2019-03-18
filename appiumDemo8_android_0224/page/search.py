# coding = utf-8

'''
搜索
'''
from appium.webdriver.common.mobileby import MobileBy
from appiumDemo8_android_0224.page.base_page import BasePage


# 继承BasePage类
class Search(BasePage):
    _search = (MobileBy.ID, "search_input_text")
    _user = (MobileBy.XPATH, "//*[@text='用户']")
    _user_name = (MobileBy.ID, "user_name")
    _stockName = (MobileBy.ID, "stockName")

    _next_talk = (MobileBy.XPATH, "//*[@text='下次再说']")
    _follow = (MobileBy.ID, "com.xueqiu.android:id/follow_btn")
    _followed = (MobileBy.ID, "com.xueqiu.android:id/followed_btn")
    _cancel = (MobileBy.XPATH, "//*[@text='取消']")

    # 搜索股票
    def search(self, keyword):
        self.find(self._search).send_keys(keyword)
        # 搜索结果还是在当前页,所以返回自己即可
        return self

    def getUserName(self):
        self.find(self._user).click()
        self.find(self._user_name).text

    # 获取股票名称
    def get_stock(self):
        return self.find(self._stockName).text

    def cancel(self):
        self.find(self._cancel).click()

    def followFirst(self):
        elements = self.findAll(self._follow)
        if len(elements) > 0:
            elements[0].click()

        return self