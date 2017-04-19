# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from menu_page import MenuPage
from base_element import BaseTextElement
from pageobject.parameter.locator_element import setting_locators


class OldPasswordElement(BaseTextElement):
    def __init__(self):
        self.locator = setting_locators["setting.old_password"]


class NewPasswordElement(BaseTextElement):
    def __init__(self):
        self.locator = setting_locators["setting.new_password"]


class NewPasswordAgainElement(BaseTextElement):
    def __init__(self):
        self.locator = setting_locators["setting.repeat_password"]


class SettingPage(MenuPage):
    old_password = OldPasswordElement()
    new_password = NewPasswordElement()
    repeat_new_password = NewPasswordAgainElement()

    def submit(self):
        self.click_element(setting_locators["setting.submit"])
