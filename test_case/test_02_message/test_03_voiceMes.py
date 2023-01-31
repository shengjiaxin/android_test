# coding=utf-8
import time
import allure
import pytest
from selenium.webdriver.common.by import By
from Common.publicMethod import PubMethod
from base.assertMethod import AssertMethod
from base.base import Base

date = PubMethod.get_date()
contact = PubMethod.get_csv_data(4)


@allure.feature("消息的发送与接收")
class TestVoice:

    @allure.story('语音消息的发送与接收')
    @allure.title('[case01] 验证语音消息的发送')
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.dependency()
    def test_voiceMes_case01(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        PubMethod.is_login(driver, 2)
        with allure.step("1、搜索联系人进入聊天窗口"):
            time.sleep(5)
            base.click_btn(locator=(By.XPATH, "//*[@text = '搜索']"))
            base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact[1])
            result = PubMethod.is_ele(driver, "//*[@text='联系人']/../../android.view.ViewGroup[2]")
            # 如果找不到联系人，可能是上个用例没有正常退出接收方的账号，所以进行重登操作
            if not result:
                base.click_btn(locator=(By.XPATH, "//*[@text='取消']"))
                PubMethod.log_out(driver)
                PubMethod.login(driver, 2)
                base.click_btn(locator=(By.XPATH, "//*[@text='搜索']"))
                base.send_key(locator=(By.XPATH, "//*[@class ='android.widget.EditText' and @text='搜索']"), value=contact[1])
            base.click_btn(locator=(By.XPATH, "//*[@text='联系人']/../../android.view.ViewGroup[2]"))
            time.sleep(5)
            result = PubMethod.is_ele(driver, "//*[@text='发送']")
            print("进入聊天页的结果是：{}".format(result))
        with allure.step('2、验证是否进入聊天页'):
            AssertMethod.assert_true_screen_shot(driver, result)
        with allure.step("3、发送语音消息"):
            # 先发送文本
            base.value_clear(locator=(By.XPATH, "//*[@text='发送']/../../android.widget.EditText"))
            base.send_key(locator=(By.XPATH, "//*[@text='发送']/../../android.widget.EditText"), value="语音：" + date)
            base.click_btn(locator=(By.XPATH, '//*[@text="发送"]'))
            base.send_key(locator=(By.XPATH, "//*[@text='发送']/../../../android.widget.EditText"), value="1")
            base.click_btn(locator=(By.XPATH, '//*[@text="发送"]'))
            # 再发送语音
            base.click_btn(locator=(By.XPATH, '//*[@text="发送"]/../../../../android.view.ViewGroup[4]'))
            # 判断录音权限
            PubMethod.check_permission_public(driver)
            base.long_press(locator=(By.XPATH, '//*[@text="按住说话"]/following-sibling::android.view.ViewGroup[1]'), time=10000)
        with allure.step("4、验证消息是否已发送"):
            ele = PubMethod.is_ele_within(driver, "//*[@text='语音：" + date + "']/../../../following-sibling::android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView", 30)
            AssertMethod.assert_false_screen_shot(driver, ele)

    @allure.story('语音消息的发送与接收')
    @allure.title('[case02] 验证语音消息的接收')
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.dependency(depends=["TestVoice::test_voiceMes_case01"])
    def test_voiceMes_case02(self, start_app, reload_app):
        driver = start_app
        base = Base(driver)
        with allure.step("1、登录接收方账号"):
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
        with allure.step('3、验证语音是否接收成功'):
            time.sleep(5)
            voice_result = PubMethod.is_ele(driver, "//*[@text='语音：" + date + "' ]/../../../following-sibling::android.view.ViewGroup[2]")
            print("接收语音的结果是:{}".format(voice_result))
            AssertMethod.assert_true_screen_shot(driver, voice_result)


if __name__ == "__main__":
    pytest.main(["test_03_voiceMes.py"])
