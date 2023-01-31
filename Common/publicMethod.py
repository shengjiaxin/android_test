# coding=utf-8
import datetime
import random
import string
import sys
import yaml
import os
import time
import logging
import allure
from Common.fileOption import FileOption
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from base.base import Base
from Common.read_csv import ReadCsvData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

'''公共方法'''


class PubMethod:

    @staticmethod
    def get_rand_num(min=10, max=200, type=1):
        """
        获取随机数
        :param min:最小值
        :param max: 最大值
        :param type: 类型，1为浮点型，2为布尔值，0为整型
        :return:
        """
        value = random.uniform(min, max)
        if type == 1:
            return float(round(value, 1))
        elif type == 0:
            return int(value)
        elif type == 2:
            return random.randint(0, 1)

    @staticmethod
    def read_yaml(file):
        """
        读取yaml文件，返回文件对象
        @param file:
        @return:
        """
        if os.path.isfile(file):
            fr = open(file, 'r', encoding='utf-8')
            yaml_info = yaml.safe_load(fr)
            fr.close()
            return yaml_info
        else:
            logging.error(file, '文件不存在')
            sys.exit()

    @staticmethod
    def random_string(strings=string.ascii_letters, length=15):
        values = ''.join(random.choices(strings, k=length))
        return values

    @staticmethod
    def create_file(file_path):
        """
        创建文件，当目录不存在时自动创建
        :param file_path:
        """
        dir_path = os.path.split(file_path)[0]
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.isfile(file_path):
            f = open(file_path, mode='w', encoding='utf-8')
            f.close()

    @staticmethod
    def create_dirs(file_dir):
        """
        创建文件路径,先判断目录是否存在
        :param file_dir:
        """
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    @staticmethod
    def screen_picture(driver):
        picture_url = None
        """
        截图操作
        """
        try:
            logging.info("正在进行截图操作：")
            picture_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            file_path = "Report/picture"
            file_name = picture_time + ".png"
            FileOption.file_mkdir(file_path)
            res = driver.get_screenshot_as_file(file_path + '/' + file_name)
            picture_url = file_path + '/' + file_name
            allure.attach.file(picture_url, attachment_type=allure.attachment_type.PNG)
            logging.info("截图成功，picture_url为：{}".format(picture_url))
        except Exception as e:
            logging.error("截图失败，错误信息为：{}".format(e))
        finally:
            return picture_url

    @staticmethod
    def is_element_exist(driver, elements, timeout=3):
        """
        判断元素是否存在
        """
        count = 0
        while count < timeout:
            souce = driver.page_source
            if elements in souce:
                return True
            else:
                count += 1
                time.sleep(1)
        return False

    @staticmethod
    def is_ele(driver, xpath):
        try:
            WebDriverWait(driver, 5, 0.5).until(ec.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    @staticmethod
    def is_ele_within(driver, xpath, time):
        """
        判断元素
        :param time:等待时间
        """
        try:
            WebDriverWait(driver, time, 0.5).until(ec.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    @staticmethod
    def check_permission_public(driver):
        """
        检查首次会弹出的权限提示
        @return:
        """
        base = Base(driver)
        miui_agree = 'com.lbe.security.miui:id/permission_allow_foreground_only_button'
        miui_agree1 = 'com.lbe.security.miui:id/permission_allow_foreground_only_button'
        pers_pic_audio = [miui_agree, miui_agree1]
        for item1 in pers_pic_audio:
            try:
                ele1 = WebDriverWait(driver, 3, 0.5).until(ec.visibility_of_element_located((By.ID, item1)))
                if ele1:
                    base.click_btn(locator=(By.ID, item1))
                else:
                    pass
                return True
            except Exception as e:
                logging.error("不需要权限校验".format(e))
                return False


    @staticmethod
    def touch_long_press(driver, find_element=None, x=None, y=None, duration=None):
        TouchAction(driver).long_press(find_element, x, y, duration).wait(1000).perform()

    @staticmethod
    def swipe_up(driver, t=500, n=1):
        """
        向上滑动屏幕
        :t 持续时间
        :n 滑动次数
        """
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标 屏幕宽度的1/2
        y1 = l['height'] * 0.75  # 起始y坐标 屏幕高度的3/4
        y2 = l['height'] * 0.25  # 终点y坐标 屏幕高度的1/4
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    @staticmethod
    def get_toast(driver, xpath, timeout=10, poll_frequency=0.01):
        """
        获取toast弹窗中文字
        :param driver:
        :param xpath: 页面看到的文本
        :param timeout: 最大超时时间，默认10
        :param poll_frequency: 间隔查询时间，默认0.01s查询一次
        """
        try:
            WebDriverWait(driver, timeout, poll_frequency).until(ec.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    @staticmethod
    def get_date():
        return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    @staticmethod
    def get_dateByMS():
        return time.strftime("%M-%S", time.localtime())

    @staticmethod
    def get_str():
        """
        随机生成8位字符串 大小写字母+数字
        :return:
        """
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))

    @staticmethod
    def get_csv_data(row):
        return ReadCsvData().get_csv_data(row)

    @staticmethod
    def login(driver, row):
        base = Base(driver)
        csv_data = ReadCsvData().get_csv_data(row)
        time.sleep(2)
        base.value_clear(locator=(By.XPATH, "//*[@text='登录']/../../../../android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText"))
        base.send_key(locator=(By.XPATH, "//*[@text='登录']/../../../../android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText"), value=csv_data[0])
        base.send_key(locator=(By.XPATH, "//*[@text='请输入密码']"), value=csv_data[1])
        base.click_btn(locator=(By.XPATH, "//*[@text='登录']"))

        # time.sleep(10)
        # base.click_btn(locator=(By.IMAGE, r"C:\Users\shengjiaxin\Desktop\focustalk_android_04\Common\login.png"))

        # driver.update_settings({
        #                         "imageMatchThreshold": 0.9,
        #                         "getMatchedImageResult": True,
        #                         "fixImageTemplateScale": True
        #
        #                         })
        # driver.update_settings({"getMatchedImageResult": True})
        # el = driver.find_element_by_image('./Login.png')
        # el.get_attribute('visual')

        # base.click_btn(locator=(By.IMAGE, r"./01.png"))
        # path = r"C:\Users\shengjiaxin\Desktop\focustalk_android_04\test_case\test_01_login\login.png"
        # base.click_btn(locator=(By.IMAGE, el))


    @staticmethod
    def log_out(driver):
        base = Base(driver)
        time.sleep(3)
        base.click_btn(locator=(By.XPATH, '//android.widget.Button[@content-desc="我的, tab, 4 of 4"]'))
        time.sleep(2)
        base.click_btn(locator=(By.XPATH, "//*[@text='退出登录']"))
        time.sleep(2)
        base.click_btn(locator=(By.XPATH, "//*[@text='确定']"))
        time.sleep(2)

    @staticmethod
    def is_login(driver, row):
        if PubMethod.is_ele(driver, '//*[@text="登录"]'):
            PubMethod.login(driver, row)
        return driver
