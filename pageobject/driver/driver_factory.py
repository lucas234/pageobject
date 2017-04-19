# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from selenium import webdriver
import os


class DriverFactory(object):
    # singleton
    _instance = None
    _driver = None
    firefox_driver_path = os.path.join(os.path.dirname(__file__), "webdriver/geckodriver")
    chrome_driver_path = os.path.join(os.path.dirname(__file__), "webdriver/chromedriver")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DriverFactory, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get_driver_singleton(cls, browser="firefox"):

        if cls._driver is None:
            cls._driver = cls.get_driver(browser)
        return cls._driver

    @classmethod
    def get_driver(cls, driver="firefox"):

        obj_driver = None
        if driver.lower() == "firefox":
            obj_driver = webdriver.Firefox(executable_path=cls.firefox_driver_path)
        elif driver.lower() == "chrome":
            obj_driver = webdriver.Chrome(executable_path=cls.chrome_driver_path)
        elif driver.lower() == "ie":
            obj_driver = webdriver.Ie()
        elif driver.lower() == "Safari":
            obj_driver = webdriver.Safari()

        return obj_driver

