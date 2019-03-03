from appium import webdriver
import pytest


class TestXueQiu:

    @pytest.fixture(scope="function", autouse=True)  # 如果scope设置为class，则需要return driver 并将base作为参数传入后续用例调用
    def init_base(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",
                                       {"platformName": "android",
                                        "deviceName": "demo",
                                        "appPackage": "com.xueqiu.android",
                                        "appActivity": ".view.WelcomeActivityAlias",
                                        "unicodeKeyboard": True,
                                        "resetKeyboard": True,
                                        "autoGrantPermissions": True,
                                        })
        self.driver.implicitly_wait(20)
        yield
        self.driver.quit()

    # 方法封装 ,进入自选
    # 自选页面是动态加载的,所以要等待 连续定位直到位置不变
    def loaded_zixuan(self):
        locations = ["x", "y"]
        while locations[-1] != locations[-2]:
            element = self.driver.find_element_by_xpath(
                "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
            locations.append(element.location)
            print(locations)

    # 参数化  添加10支股票
    @pytest.mark.parametrize("stock_name", [
        "特斯拉", "阿里巴巴", "腾讯", "美团", "今日头条",
        "拼多多", "饿了么", "京东", "滴滴出行", "百度",
    ])
    def test_add_batch(self, stock_name):
        self.loaded_zixuan()
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_id('action_create_cube').click()
        self.driver.find_element_by_id('search_input_text').send_keys(stock_name)
        self.driver.find_element_by_id('follow_btn').click()
        self.driver.find_element_by_xpath("//*[@text='下次再说']").click()

    # 当全部股票大于2页的时候断言某个股票同时存在于“美股”与“全部”分类中
    def test_exist_in_all(self):
        self.loaded_zixuan()
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_xpath("//*[@text='美股']").click()
        meigu_tsl = self.driver.find_element_by_xpath("//*[@text='百度']")

        self.driver.find_element_by_xpath("//*[@text='全部']").click()
        quanbu_tsl = self.driver.find_element_by_xpath("//*[@text='百度']")

        assert meigu_tsl and quanbu_tsl

