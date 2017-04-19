# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
from login_page import LoginPage
from menu_page import MainPage
from base_page import BasePage
from register_page import RegisterPage
from search_page import SearchPage
import os


def get_page(page_name, driver):
    """Return the appropriate page object based on page_name"""
    page = {"login": LoginPage(driver), "main": MainPage(driver),
            "register": RegisterPage(driver), "search": SearchPage(driver),
            "base": BasePage(driver), }
    obj_page = page.get(page_name)
    return obj_page


def create_get_page_file(file_name):
    """自动遍历page文件夹,获取所有page文件名(获取page类名),创建page_factory.py"""
    page_path = os.path.dirname(__file__)
    ls = os.listdir(page_path)
    module_name = """"""
    page = """pages = {"""
    for j, i in enumerate(ls):
        if i.endswith("page.py"):
            split_file_name = i[:-3].split("_")
            class_name = "".join(map(lambda x: x.capitalize(), split_file_name))
            module_name += """from {0} import {1} \n""".format(i[:-3], class_name)
            page += """'{0:^}': {1}(driver),  """.format(split_file_name[0], class_name).ljust(10)
        else:
            continue
    page += """}"""
    function_str = """def get_page(page_name, driver):
    "Return the appropriate page object based on page_name"
    %s
    obj_page = pages.get(page_name)
    return obj_page""" % page
    with open(os.path.join(page_path, "%s.py" % file_name), "w+") as f:
        f.write(module_name)
        f.write("\n \n")
        f.write(function_str)

create_get_page_file("page_factory")