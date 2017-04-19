# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from selenium.webdriver.support.ui import WebDriverWait
from base_page import BasePage
from pageobject.parameter.locator_element import login_locators
from base_element import BaseTextElement


class UsernameElement(BaseTextElement):

    def __init__(self):
        self.locator = login_locators["login.username"]

    # def __set__(self, obj, val):
    #     dr = obj.driver
    #     WebDriverWait(dr, 100).until(
    #         lambda driver: driver.find_element(*self.locator))
    #     dr.find_element(*self.locator).clear()
    #     dr.find_element(*self.locator).send_keys(val)


class PasswordElement(BaseTextElement):

    def __init__(self):
        self.locator = login_locators["login.password"]

    # def __set__(self, obj, val):
    #     dr = obj.driver
    #     WebDriverWait(dr, 100).until(
    #         lambda driver: driver.find_element(*self.locator))
    #     dr.find_element(*self.locator).clear()
    #     dr.find_element(*self.locator).send_keys(val)


class LoginPage(BasePage):

    username = UsernameElement()
    password = PasswordElement()

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.open(login_locators.get("login.url"))

    def submit(self):
        "submit the login form"
        self.click_element(login_locators.get("login.submit"))

    @property
    def register(self):
        "jump to register page"
        self.click_element(login_locators["login.register"])
        from register_page import RegisterPage
        return RegisterPage(self.driver)
