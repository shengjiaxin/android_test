# coding=utf-8
import pytest
from appium import webdriver
from Common.publicMethod import PubMethod


@pytest.fixture(scope="function")
def start_app(android_setting):
    global driver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", android_setting)
    return PubMethod.is_login(driver, 2)


@pytest.fixture()
def reload_app():
    yield driver
    driver.quit()
