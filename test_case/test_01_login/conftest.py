# coding=utf-8
import time
import pytest
from appium import webdriver


# 启动APP
@pytest.fixture(scope="function")
def start_app(android_setting):
    global driver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", android_setting)
    return driver


# 退出APP
@pytest.fixture()
def reload_app():
    yield driver
    time.sleep(2)
    driver.quit()
