# coding=utf-8
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from base.base import Base
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod


@allure.feature("聊天记录")
class TestRecord:

    @allure.story('查找聊天记录功能')
    @allure.title('[case01] 查找聊天记录')
    @pytest.mark.flaky(reruns=1)
    def test_case01(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        contact = PubMethod.get_csv_data(4)

        with allure.step('1、搜素联系人'):
            time.sleep(3)
            base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact[1])
            base.click_btn(locator=(By.XPATH, "//*[@text='联系人']/../../android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]"))
            result = PubMethod.is_ele(driver, "//*[@text='发送']")
        with allure.step('2、验证是否进入聊天页'):
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step('3、聊天窗口发消息并查找记录'):
            text = PubMethod.get_str()
            # 发送随机字符串
            base.send_key(locator=(By.XPATH, "//*[@text='发送']/../../android.widget.EditText"), value=text)
            base.click_btn(locator=(By.XPATH, '//*[@text="发送"]'))
            for i in range(1, 15):
                base.send_key(locator=(By.XPATH, "//*[@text='发送']/../../../android.widget.EditText"), value=i)
                time.sleep(1)
                base.click_btn(locator=(By.XPATH, '//*[@text="发送"]'))
            # 点击进入聊天设置页
            base.click_btn(locator=(By.XPATH, "//*[@text='发送']/../../../../android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]"))
            base.click_btn(locator=(By.XPATH, "//*[@text='查找聊天记录']"))
            # 输入框输入查找到消息
            base.send_key(locator=(By.XPATH, "//*[@text='搜索' and @class='android.widget.EditText']"), value=text)
            result = PubMethod.is_ele(driver, "//android.widget.TextView[@text='" + text + "']")
            print("查找聊天记录结果是：{}".format(result))
        with allure.step("4、验证是否查找到对应消息"):
            AssertMethod.assert_true_screen_shot(driver, result)
            # 点击消息内容进入聊天页
            base.click_btn(locator=(By.XPATH, "//android.widget.TextView[@text='" + text + "']"))
            base.click_btn(locator=(By.XPATH, "//android.widget.TextView[@text='" + text + "']"))
            time.sleep(2)
            result = PubMethod.is_ele(driver, "//*[@text='" + text + "']")
        with allure.step("5、验证是否查跳转到聊天页对应消息"):
            AssertMethod.assert_true_screen_shot(driver, result)


if __name__ == "__main__":
    pytest.main(["test_01_findRecord.py"])
