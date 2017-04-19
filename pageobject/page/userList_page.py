# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from menu_page import MenuPage
from base_element import BaseTextElement, BaseDropDownMenu, BaseTableElement
from pageobject.parameter.locator_element import userList_locators


class SearchElement(BaseTextElement):
    def __init__(self):
        self.locator = userList_locators["user_list.search_text"]


class DropDownMenuElement(BaseDropDownMenu):
    def __init__(self):
        self.btn_locator = userList_locators["user_list.drop_down_btn"]
        self.ul_locator = userList_locators["user_list.drop_down_ul"]


class UserListTableElement(BaseTableElement):
    def __init__(self, driver):
        self.driver = driver
        self.column_locator = userList_locators["user_list.table_column"]
        self.row_locator = userList_locators["user_list.table_row"]
        self.tbody_locator = userList_locators["user_list.table_tbody"]


class UserListPage(MenuPage):
    search_text = SearchElement()
    search_by = DropDownMenuElement()

    @property
    def table(self):
        return UserListTableElement(self.driver)

    @property
    def create_user(self):
        self.click_element(userList_locators.get("user_list.create_user"))
        from newUser_page import NewUserPage
        return NewUserPage(self.driver)

    # @property
    def search(self):
        self.click_element(userList_locators.get("user_list.search_btn"))
        # from search_page import SearchResult
        # return SearchResult(self.driver)

    @property
    def b(self):
        return self.driver.current_url
