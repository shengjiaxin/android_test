# coding=utf-8
import time
import allure
import pytest
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod
from base.base import Base


@allure.feature("登录")
class Test_Reconnect:

    @allure.story('杀进程重连')
    @allure.title('[case01] 验证是否重连成功')
    def test_reconnect_case01(self, start_app, reload_app):
        with allure.step('1、启动app'):
            driver = start_app
            base = Base(driver)
            # 登录判断
            if PubMethod.is_ele(driver, '//*[@text="登录"]'):
                PubMethod.login(driver, 2)
        with allure.step('2、杀进程'):
            time.sleep(5)
            base.kill_app()
            time.sleep(3)
        with allure.step('3、重连'):
            base.restart_app()
            driver.implicitly_wait(20)
            result = PubMethod.is_ele(driver, ".//*[@text='未连接']")
            print("重连的结果是：{}".format(not result))
        with allure.step('4、重连是否正确'):
            AssertMethod.assert_false_screen_shot(driver, result)


if __name__ == "__main__":
    pytest.main(["test_reconnect.py"])
