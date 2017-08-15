# _*_ coding=utf-8 _*_
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
_LOCATOR_MAP = {'css': By.CSS_SELECTOR,
                'id_': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT,
                'tag_name': By.TAG_NAME,
                'class_name': By.CLASS_NAME,
                }


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""
    def __init__(self, locator):
        # self.locator = locator
        k, v = locator
        self.locator = (_LOCATOR_MAP[k], v)

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        dr = obj.driver
        WebDriverWait(dr, 100).until(
            lambda driver: driver.find_element(*self.locator))
        dr.find_element(*self.locator).clear()
        dr.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element
