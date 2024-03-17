from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

class HomePage(BasePage):
    HOME_PAGE_URL = "https://magento.softwaretestingboard.com/"
    BUTTON_WHATS_NEW = (By.ID, "ui-id-3")
    BUTTON_PANTS = (By.LINK_TEXT, 'Pants')

    def open(self):
        self.driver.get(self.HOME_PAGE_URL)

    def verify_url(self):
        assert self.driver.current_url == self.HOME_PAGE_URL

    def click_whats_new_button(self):
        self.find(self.BUTTON_WHATS_NEW).click()

    def click_pants_button(self):
        self.find(self.BUTTON_PANTS).click()




