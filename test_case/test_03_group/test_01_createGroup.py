# coding=utf-8
import time
import allure
import pytest
from selenium.webdriver.common.by import By
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod
from base.base import Base


@allure.feature("群功能")
class TestCreateGroup:

    @allure.story('创建群模块')
    @allure.title('[case01] 创建群')
    @pytest.mark.flaky(reruns=1)
    def test_createGroup_case01(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        name = PubMethod.get_csv_data(4)
        nicheng = PubMethod.get_csv_data(5)
        result = True

        with allure.step("1、进入选择群成员界面"):
            time.sleep(3)
            base.click_btn(locator=(By.XPATH, "//*[@resource-id='headerContainer']/android.view.ViewGroup/android.view.ViewGroup[3]"))
            base.click_btn(locator=(By.XPATH, "//*[@text='创建群']"))
        with allure.step("2、搜索联系人并创建群"):
            for i in range(1, len(name)):
                base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
                base.send_key(locator=(By.XPATH, "//*[@text='取消']/../../android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText"), value=name[i])
                time.sleep(3)
                base.click_btn(locator=(By.XPATH, "//*[@text='取消']/../../../../android.widget.ScrollView/android.view.ViewGroup"))
            time.sleep(2)
            base.click_btn(locator=(By.XPATH, "//*[@text='确定']"))
        with allure.step("3、验证群是否创建成功"):
            time.sleep(8)
            for i in range(1, len(nicheng)):
                result = PubMethod.is_ele(driver, "//*[@text='您邀请"+nicheng[i]+"加入本群，新加入成员可查看历史消息']") and result
            AssertMethod.assert_true_screen_shot(driver, result)


if __name__ == "__main__":
    pytest.main(["test_01_createGroup.py"])






























