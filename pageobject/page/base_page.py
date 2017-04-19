# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from abc import abstractmethod
from pageobject.log.logger import Logging
import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    base_url = "http://xxx.xxx.xx.xx:xxxx/"

    def __init__(self, driver):
        if self.base_url[-1] != '/':
            self.base_url += '/'
        # self._validate_page(driver)
        self.driver = driver
        self.log_obj = Logging()

    @abstractmethod
    def _validate_page(self, driver):
        return

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_xpath(self, xpath):
        "return the DOM element of the xpath or the None object if the element is not found"

    def click_element(self, locator, is_button=True):
        "click the button supplied"
        if is_button:
            self.driver.find_element(*locator).click()
        else:
            f = self.driver.find_element(*locator)
            ActionChains(self.driver).click(f).perform()

    def write(self, msg, level='error'):
        self.log_obj.write(msg, level)

    def set_text(self, locator, values):
        try:
            text_field = self.driver.find_element(*locator)
            text_field.clear()
            text_field.send_keys(values)
        except Exception as msg:
            self.write(msg)

    def wait(self, wait_seconds=5):
        "performs wait for time provided"
        time.sleep(wait_seconds)


class InvalidPageException(Exception):
    pass


