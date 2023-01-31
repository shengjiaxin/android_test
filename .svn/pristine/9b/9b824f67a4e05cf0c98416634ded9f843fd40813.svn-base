# coding=utf-8
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from base.base import Base
from Common.publicMethod import PubMethod
from Common.read_csv import ReadCsvData
from base.assertMethod import AssertMethod


@allure.feature("工作台")
class TestCollect:
    csv_data = ReadCsvData()

    @allure.story('消息收藏')
    @allure.title('[case01] 消息收藏并查看')
    @pytest.mark.flaky(reruns=1)
    def test_case01(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        contact = PubMethod.get_csv_data(4)
        date = PubMethod.get_dateByMS()

        with allure.step('1、进入收藏列表，查看初始化收藏数据'):
            time.sleep(5)
            base.click_btn(locator=(By.XPATH, "//android.widget.Button[@content-desc='工作台, tab, 2 of 4']"))
            base.click_btn(locator=(By.XPATH, "//*[@text ='收藏']"))
            time.sleep(3)
            result = PubMethod.is_ele(driver, "//*[@text='暂无相关收藏']")
            print("查看初始化的结果是：{}".format(not result))
            AssertMethod.assert_false_screen_shot(driver, result)
        with allure.step('2、搜素联系人'):
            base.click_btn(locator=(By.XPATH, "//*[@text='我的收藏']/../android.view.ViewGroup"))
            base.click_btn(locator=(By.XPATH, '//android.widget.Button[@content-desc="会话, tab, 1 of 4"]'))
            base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact[1])
            base.click_btn(locator=(By.XPATH, "//*[@text='联系人']/../../android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]"))
            result = PubMethod.is_ele(driver, "//*[@text='发送']")
            print("进入聊天页的结果是：{}".format(result))
        with allure.step('3、验证是否进入聊天页'):
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step("4、发文本消息长按收藏"):
            base.send_key(locator=(By.XPATH, "//*[@text='发送']/../../android.widget.EditText"), value=date)
            base.click_btn(locator=(By.XPATH, '//*[@text="发送"]'))
            result = PubMethod.is_ele(driver, "//*[@text='" + date + "']")
            print("找到时间消息{}".format(result))
            base.long_press(locator=(By.XPATH, "//*[@text='" + date + "']"), time=2000)
            base.click_btn(locator=(By.XPATH, "//*[contains(@text,'收藏')]"))
            result = PubMethod.get_toast(driver, "//*[contains(@text, '已收藏')]")
            print("收藏的结果是：{}".format(result))
        with allure.step("5、验证是否收藏成功"):
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step("6、收藏列表查看消息"):
            # 点击返回会话列表
            base.click_btn(locator=(By.XPATH, "//*[@text='发送']/../../../../android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]"))
            base.click_btn(locator=(By.XPATH, "//*[@text='取消']"))
            base.click_btn(locator=(By.XPATH, "//android.widget.Button[@content-desc='工作台, tab, 2 of 4']"))
            base.click_btn(locator=(By.XPATH, "//*[@text ='收藏']"))
            time.sleep(3)
            result = PubMethod.is_ele(driver, "//*[@text='" + date + "']")
            print("查看收藏的结果是：{}".format(result))
        with allure.step("7、验证是否查看到收藏的消息"):
            AssertMethod.assert_true_screen_shot(driver, result)


if __name__ == "__main__":
    pytest.main(["test_01_msgCollect.py"])
