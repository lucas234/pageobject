# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from selenium.webdriver.common.by import By

login_locators = {"login.url": "xxxxxx",
                  "login.username": (By.NAME, "username"),
                  "login.password": (By.NAME, "password"),
                  "login.submit": (By.XPATH, "//button[@type='submit']/span"),
                  "login.register": (By.ID, "register"),
                  }

menu_locators = {"menu.url": "xxxx",
                 "menu.welcome": (By.XPATH, '//*[@id="wrapper"]/div/aside[2]/section/ol/li/a'),
                 "menu.logout.select": (By.CSS_SELECTOR, "span.ng-binding"),
                 "menu.logout.logout": (By.LINK_TEXT, u"用户登出"),
                 "menu.user_management": (By.LINK_TEXT, u"用户管理"),
                 "menu.group_list": (By.LINK_TEXT, u"群组列表"),
                 "menu.device_management": (By.LINK_TEXT, u"设备管理"),
                 "menu.device_control": (By.LINK_TEXT, u"设备控制"),
                 "menu.gateway_management": (By.LINK_TEXT, u"网关管理"),
                 "menu.rule_management": (By.LINK_TEXT, u"规则管理"),
                 "menu.device_monitor": (By.LINK_TEXT, u"设备监控"),
                 "menu.setting": (By.LINK_TEXT, u"设置"),
                 "menu.data_report": (By.LINK_TEXT, u"数据报表"),
                 }

userList_locators = {"user_list.url": "xxxxxx",
                     "user_list.search_text": (By.XPATH, "//input[@type='text']"),
                     "user_list.search_btn": (By.XPATH, "(//button[@type='button'])[2]"),
                     "user_list.create_user": (By.XPATH, "//div[@id='wrapper']/div/aside[2]/section/div/div/div/div/div/div/div/section/div/div/div/button"),
                     "user_list.drop_down_btn": (By.XPATH, "//*[@id=\"search-filter\"]"),
                     "user_list.drop_down_ul": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div/div/section/div[1]/div/div[2]/div/div/ul"),
                     "user_list.table_row": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div/div/section/div[2]/table/tbody/tr"),
                     "user_list.table_column": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div/div/section/div[2]/table/thead/tr/th"),
                     "user_list.table_tbody": "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div/div/section/div[2]/table/tbody",
                     }

newUser_locators = {"newUser.role": (),
                    "newUser.name": (By.NAME, "displayName"),
                    "newUser.login_name": (By.NAME, "loginName"),
                    "newUser.phone": (By.NAME, "phone"),
                    "newUser.email": (By.NAME, "mail"),
                    "newUser.submit": (By.NAME, "submit"),
                    "newUser.role_btn": (By.XPATH, "//*[@id=\"search-filter\"]"),
                    "newUser.role_ul": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div/div/section/div/form/div[2]/div/div/ul"),
                    }

gatewayManage_locators = {"gatewayManage.url": "xxxxxx",
                          "gatewayManage.create_gateway": (By.XPATH, "//div[@id='wrapper']/div/aside[2]/section/div/div/div/div/div/div/button"),
                          "gatewayManage.search_btn": (By.XPATH, "//section[@id='gateway-list']/header/div/div[2]/button"),
                          "gatewayManage.dropdown_btn": (By.XPATH, "(//button[@id='search-filter'])[2]"),
                          "gatewayManage.dropdown_building": (By.XPATH, "//section[@id='gateway-list']/header/div/div[2]/div/div/div/div/div/div/select"),
                          "gatewayManage.dropdown_floor": (By.XPATH, "//section[@id='gateway-list']/header/div/div[2]/div/div/div/div/div/div[2]/select"),
                          "gatewayManage.dropdown_area": (By.XPATH, "//section[@id='gateway-list']/header/div/div[2]/div/div/div/div/div/div[3]/select"),
                          "gatewayManage.dropdown_block": (By.XPATH, "//section[@id='gateway-list']/header/div/div[2]/div/div/div/div/div/div[4]/select"),
                          "gatewayManage.dropdown_seat": (By.XPATH, "//section[@id='gateway-list']/header/div/div[2]/div/div/div/div/div/div[5]/select"),
                          }

setting_locators = {"setting.url": "xxxxxx",
                    "setting.old_password": (By.XPATH, "//input[@type='password']"),
                    "setting.new_password": (By.XPATH, "(//input[@type='password'])[2]"),
                    "setting.repeat_password": (By.XPATH, "(//input[@type='password'])[3]"),
                    "setting.submit": (By.NAME, "submit"),
                    }

ruleManagement_locators = {"ruleManage.url": "xxxxxxx",
                           "ruleManage.add_btn": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div[2]/span"),
                           "ruleManage.add_ul": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div[2]/ul"),
                           "ruleManage.table_column": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div[1]/div/div/table/thead/tr/th"),
                           "ruleManage.table_row": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div[1]/div/div/table/tbody/tr"),
                           "ruleManage.table_tbody": "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/div[1]/div/div/table/tbody",
                           "ruleManage.dispalay_btn": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/ul"),
                           "ruleManage.dispalay_ul": (By.XPATH, "//*[@id=\"wrapper\"]/div/aside[2]/section/div/div/div/div/div/ul"),
                            }
