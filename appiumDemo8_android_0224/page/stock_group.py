# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from appiumDemo8_android_0224.page.portfolio import Portfolio


class StockGroup(Portfolio):
    _add_item = (MobileBy.ID, "add_item")
    _input_text = (MobileBy.ID, "dialog_input_text")
    _commit = (MobileBy.XPATH, "//*[@text='确认']")
    _group_name = (MobileBy.ID, "group_edit_text")
    _group_opt = (MobileBy.ID, "group_opt")
    _ok = (MobileBy.XPATH, "//*[@text='确定']")

    # 添加分组
    def add(self, group_name):
        self.find(self._add_item).click()
        self.find(self._input_text).send_keys(group_name)
        self.find(self._commit).click()
        return self

    # 删除分组
    def delete(self):

        elements = self.findAll(self._group_opt)
        if len(elements)>0:
            print("ifififif")
            print(elements)
            # 删除最后一个自定义分组名称
            elements[-1].click()
            self.find(self._ok).click()
        return self

    # 获取所有分组名称
    def getGroups(self):
        x = []
        for e in self.findAll(self._group_name):
            x.append(e.text)
        return x

    # 在分组下搜索股票-添加股票
    def add_stock(self):
        pass

    def delete_stock(self):
        pass

