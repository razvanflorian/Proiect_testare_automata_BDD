from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
import time
import random



class RegisterPage(BasePage):
    REGISTER_URL = "https://magento.softwaretestingboard.com/customer/account/create/"
    INPUT_FIRST_NAME = (By.ID, "firstname")
    INPUT_LAST_NAME = (By.ID, "lastname")
    INPUT_EMAIL = (By.ID, "email_address")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "password-confirmation")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, '//*[@class="action submit primary"]')
    MESSAGE_MY_ACCOUNT = (By.XPATH, '//*[@class="base"]')

    def open_register(self):
        self.driver.get(self.REGISTER_URL)

    def verify_url_register(self):
        assert self.driver.current_url == self.REGISTER_URL

    def set_first_name(self, first_name):
        self.type(self.INPUT_FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        self.type(self.INPUT_LAST_NAME, last_name)

    def set_unique_email(self):
        number = random.randint(0, 9999999999999999)
        email_address = f"leomessi_{number}@yahoo.com"
        self.set_email(email_address)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def set_password_confirm(self, text):
        self.type(self.INPUT_PASSWORD_CONFIRM, text)

    def click_create_account_button(self):
        self.find(self.BUTTON_CREATE_ACCOUNT).click()

    def verify_success_message_displayed(self):
        assert self.find(self.MESSAGE_MY_ACCOUNT).is_displayed()

    # def verify_first_name_displayed(self):
    #     assert self.find(self.ERROR_FIRST_NAME).is_displayed()
    #
    # def verify_last_name_displayed(self):
    #     assert self.find(self.ERROR_LAST_NAME).is_displayed()
    #
    # def verify_email_displayed(self):
    #     assert self.find(self.ERROR_EMAIL).is_displayed()
    #
    # def verify_password_displayed(self):
    #     assert self.find(self.ERROR_PASSWORD).is_displayed()
    #
    # def verify_password_confirm_displayed(self):
    #     assert self.find(self.ERROR_PASSWORD_CONFIRM).is_displayed()









