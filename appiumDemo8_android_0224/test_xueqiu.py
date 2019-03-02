# coding = utf-8
import pytest
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu(unittest.TestCase):
    loaded = False

    def setUp(self):
        print("setup")
        caps = {"platformName": "Android",
                "deviceName": "demo",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "autoGrantPermissions": True,  # 权限弹窗关闭
                "unicodeKeyboard": True,  # 支持中文输入
                "resetKeyboard": True,  # 键盘恢复
                "automationName":"UiAutomator2"
                }

        if TestXueqiu.loaded == True:
            caps["noReset"] == "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)  # 隐式等待
        loaded = True

    # 方法封装 ,进入自选
    # 自选页面是动态加载的,所以要等待 连续定位直到位置不变
    def loaded_zixuan(self):
        locations = ["x", "y"]
        while locations[-1] != locations[-2]:
            element = self.driver.find_element_by_xpath(
                "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
            locations.append(element.location)
            print(locations)

        # self.driver.find_element_by_xpath(
        #   "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()

    # 作业1 0221-查看拼多多股票
    def test_select_stock(self):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys('pdd')
        self.driver.save_screenshot("screenhot/search_input_text.png")  # 截图 定义图片名称并保存在一个路径下
        self.driver.find_element_by_xpath("//*[@text='拼多多']").click()
        self.driver.save_screenshot("screenhot/pinduoduo_xiangqing.png")
        self.driver.implicitly_wait(2)
        self.driver.back()  # 返回上一页

    # 作业2 0221- 搜索拼多多股票 ,并把拼多多股票加入到自选股中
    def test_add_stock(self):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys('pdd')
        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            self.driver.find_element_by_id("follow_btn").click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()

    # 作业2  0221-验证自选股中是否有拼多多股票
    def test_check_stock(self):
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        assert 1 == len(self.driver.find_elements_by_xpath(
            "//*[@text='拼多多'] and contains(@resource-id, 'portfolio_stockName')"))

    # 作业1-0224
    # 进去自选，点击搜索，搜索alibaba，点击添加。然后回到自选，判断阿里巴巴已经在自选中，
    # 把测试用例代码贴到回复里。测试用例的名字 test_search_add
    def test_search_add(self):

        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()

        self.driver.find_element_by_id('action_create_cube').click()
        self.driver.find_element_by_id('search_input_text').send_keys('alibaba')

        if len(self.driver.find_element_by_id('follow_btn')) > 0:
            self.driver.find_element_by_id('follow_btn').click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
        self.driver.find_element_by_id('action_close').click()

        assert 1 == len(self.driver.find_elements_by_xpath("//*[@text='阿里巴巴']"))

    # 作业2 0224
    # 进去自选，点击搜索，搜索“阿里巴巴”，点击添加，判断添加按钮自动变化状态 test_alibaba_search
    # 进入自选，判断阿里巴巴存在，不要使用xpath定位判断阿里巴巴股票存在 test_alibaba_exist
    def test_alibaba_search(self):
        # 自选页面是动态加载的,所以要等待 连续定位直到位置不变
        location = []
        for i in range(1, 5):
            element = self.driver.find_element_by_xpath(
                "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
            location.append(element.location)
            # print(location)
            if len(location) > 1:
                if location[-1] == location[-2]:
                    break

        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_id('action_create_cube').click()
        self.driver.find_element_by_id('search_input_text').send_keys('阿里巴巴')

        # 通过先定位父级元素 在找子元素
        button_before = self.driver.find_element_by_id("add_attention"). \
            find_element_by_class_name("android.widget.TextView").get_attribute("resourceId")

        if button_before == 'com.xueqiu.android:id/follow_btn':
            self.driver.find_element_by_id('follow_btn').click()
            button_after = self.driver.find_element_by_id('add_attention'). \
                find_element_by_class_name("android.widget.TextView").get_attribute('resourceId')
            assert button_before != button_after

    # 进入自选，判断阿里巴巴存在，不要使用xpath定位判断阿里巴巴股票存在 test_alibaba_exist
    def test_alibaba_exist(self):
        location = []
        for i in range(1, 5):
            element = self.driver.find_element_by_xpath(
                "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
            location.append(element.location)
            if len(location) > 1:
                if location[-1] == location[-2]:
                    break

        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()

        assert 1 == len(self.driver.find_elements_by_xpath(
            "//*[@text='阿里巴巴' and contains(@resource-id, 'portfolio_stockName')]"))

    # 作业3 0224
    # 添加一只美股，判断是否添加成功 test_add_us
    # 然后删除一只美股，判断删除成功 test_delete_us
    # 利用参数化或者数据驱动添加30只股票 test_add_batch

    def test_add_us(self):
        self.loaded_zixuan()
        self.driver.find_element_by_xpath("//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_xpath("//*[@text='美股']").click()
        if len(self.driver.find_elements_by_id("add_to_portfolio_stock")) > 0:
            self.driver.find_element_by_xpath(
                "//*[@selected='true' and contains(@resource-id, 'recommend_select_two')]").click()
            self.driver.find_element_by_xpath(
                "//*[@selected='true' and contains(@resource-id, 'recommend_select_three')]").click()
            self.driver.find_element_by_xpath(
                "//*[@selected='true' and contains(@resource-id, 'recommend_select_four')]").click()
            self.driver.find_element_by_xpath(
                "//*[@selected='true' and contains(@resource-id, 'recommend_select_five')]").click()
            self.driver.find_element_by_xpath(
                "//*[@selected='true' and contains(@resource-id, 'recommend_select_six')]").click()

            self.driver.find_element_by_id("add_to_portfolio_stock").click()

        assert 1 == len(self.driver.find_elements_by_id("portfolio_stockName"))

        # test_delete_us
        #  定位到元素,长按 点击删除

        element = self.driver.find_element_by_id("portfolio_stockName")
        TouchAction(self.driver).long_press(element, None, None, 10000).perform()

        self.driver.find_element_by_xpath("//*[@text='删除' and contains(@resource-id, 'md_title')]").click()

        assert 1 == len(self.driver.find_elements_by_id("add_to_portfolio_stock"))

    # 添加10只美股，当全部股票大于2页的时候断言某个股票同时存在于“美股”与“全部”分类中 test_exist_in_all
    def test_exist_in_all(self):
        # 每股 :特斯拉 苹果 汽车之家 百度 谷歌C  陌陌  优信 阿里巴巴 聚美优品  拼多多
        self.load_zixuan()
        self.driver.find_element_by_xpath("//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_xpath("//*[@text='美股']").click()
        if len(self.driver.find_elements_by_id("add_to_portfolio_stock")) > 0:
            self.driver.find_element_by_id("add_to_portfolio_stock").click()

    def test_mobile(self):
        # self.driver.start_activity("com.android.calculator2",".Calculator")
        # self.driver.install_app("E:/apk/com.bussinesscloud.apk")
        print(self.driver.is_locked())  # 先判断是否锁屏 ，然后锁屏5秒，然后解锁
        self.driver.lock(5)
        self.driver.unlock()

    def test_main_swipe(self):
        self.loaded_zixuan()
        for i in range(10):
            # duration表示滑动一次等待1000毫秒    注意打开手机开发者模式-指针位置，可以看看 x轴 y轴的值
            # x轴不变，y轴 变小，表示向上滑动
            self.driver.swipe(start_x=500, start_y=1000, end_x=500, end_y=600, duration=1000)

        for i in range(5):
        #左右滑动
            self.driver.swipe(start_x=800, start_y=1200, end_x=200, end_y=1200, duration=1000)

    def test_battery(self):
        print(self.driver.execute_script("mobile:batteryInfo"))  # 打印耗电量

    def test_shell(self):
        self.driver.execute_script("mobile:shell",{"command": "am", "args": ["start", "-n", "com.android.calculator2/.Calculator"]})


    def tearDown(self):
        print("teardown")
        self.driver.quit()
