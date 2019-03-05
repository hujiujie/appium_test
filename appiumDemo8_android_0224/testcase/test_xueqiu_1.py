# coding = utf-8
import unittest
import pytest

from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page.Homepage import Homepage
from appiumDemo8_android_0224.page.Search import Search


class TestXueqiu1(unittest.TestCase):
    def setUp(self):
        print(Appium().initDriver())


    def test_search(self):
        Homepage().toSearch()
        search_r = Search()
        search_r.search("特斯拉")
        assert search_r.get_stock() == ("特斯拉")


