# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
import unittest
from pageobject.driver.driver_factory import DriverFactory


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = DriverFactory.get_driver_singleton()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        # pass


if __name__ == '__main__':
    unittest.main()
