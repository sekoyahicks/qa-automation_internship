from pages.header import Header
from pages.main_page import MainPage
from pages.base_page import Page
from pages.filter_by_sale_page import FilterBySalePage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.filter_by_sale_page = FilterBySalePage(driver)