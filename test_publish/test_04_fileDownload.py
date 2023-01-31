# coding=utf-8
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from base.base import Base
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod


@allure.feature("群功能")
class TestGroup:

    @allure.story('群文件下载')
    @allure.title('[case01] 群文件下载')
    def test_case01(self, start_app, reload_app):
        contact = PubMethod.get_csv_data(6)

        with allure.step('1、搜素群'):
            driver = start_app
            base = Base(driver)
            time.sleep(5)
            base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact[0])
            time.sleep(3)
            base.click_btn(locator=(By.XPATH, "//*[@text='群']/../following-sibling::android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"))
            result = PubMethod.is_ele(driver, "//*[@text='发送']")
            print("进入群聊页的结果是：{}".format(result))
        with allure.step('2、验证是否进入群聊天页'):
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step('3、进入群设置页，下载群文件'):
            base.click_btn(locator=(By.XPATH, "//*[@text='发送']/../../../android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView"))
            base.click_btn(locator=(By.XPATH, "//*[@text='群文件']"))
            time.sleep(3)
            ele = PubMethod.is_ele(driver, "//*[contains(@text,'暂时没有')]")
            print("不存在群文件结果是：{}".format(ele))
        with allure.step('4、验证是否存在群文件'):
            AssertMethod.assert_false_screen_shot(driver, ele)
            base.click_btn(locator=(By.XPATH, "//android.widget.TextView[@text='focustalk.apk']"))
            base.click_btn(locator=(By.XPATH, "//android.widget.TextView[@text='focustalk.apk']"))
            result = PubMethod.is_ele(driver, "//*[contains(@text,'正在下载')]")
            print("文件正在下载的结果是：{}".format(result))
            time.sleep(10)
            result1 = PubMethod.is_ele(driver, "//android.widget.TextView[@text='用其他应用打开']")
        with allure.step('5、验证文件是否下载成功'):
            AssertMethod.assert_true_screen_shot(driver, result1)


if __name__ == "__main__":
    pytest.main(["test_04_fileDownload.py"])