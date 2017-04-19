# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from base_page import BasePage
from base_page import InvalidPageException
from pageobject.parameter.locator_element import menu_locators


class MenuPage(BasePage):

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver)

    def _validate_page(self, driver):
        """validate the current pag is exist"""
        try:
            driver.find_element(*menu_locators.get("menu.welcome"))
        except:
            raise InvalidPageException("Home Page not loaded")

    def logout(self):
        """click to logout"""
        self.click_element(menu_locators.get("menu.logout.select"))
        self.click_element(menu_locators.get("menu.logout.logout"))

    @property
    def user_management(self):
        """jump to user list page"""
        self.click_element(menu_locators["menu.user_management"])
        from userList_page import UserListPage
        return UserListPage(self.driver)

    @property
    def group_list(self):
        """jump to group list page"""
        self.click_element(menu_locators["menu.user_management"])
        self.wait(4)
        self.click_element(menu_locators["menu.group_list"])
        from groupList_page import GroupListPage
        return GroupListPage(self.driver)

    @property
    def gateway_management(self):
        """jump to gateway page"""
        self.click_element(menu_locators["menu.gateway_management"])
        from gatewayManagement_page import GatewayManagementPage
        return GatewayManagementPage(self.driver)

    @property
    def device_management(self):
        """jump to device overview page"""
        self.click_element(menu_locators["menu.device_management"])
        from deviceOverview_page import DeviceOverviewPage
        return DeviceOverviewPage(self.driver)

    @property
    def device_control(self):
        """jump to device control page"""
        self.click_element(menu_locators["menu.device_management"])
        self.wait(4)
        self.click_element(menu_locators["menu.device_monitor"])
        from deviceControl_page import DeviceControlPage
        return DeviceControlPage(self.driver)

    @property
    def data_report(self):
        """jump to data report page"""
        self.click_element(menu_locators["menu.data_report"])
        from dataReport_page import DataReportPage
        return DataReportPage(self.driver)

    @property
    def rule_management(self):
        """jump to rule page"""
        self.click_element(menu_locators["menu.rule_management"])
        from ruleManagement_page import RuleManagementPage
        return RuleManagementPage(self.driver)

    @property
    def device_monitor(self):
        """jump to device monitor page"""
        self.click_element(menu_locators["menu.device_monitor"])
        from deviceMonitor_page import DeviceMonitorPage
        return DeviceMonitorPage(self.driver)

    @property
    def setting(self):
        """jump to setting page"""
        self.click_element(menu_locators["menu.setting"])
        from setting_page import SettingPage
        return SettingPage(self.driver)
