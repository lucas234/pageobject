# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from base_testcase import BaseTestCase
from pageobject.page.page_factory import get_page
from pageobject.page.gatewayManagement_page import GatewayManagementPage
from pageobject.page.userList_page import UserListPage
from pageobject.page.setting_page import SettingPage
from pageobject.page.ruleManagement_page import RuleManagementPage


class LoginTest(BaseTestCase):

    def test_login(self):
        obj = get_page("login", self.driver)
        obj.username = "xxxxx"
        obj.password = "xxxxx"
        obj.submit()
        import time
        time.sleep(5)
        # rule test---------------start
        self.driver.find_element_by_link_text(u"规则管理").click()
        time.sleep(5)
        rule = RuleManagementPage(self.driver)
        print rule.table.get_x_column_all_cell_text(2)
        # rule.display_disable_rule_or_not()
        # rule.display_machine_learning_rule_or_not()
        # rule.create_condition
        # rule test---------------end

        # #user list test--------start
        # self.driver.find_element_by_link_text(u"用户管理").click()
        # time.sleep(5)
        # self.driver.find_element_by_link_text(u"用户列表").click()
        # time.sleep(5)
        # a = UserListPage(self.driver)
        # print a.b
        # time.sleep(5)
        # print a.table.column
        # print a.table.row
        # print a.table.get_cell_text(1, 1)
        # print a.table.get_x_column_all_cell_text(2)
        # new = a.create_user
        # new.role = u"用户管理员"
        # new.submit()
        # user list test-----------end

        # gateway management test-----------start
        # self.driver.find_element_by_link_text(u"网关管理").click()
        # time.sleep(6)
        # a = GatewayManagementPage(self.driver)
        # a.building = "S2"
        # a.floor = "S212"
        # a.area = "S212M"
        # a.create_gateway
        # gateway management test-----------end

        # # #setting test--------start
        # self.driver.find_element_by_link_text(u"设置").click()
        # time.sleep(5)
        # set_obj = SettingPage(self.driver)
        # set_obj.old_password = "123"
        # set_obj.new_password = "234"
        # set_obj.repeat_new_password = "123"
        # set_obj.submit()
        # # #setting test--------end

        time.sleep(20)
