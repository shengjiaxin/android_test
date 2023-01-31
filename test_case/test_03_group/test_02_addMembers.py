# coding=utf-8
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from base.base import Base
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod


@allure.feature("群功能")
class TestAddMembers:

    @allure.story('添加群成员模块')
    @allure.title('[case01] 添加群成员')
    @pytest.mark.flaky(reruns=1)
    def test_case01(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        contact1 = PubMethod.get_csv_data(7)
        contact2 = PubMethod.get_csv_data(6)

        with allure.step('1、搜素群'):
            time.sleep(3)
            base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact2[0])
            time.sleep(3)
            base.click_btn(locator=(By.XPATH, "//*[@text='群']/../following-sibling::android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"))
            result = PubMethod.is_ele(driver, "//*[@text='发送']")
            print("进入群聊页的结果是：{}".format(result))
        with allure.step('2、验证是否进入群聊天页'):
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step('3、添加群成员'):
            # 点击进入群设置页
            base.click_btn(locator=(By.XPATH, "//*[@text='发送']/../../../android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]"))
            # 点击添加【群成员】按钮
            base.click_btn(locator=(By.XPATH, "//*[@text='查看群成员']/../../../android.view.ViewGroup[3]"))
            # 点击搜索 进入搜索页
            base.click_btn(locator=(By.XPATH, "//*[@text = '搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@text='搜索' and @class='android.widget.EditText']"), value=contact1[0])
            # 点击被添加联系人【勾选】按钮
            base.click_btn(locator=(By.XPATH, "//*[@text='取消']/../../../../android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"))
            # 点击确定
            base.click_btn(locator=(By.XPATH, "//*[@text='确定']"))
            time.sleep(5)
        with allure.step('4、查看群成员'):
            # 点击查看群成员右侧 >
            base.click_btn(locator=(By.XPATH, "//*[@text='查看群成员']/../android.view.ViewGroup"))
            base.send_key(locator=(By.XPATH, "//*[@text='搜索' and @class='android.widget.EditText']"), value=contact1[0])
            # 是否找到该联系人头像
            result = PubMethod.is_ele(driver, "//*[@text='查看群成员']/../../../android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup")
            print("查找添加该成员的结果是：{}".format(result))
            with allure.step('5、验证是否添加该成员'):
                AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step('5、删除该成员'):
            # 返回群设置界面
            base.click_btn(locator=(By.XPATH, "//*[@text='查看群成员']/../android.view.ViewGroup"))
            # 点击移除群成员按钮
            base.click_btn(locator=(By.XPATH, "//*[@text='查看群成员']/../../../android.view.ViewGroup[5]"))
            base.send_key(locator=(By.XPATH, "//*[@text='搜索' and @class='android.widget.EditText']"), value=contact1[0])
            base.click_btn(locator=(By.XPATH, "//*[@text='删除群成员']/../../../android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup"))
            base.click_btn(locator=(By.XPATH, "//*[@text='确定']"))
            result = PubMethod.is_ele(driver, "//*[@text='无搜索结果']")
            print("删除该成员的结果是：{}".format(result))
        with allure.step('6、验证是否删除该成员'):
            AssertMethod.assert_true_screen_shot(driver, result)


if __name__ == "__main__":
    pytest.main(["test_02_addMembers.py"])
