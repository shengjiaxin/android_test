# coding=utf-8
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from base.base import Base
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod


@allure.feature("工作台")
class TestExpress:

    @allure.story('快递')
    @allure.title('[case01] 检查账号有快递的情况')
    @pytest.mark.flaky(reruns=1)
    def test_case01(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        with allure.step('1、进入工作台快递模块'):
            time.sleep(3)
            base.click_btn(locator=(By.XPATH, "//android.widget.Button[@content-desc='工作台, tab, 2 of 4']"))
            base.click_btn(locator=(By.XPATH, "//*[@text='快递']"))
            time.sleep(6)
            result = PubMethod.is_ele(driver, "//*[contains(@text,'手动输入码')]")
            print("有快递结果是：{}".format(result))
        with allure.step("2、验证当前有快递"):
            AssertMethod.assert_true_screen_shot(driver, result)


if __name__ == "__main__":
    pytest.main(["test_02_express.py"])
