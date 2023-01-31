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
    return driver


@pytest.fixture()
def reload_app():
    yield driver
    base = Base(driver)
    time.sleep(3)
    base.click_btn(locator=(By.XPATH, "(//*[@resource-id='headerContainer']/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1])[2]"))
    time.sleep(5)
    base.click_btn(locator=(By.XPATH, "//*[@text='取消']"))
    PubMethod.log_out(driver)
    driver.quit()



