from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/login/referer/"
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "pass")
    BUTTON_SIGN_IN = (By.XPATH, '//*[@class="action login primary"]')
    DIV_ERROR_MESSAGE = (By.XPATH, '//*[@class="page messages"]')




    def open(self):
           self.driver.get(self.LOGIN_PAGE_URL)

    def verify_url(self):
             assert self.driver.current_url == self.LOGIN_PAGE_URL


    def set_email(self, text):
        self.find(self.INPUT_EMAIL).send_keys(text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_sign_up_button(self):
        self.find(self.BUTTON_SIGN_IN).click()


    # def verify_the_incorrect_sign_in_message(self):
    #     assert "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later" in self.find(self.DIV_ERROR_MESSAGE).text

    def verify_login_error_message(self,):
        assert self.find(self.DIV_ERROR_MESSAGE).is_displayed()

