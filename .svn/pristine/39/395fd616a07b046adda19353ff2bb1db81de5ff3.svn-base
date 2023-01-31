# coding=utf-8
import time
import allure
import pytest
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod


@allure.feature("登录")
class TestLogin:

    @allure.story('登录检查')
    @allure.title('[case01] 验证是否能登录成功')
    def test_login_case01(self, start_app, reload_app):
        with allure.step('1、启动app'):
            driver = start_app
            driver.implicitly_wait(5)
        with allure.step('2、开始登录'):
            if PubMethod.is_ele(driver, '//*[@text="登录"]') is False:
                PubMethod.check_permission_public(driver)
                PubMethod.log_out(driver)
            PubMethod.login(driver, 2)
            PubMethod.check_permission_public(driver)
            time.sleep(10)
            result1 = PubMethod.is_ele(driver, "//*[@text='未连接']")
            result2 = PubMethod.is_ele(driver, "//*[@text='搜索']")
        with allure.step('3、验证实际结果是否正确'):
            AssertMethod.assert_true_screen_shot(driver, (not result1) and result2)


if __name__ == "__main__":
    pytest.main(["test_login.py"])
