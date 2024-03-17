from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

class AddPage(BasePage):
    HOME_PAGE = "https://magento.softwaretestingboard.com/"
    INPUT_SEARCH_FIELD = (By.ID, "search")
    BUTTON_SEARCH = (By.XPATH, '//*[@id="search_mini_form"]/div[2]/button')
    BUTTON_PRODUCT = (By.LINK_TEXT, "Endeavor Daytrip Backpack")
    BUTTON_ADD_TO_CART = (By.XPATH, '//*[@id="product-addtocart-button"]/span')
    ADDED_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div')


    def open(self):
        self.driver.get(self.HOME_PAGE)

    def verify_url(self):
        assert self.driver.current_url == self.HOME_PAGE



    def set_input_search_field(self, text):
        self.find(self.INPUT_SEARCH_FIELD).send_keys(text)

    def click_button_search(self):
        self.find(self.BUTTON_SEARCH).click()

    def click_button_product(self):
        self.find(self.BUTTON_PRODUCT).click()

    def click_button_add(self):
        self.find(self.BUTTON_ADD_TO_CART).click()

    def verify_login_added_message(self):
        assert self.find(self.ADDED_MESSAGE).is_displayed()





