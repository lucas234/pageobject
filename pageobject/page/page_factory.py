from base_page import BasePage 
from login_page import LoginPage 
from menu_page import MenuPage
from register_page import RegisterPage 
from search_page import SearchPage 

 
def get_page(page_name, driver):
    "Return the appropriate page object based on page_name"
    pages = {'base': BasePage(driver),  'login': LoginPage(driver),  'main': MenuPage(driver),  'register': RegisterPage(driver),  'search': SearchPage(driver),  }
    obj_page = pages.get(page_name)
    return obj_page