# coding=utf-8


from appium.webdriver import WebElement
from lxml import etree
from selenium.webdriver.common.by import By

from appiumDemo8_android_0224.driver.Appium import Appium


class BasePage(object):
    def __init__(self):
        pass

    @classmethod
    def byAttribute(self, text=None, id=None):
        text_selector=""

        if(text!=None):
            text_selector="@text='" + text + "'"
        if (id != None):
            id_selector = "contains(@resource-id, '" + id + "')"
            #return 'new UiSelector().resourceId("' + id + '").text("' + text + '")'
            return "//*[" + text_selector + " and " + id_selector + "]"
        else:
            #return 'new UiSelector().text("'+text+'")'
            return "//*[" + text_selector + "]"


    def findBy(self, by=By.ID, value=None):
        try:
            return Appium.getDriver().find_element(by, value)
        except:
            print("yichang")
            self.exception_handle()
            return Appium.getDriver().find_element(by, value)

    def find(self, locate) -> WebElement:
        return self.findBy(*locate)

    def findAll(self, locate) -> []:
        return Appium.getDriver().find_elements(*locate)

    def exception_handle(self):
        self.black_words = [self.byAttribute(text="好的"), self.byAttribute(text="下次再说")]

        for w in self.black_words:
            elements = Appium.getDriver().find_elements(By.XPATH, w)
            if len(elements) > 0:
                elements[0].click()
                return Appium.getDriver().find_element(By.XPATH, w)


    def exception_handle2(self):
        self.black_words = [self.byAttribute(text="好的"), self.byAttribute(text="下次再说")]

        #todo: 优化弹框处理逻辑，发现toast，自动发现兼容性问题等。。。
        page_source=Appium.getDriver().page_source
        print(page_source)
        #parser = etree.XMLParser(encoding='utf-8')
        xml=etree.XML(str(page_source).encode("utf-8"))
        print("clicktest1")
        for w in self.black_words:
            print(w)
            print("clicktest2")
            if(len(xml.xpath(w))>0):
                Appium.getDriver().find_element(By.XPATH, w).click()
            print("clicktest333333")
