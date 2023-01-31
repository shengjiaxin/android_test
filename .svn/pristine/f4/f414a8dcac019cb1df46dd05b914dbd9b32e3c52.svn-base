# coding=utf-8
import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from Common.publicMethod import PubMethod
from base.base import Base


@pytest.fixture(scope="function")
def start_app(android_setting):
    global driver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", android_setting)
    return PubMethod.is_login(driver, 2)


@pytest.fixture()
def reload_app():
    yield driver
    base = Base(driver)
    base.click_btn(locator=(By.XPATH, "//*[@text='focustalk.apk']/../android.view.ViewGroup"))
    base.click_btn(locator=(By.XPATH, "//*[@text='群文件']/../android.view.ViewGroup"))
    base.click_btn(locator=(By.XPATH, "//*[@text='群设置']/../android.view.ViewGroup"))
    time.sleep(3)
    base.click_btn(locator=(By.XPATH, "//*[@text='发送']/../../../android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]"))
    base.click_btn(locator=(By.XPATH, "//*[@text='取消']"))
    base.click_btn(locator=(By.XPATH, "//android.widget.Button[@content-desc='我的, tab, 4 of 4']/android.widget.ImageView"))
    base.click_btn(locator=(By.XPATH, "//*[@text='清除缓存']"))
    base.click_btn(locator=(By.XPATH, "//*[@text='确定']"))
    base.click_btn(locator=(By.ID, "android:id/button1"))
    time.sleep(10)
    driver.quit()
