from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class LoginPage(Page):
    LOGIN_USR = (By.CSS_SELECTOR, "[placeholder='Email']")
    LOGIN_PWD = (By.CSS_SELECTOR, "[placeholder='Password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "[class='login-button w-button']")

    def login(self):
        self.input_text('***********', *self.LOGIN_USR)
        self.input_text('********', *self.LOGIN_PWD)
        self.wait_and_click(*self.LOGIN_BTN)
        sleep(5)
