from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

class RemovePage(BasePage):
    HOME_PAGE_1 = "https://magento.softwaretestingboard.com/"
    PRODUCT_SELECT = (By.LINK_TEXT, "Radiant Tee")
    SIZE_BUTTON = (By.ID, "option-label-size-143-item-167")
    COLOR_BUTTON = (By.ID, "option-label-color-93-item-56")
    PRESS_ADD_TO_CART = (By.XPATH, '//*[@id="product-addtocart-button"]/span')
    ITEM_CART_BUTTON = (By.LINK_TEXT, "shopping cart")
    # VIEW_EDIT_BUTTON = (By.XPATH, '//*[@id="minicart-content-wrapper"]/div[2]/div[5]/div/a/span')
    REMOVE_BUTTON = (By.XPATH, '//*[@id="shopping-cart-table"]/tbody[2]/tr[2]/td/div/a[2]')

    def open(self):
           self.driver.get(self.HOME_PAGE_1)

    def verify_url_home(self):
        assert self.driver.current_url == self.HOME_PAGE_1

    def click_on_product(self):
        self.find(self.PRODUCT_SELECT).click()

    def click_size(self):
        self.find(self.SIZE_BUTTON).click()

    def click_color(self):
        self.find(self.COLOR_BUTTON).click()

    def click_add_cart(self):
        self.find(self.PRESS_ADD_TO_CART).click()

    def click_item_cart(self):
        self.find(self.ITEM_CART_BUTTON).click()

    # def click_view_edit(self):
    #     self.find(self.VIEW_EDIT_BUTTON).click()

    def click_remove_item(self):
        self.find(self.REMOVE_BUTTON).click()


