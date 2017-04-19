# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from menu_page import MenuPage
from pageobject.parameter.locator_element import gatewayManage_locators
from base_element import BaseDropDownMenu


class BuildingDropDownElement(BaseDropDownMenu):

    def __init__(self):
        self.btn_locator = gatewayManage_locators["gatewayManage.dropdown_btn"]
        self.ul_locator = gatewayManage_locators["gatewayManage.dropdown_building"]


class FloorDropDownElement(BaseDropDownMenu):

    def __init__(self):
        self.btn_locator = gatewayManage_locators["gatewayManage.dropdown_btn"]
        self.ul_locator = gatewayManage_locators["gatewayManage.dropdown_floor"]


class AreaDropDownElement(BaseDropDownMenu):

    def __init__(self):
        self.btn_locator = gatewayManage_locators["gatewayManage.dropdown_btn"]
        self.ul_locator = gatewayManage_locators["gatewayManage.dropdown_area"]


class BlockDropDownElement(BaseDropDownMenu):

    def __init__(self):
        self.btn_locator = gatewayManage_locators["gatewayManage.dropdown_btn"]
        self.ul_locator = gatewayManage_locators["gatewayManage.dropdown_block"]


class SeatDropDownElement(BaseDropDownMenu):

    def __init__(self):
        self.btn_locator = gatewayManage_locators["gatewayManage.dropdown_btn"]
        self.ul_locator = gatewayManage_locators["gatewayManage.dropdown_seat"]


class GatewayManagementPage(MenuPage):

    building = BuildingDropDownElement()
    floor = FloorDropDownElement()
    area = AreaDropDownElement()
    block = BlockDropDownElement()
    seat = SeatDropDownElement()

    @property
    def create_gateway(self):
        self.click_element(gatewayManage_locators.get("gatewayManage.create_gateway"))
        return NewGateway(self.driver)

    @property
    def search_for(self):
        self.click_element(gatewayManage_locators.get("gatewayManage.search_btn"))
        from search_page import SearchResult
        return SearchResult(self.driver)


class NewGateway(MenuPage):
    pass
