# coding = utf-8
import unittest
import pytest

from appiumDemo8_android_0224.driver.Appium import Appium
from appiumDemo8_android_0224.page import Search
from appiumDemo8_android_0224.page.Homepage import Homepage


class TestXueqiu1(unittest.TestCase):
    def setUp(self):
        print(Appium().initDriver())


    def test_search(self):
        homepage_r = Homepage()
        print(homepage_r)
        homepage_r.toSearch()
        search_r = Search.Search("拼多多")
        assert search_r.get_stock() == "拼多多"


