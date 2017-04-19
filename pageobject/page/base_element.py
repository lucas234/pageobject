# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BaseTextElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        dr = obj.driver
        WebDriverWait(dr, 100).until(
            lambda driver: driver.find_element(*self.locator))
        dr.find_element(*self.locator).clear()
        dr.find_element(*self.locator).send_keys(value)

    def __delete__(self, obj):
        pass

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        # driver = obj.driver
        # WebDriverWait(driver, 100).until(
        #     lambda driver: driver.find_element(*self.locator))
        # element = driver.find_element(*self.locator)
        # return element.get_attribute("value")
        pass


class BaseDropDownMenu(object):
    """Base DropDownMenu class that is initialized on every page object class."""

    def __set__(self, obj, value):
        dr = obj.driver
        # element = dr.find_element(*self.btn_locator)
        # ActionChains(dr).click(element).perform()
        dr.find_element(*self.btn_locator).click()
        ul_element = dr.find_element(*self.ul_locator)
        if ul_element.tag_name.lower() != "select":
            # dr.find_element_by_link_text(u"%s" % value).click()
            dr.find_element_by_xpath(self.ul_locator[1] + "/li[{0}]".format(value)).click()
        else:
            try:
                dr.find_element(*self.ul_locator).click()
            except Exception:
                dr.find_element(*self.btn_locator).click()
                dr.find_element(*self.ul_locator).click()
            dr.find_element_by_css_selector("option[value=\"%s\"]" % value).click()


class BaseTableElement(object):
    """Base table class that is initialized on every page object class."""

    @property
    def column(self):
        column = len(self.driver.find_elements(*self.column_locator))
        return column

    @property
    def row(self):
        row = len(self.driver.find_elements(*self.row_locator))
        return row

    def get_element(self, *row_column):
        try:
            element = self.driver.find_element_by_xpath(self.tbody_locator + "/tr[{0}]/td[{1}]".format(*row_column))
            return element
        except Exception as msg:
            print msg

    def get_cell_text(self, *value):
        # locator = "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div/div/section/div[2]/table/tbody"
        if self.row:
            text = self.get_element(*value).text
        else:
            text = "Nothing"
        return text

    def get_x_column_all_cell_text(self, column):
        """get all value about some column and row-column , such as {value:(1,2)}"""
        text_row = {}
        if self.row:
            for i in range(1, self.row+1):
                temp = self.get_cell_text(i, column)
                text_row[temp] = i
        else:
            text_row = {}
        return text_row




