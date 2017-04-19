# _*_ coding=utf-8 _*_

import HTMLTestRunner
from general_function.base_function import *
import os
from pageobject import testcase, report_result
import unittest


class ExecuteTestCase(object):
    def __init__(self):
        pass

    def create_suite(self, dir_name, pattern):
        """
        :param pattern:test_case下.py文件名称的格式
        :param dir_name: test_case文件夹的路径
        :return:返回装填后的测试套件
        """
        test_unit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(dir_name, pattern=pattern, top_level_dir=None)
        for test_suite in discover:
            for test_case in test_suite:
                test_unit.addTests(test_case)

        return test_unit

    @classmethod
    def run(cls, pattern="unittest_*.py"):
        # 测试用例的路径
        dir_path = os.path.dirname(testcase.__file__)
        # 获取装填后的测试套件
        all_tests = cls.create_suite(dir_path, pattern)
        # 存放测试报告的路径
        filename = os.path.dirname(report_result.__file__) + get_slash() + get_time() + "result.html"
        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='XXX_UI_Test', description="tests_requirements")
        runner.run(all_tests)
        fp.close()

# aa = ExecuteTestCase()
# aa.run(r"device_*.py")


