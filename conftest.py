# coding=utf-8
import warnings
import pytest


# 配置app连接信息
# 红米
@pytest.fixture(scope='session')
def android_setting():
    warnings.filterwarnings("ignore")
    desired_caps = {"platformName": "Android",
                    "deviceName": "m11",
                    "platformVersion": "12",
                    # 'appPackage': 'com.focus.focustalk',
                    # 'appActivity': '.MainActivity t687',
                    "noReset": True,
                    "unicodeKeyboard": True,
                    "resetKeyboard": True,
                    "waitForIdleTimeout": 100,
                    "automationName": "UiAutomator2",

                    "appium:appPackage": "com.focus.focustalk",
                    "appium:appActivity": ".MainActivity t280"

                    }
    return desired_caps

