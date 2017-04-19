# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from menu_page import MenuPage
from base_element import BaseTextElement, BaseDropDownMenu
from pageobject.parameter.locator_element import newUser_locators


class DisplayNameElement(BaseTextElement):
    def __init__(self):
        self.locator = newUser_locators["newUser.name"]


class LoginNameElement(BaseTextElement):
    def __init__(self):
        self.locator = newUser_locators["newUser.login_name"]


class PhoneElement(BaseTextElement):
    def __init__(self):
        self.locator = newUser_locators["newUser.phone"]


class EmailElement(BaseTextElement):
    def __init__(self):
        self.locator = newUser_locators["newUser.email"]


class RoleDropDownMenu(BaseDropDownMenu):
    def __init__(self):
        self.btn_locator = newUser_locators["newUser.role_btn"]
        self.ul_locator = newUser_locators["newUser.role_ul"]


class NewUserPage(MenuPage):
    display_name = DisplayNameElement()
    login_name = LoginNameElement()
    phone = PhoneElement()
    email = EmailElement()
    role = RoleDropDownMenu()

    def submit(self):
        self.click_element(newUser_locators.get("newUser.submit"))
