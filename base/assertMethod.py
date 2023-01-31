import logging
from Common.publicMethod import PubMethod


class AssertMethod:

    @staticmethod
    def assert_true_screen_shot(driver, bool_value):
        if not isinstance(bool_value, bool):
            logging.error('bool_value参数类型错误，必须传bool类型：exceptor=Ture/False')
        else:
            logging.info("正在进行元素断言：断言方式->%s：是否等于True" % bool_value)
            try:
                assert bool_value is True
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_false_screen_shot(driver, bool_value):
        if not isinstance(bool_value, bool):
            logging.error('bool_value参数类型错误，必须传bool类型：exceptor=Ture/False')
        else:
            logging.info("正在进行元素断言：断言方式->{}：是否等于False->{}".format(False, bool_value))
            try:
                assert False == bool_value
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e
