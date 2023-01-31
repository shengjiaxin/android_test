# coding=utf-8
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from base.base import Base
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod

date = PubMethod.get_date()
contact = PubMethod.get_csv_data(4)


@allure.feature("消息的发送与接收")
class TestPic:

    @allure.story('图片消息的发送与接收')
    @allure.title('[case01] 验证图片消息的发送')
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.dependency()
    def test_picMes_case01(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        PubMethod.is_login(driver, 2)
        with allure.step('1、搜素联系人'):
            time.sleep(5)
            base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact[1])
            result = PubMethod.is_ele(driver, "//*[@text='联系人']/../../android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]")
            # 如果找不到联系人，可能是执行上个用例时没有正常退出接收方的账号，所以进行重登操作
            if not result:
                base.click_btn(locator=(By.XPATH, "//*[@text='取消']"))
                PubMethod.log_out(driver)
                PubMethod.login(driver, 2)
                base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
                base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact[1])
            base.click_btn(locator=(By.XPATH, "//*[@text='联系人']/../../android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]"))
            time.sleep(5)
            result = PubMethod.is_ele(driver, "//*[@text='发送']")
            print(result)
            print("进入聊天页的结果是：{}".format(result))
        with allure.step('2、验证是否进入聊天页'):
            # 断言 实际结果 == True
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step("3、发文本"):
            base.value_clear(locator=(By.XPATH, "//*[@text='发送']/../../android.widget.EditText"))
            base.send_key(locator=(By.XPATH, "//*[@text='发送']/../../android.widget.EditText"), value="图片：" + date)
            base.click_btn(locator=(By.XPATH, '//*[@text="发送"]'))
            base.send_key(locator=(By.XPATH, "//*[@text='发送']/../../../android.widget.EditText"), value="1")
            base.click_btn(locator=(By.XPATH, '//*[@text="发送"]'))
        with allure.step('4、发图片消息'):
            # 点击菜单栏图片按钮
            base.click_btn(locator=(By.XPATH, "//*[@text='发送']/../../../../android.view.ViewGroup[6]"))
            #  权限允许
            PubMethod.check_permission_public(driver)
            base.click_btn(locator=(By.XPATH, "//*[@text='相册']/../../android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView"))
            # 点击发送
            base.click_btn(locator=(By.XPATH, "//*[@text = '相册']/../../android.view.ViewGroup[10]/android.widget.TextView"))
            # 通过是否存在发送失败按钮 断言
            ele = PubMethod.is_ele_within(driver, "//*[@text='图片：" + date + "']/../../../following-sibling::android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView", 30)
        with allure.step('5、验证图片是否发送成功'):
            AssertMethod.assert_false_screen_shot(driver, ele)

    @allure.story('图片消息的发送与接收')
    @allure.title('[case02] 验证图片消息的接收')
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.dependency(depends=["TestPic::test_picMes_case01"])
    def test_picMes_case02(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        with allure.step('1、登录接收方账号'):
            time.sleep(3)
            PubMethod.login(driver, 3)
        with allure.step('2、验证是否进入聊天页'):
            base.click_btn(locator=(By.XPATH, "//*[@text = '搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact[0])
            time.sleep(3)
            base.click_btn(locator=(By.XPATH, "//*[@text='联系人']/../../android.view.ViewGroup[2]"))
            result = PubMethod.is_ele(driver, "//*[@text='发送']")
            print("进入聊天页的结果是：{}".format(result))
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step('3、验证图片是否接收成功'):
            time.sleep(5)
            ele = PubMethod.is_ele(driver, "//*[@text='图片：" + date + "' ]/../../../following-sibling::android.view.ViewGroup[2]")
            print("接收图片的结果是:{}".format(ele))
            AssertMethod.assert_true_screen_shot(driver, ele)


if __name__ == "__main__":
    pytest.main(["test_02_picMes.py"])
