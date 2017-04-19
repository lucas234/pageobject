# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from pageobject.page.menu_page import MenuPage
from base_element import BaseTableElement, BaseDropDownMenu
from pageobject.parameter.locator_element import ruleManagement_locators


class RuleTableElement(BaseTableElement):
    def __init__(self, driver):
        self.driver = driver
        self.column_locator = ruleManagement_locators["ruleManage.table_column"]
        self.row_locator = ruleManagement_locators["ruleManage.table_row"]
        self.tbody_locator = ruleManagement_locators["ruleManage.table_tbody"]


class CreateRuleDropDownMenu(BaseDropDownMenu):
    """the button dropdown created rule """
    def __init__(self):
        self.btn_locator = ruleManagement_locators["ruleManage.add_btn"]
        self.ul_locator = ruleManagement_locators["ruleManage.add_ul"]


class DisplayRuleDropDownMenu(BaseDropDownMenu):
    """the button dropdown display rule"""
    def __init__(self):
        self.btn_locator = ruleManagement_locators["ruleManage.dispalay_btn"]
        self.ul_locator = ruleManagement_locators["ruleManage.dispalay_ul"]


class RuleManagementPage(MenuPage):
    create_rule = CreateRuleDropDownMenu()
    display_rule = DisplayRuleDropDownMenu()

    @property
    def table(self):
        return RuleTableElement(self.driver)

    @property
    def create_condition(self):
        self.create_rule = 1
        from newRule_page import NewRulePage
        return NewRulePage(self.driver)

    @property
    def create_time(self):
        self.create_rule = 2
        from newRule_page import NewRulePage
        return NewRulePage(self.driver)

    @property
    def create_machine_learning(self):
        self.create_rule = 3
        from newRule_page import NewRulePage
        return NewRulePage(self.driver)

    def display_disable_rule_or_not(self):
        self.display_rule = 5

    def display_condition_rule_or_not(self):
        self.display_rule = 2

    def display_time_rule_or_not(self):
        self.display_rule = 3

    def display_machine_learning_rule_or_not(self):
        self.display_rule = 4

    def delete(self, rule_name):
        rule_name_dic = self.table.get_x_column_all_cell_text(2)
        if rule_name in rule_name_dic.keys():
            self.table.get_element(rule_name_dic[rule_name], 6).click()
        else:
            print "rule is not exist!"
