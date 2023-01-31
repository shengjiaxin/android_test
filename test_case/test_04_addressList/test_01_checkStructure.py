# coding=utf-8
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from base.base import Base
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod


@allure.feature("通讯录")
class TestStructure:

    @allure.story('组织架构模块')
    @allure.title('[case01] 检查组织架构')
    @pytest.mark.flaky(reruns=1)
    def test_case01(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        contact = PubMethod.get_csv_data(4)

        with allure.step("1、进入通讯录》组织架构"):
            time.sleep(5)
            base.click_btn(locator=(By.XPATH, '//android.widget.Button[@content-desc="通讯录, tab, 3 of 4"]'))
            base.click_btn(locator=(By.XPATH, "//*[@text ='组织架构']"))
        with allure.step("2、验证是否进入应用开发部tab"):
            time.sleep(3)
            result = PubMethod.is_ele(driver, "//*[@text='应用开发部']")
            print("进入组织架构的结果是：{}".format(result))
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step("3、验证是否找到联系人"):
            result = PubMethod.is_ele(driver, "//*[contains(@text,'" + contact[0] + "')]")
            print("应用开发部tab下查找联系人结果是：{}".format(result))
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step("4、检查顶部导航栏是否能点"):
            base.click_btn(locator=(By.XPATH, "//*[@text ='研发中心']"))
            PubMethod.swipe_up(driver)
            result = PubMethod.is_ele(driver, "//*[contains(@text,'应用开发部')]")
            print("研发中心tab下查找部门结果是：{}".format(result))
        with allure.step("5、验证是否进入研发中心tab"):
            AssertMethod.assert_true_screen_shot(driver, result)


if __name__ == "__main__":
    pytest.main(["test_01_checkStructure.py"])
