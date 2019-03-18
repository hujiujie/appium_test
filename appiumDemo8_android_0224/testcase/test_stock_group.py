# coding=utf-8
import pytest

from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.homepage import Homepage
from appiumDemo8_android_0224.testcase.StockGroupTestBase import StockGroupTestBase


class TestStockGroup(StockGroupTestBase):

    # 添加多个分组名称，并断言分组名称在列表里
    @pytest.mark.parametrize("name",["1","demo","中文名","空 格",])
    def test_add_group(self,name):
        if name not in self.group.getGroups():
            self.group.add(name)
        assert name in self.group.getGroups()


    # 删除分组，并断言：删除前分组名称的数量大于删除后的
    def test_delete_group(self):
        before = len(self.group.getGroups())
        self.group.delete()
        assert before >= len(self.group.getGroups())

    # 在指定分组下添加股票
    def test_add_stock(self):
        pass


    def test_delete_stock(self):
        pass

