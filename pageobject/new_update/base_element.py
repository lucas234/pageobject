# _*_ coding=utf-8 _*_
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
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


class BaseDropDownMenu(object):
    """Base DropDownMenu class that is initialized on every page object class."""

    def __init__(self, locator):
        # self.locator = locator
        k, v = locator
        self.locator = (_LOCATOR_MAP[k], v)

    def __set__(self, obj, value):
        dr = obj.driver
        self.dr = dr
        ul_element = dr.find_element(*self.locator)
        self.ul_element = ul_element
        if ul_element.tag_name.lower() == "select":
            Select(ul_element).select_by_visible_text(u"%s" % value)
        else:
             # dr.find_element_by_xpath(self.locator[1] + "/li[{0}]".format(value)).click()
            pass

    @property
    def numbers(self):
        number = len(Select(self.ul_element).options)
        return number

    @property
    def get_texts(self):
        all_texts = []
        for i in Select(self.ul_element).options:
            all_texts.append(i.text)
        return all_texts


class BaseTableElement(object):
    """Base table class that is initialized on every page object class."""
    def __init__(self, driver, locator):
        self.driver = driver
        k, v = locator
        self.locator = (_LOCATOR_MAP[k], v)
        self.ul_element = self.driver.find_element(*self.locator)

    @property
    def column(self):
        column = len(self.ul_element.find_elements_by_xpath('thead/tr/th'))
        return column

    @property
    def row(self):
        row = len(self.ul_element.find_elements_by_xpath('tbody/tr'))
        return row

    def get_element(self, *row_column):
        try:
            element = self.ul_element.find_element_by_xpath("tbody/tr[{0}]/td[{1}]".format(*row_column))
            return element
        except Exception as msg:
            print msg

    def get_cell_text(self, *value):
        if self.row:
            text = self.get_element(*value).text
        else:
            text = "Nothing"
        return text

    def get_x_cell_texts(self, cell, flag=True):
        """get all value about some column or row , cell stand for row if flag=True,"""
        texts = {}
        if flag and cell < self.row:
            for i in range(1, self.column+1):
                temp_row = self.get_cell_text(cell, i)
                texts[i] = temp_row
        elif not flag and cell < self.column:
            for i in range(1, self.row+1):
                temp_column = self.get_cell_text(i, cell)
                texts[i] = temp_column
        return texts





