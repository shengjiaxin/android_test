# coding=utf-8
import csv
import logging
import os

BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join(BIR, 'Data', 'account.csv')

class ReadCsvData(object):

    def __init__(self, csvfile=None):
        if csvfile != None:
            self.csvfile = csvfile
        self.csvfile = csvpath

    def get_csv_data(self, line):
        try:
            with open(self.csvfile, 'r', encoding='utf-8-sig') as cf:
                data = csv.reader(cf)
                for index, items in enumerate(data, 1):  # 从索引1开始
                    if index == line:
                        return items
        except Exception as e:
            logging.error("获取Excel数据失败，错误信息为：{}".format(e))