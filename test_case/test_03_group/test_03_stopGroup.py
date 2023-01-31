# coding=utf-8
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from base.base import Base
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod


@allure.feature("群功能")
class TestStopGroup:

    @allure.story('停用群模块')
    @allure.title('[case01] 停用群')
    @pytest.mark.flaky(reruns=1)
    def test_case01(self, start_app, reload_app):
        contact1 = PubMethod.get_csv_data(7)
        with allure.step('1、建群'):
            driver = start_app
            base = Base(driver)
            time.sleep(3)
            base.click_btn(locator=(By.XPATH, "//*[@resource-id='headerContainer']/android.view.ViewGroup/android.view.ViewGroup[3]"))
            base.click_btn(locator=(By.XPATH, "//*[@text='创建群']"))
            base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@text='搜索' and @class='android.widget.EditText']"), value=contact1[0])
            # 点击被添加联系人【勾选】按钮
            base.click_btn(locator=(By.XPATH, "//*[@text='取消']/../../../../android.widget.ScrollView/android.view.ViewGroup"))
            # 点击确定
            base.click_btn(locator=(By.XPATH, "//*[@text='确定']"))
        with allure.step('2、进入群设置》停用群'):
            base.click_btn(locator=(By.XPATH, "//*[@text='发送']/../../../android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"))
            # 滑动屏幕
            time.sleep(3)
            PubMethod.swipe_up(driver)
            base.click_btn(locator=(By.XPATH, "//*[@text='停用群']"))
            base.click_btn(locator=(By.XPATH, "//*[@text='确定']"))
            result = PubMethod.get_toast(driver, "//*[contains(@text, '您已成功停用')]", 10, 0.05)
            print("停用群的结果是：{}".format(result))
        with allure.step('3、验证实际结果是否正确'):
            AssertMethod.assert_true_screen_shot(driver, result)


if __name__ == "__main__":
    pytest.main(["test_03_stopGroup.py"])
