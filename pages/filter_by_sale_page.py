from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class FilterBySalePage(Page):
    FILTER_RESULTS_TXT = (By.CSS_SELECTOR, "[aria-current='page']")
    OFF_PLAN = (By.CSS_SELECTOR, "[aria-current='page']")
    FILTERS = (By.CSS_SELECTOR, "[class='filter-button w-inline-block']")
    BALI = (By.CSS_SELECTOR, "[class='tag-properties']")
    LOCATION = (By.CSS_SELECTOR, "[name='Location']")

    def open(self):
        self.open_url('https://soft.reelly.io')

    def click_off_plan(self):
        self.wait_and_click(*self.OFF_PLAN)

    def verify_text(self, *OFF_PLAN):
        actual_text = self.driver.find_element(*self.OFF_PLAN).text
        assert 'Off-plan' in actual_text, f'Expected Off-plan not in actual {actual_text}'

    def click_filters(self):
        self.wait_and_click(*self.FILTERS)

    def click_bali(self):
        self.wait_and_click(*self.BALI)

    def verify_location(self):
        actual_text = self.driver.find_element(*self.LOCATION).text
        assert 'Bali' in actual_text, f'Expected Bali not in actual {actual_text}'
