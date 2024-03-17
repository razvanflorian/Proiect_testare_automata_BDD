from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
import time

class ComparisonPage(BasePage):

    PRODUCT_PAGE = "https://magento.softwaretestingboard.com/hero-hoodie.html"
    COMPARE_BUTTON = (By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[2]/div[5]/div/a[2]')
    COMPARISON_LIST_BUTTON = (By.XPATH, '/html/body/div[2]/header/div[2]/ul/li/a')

    def open_product_page(self):
        self.driver.get(self.PRODUCT_PAGE)

    def verify_url_product(self):
        time.sleep(1)
        assert self.driver.current_url == self.PRODUCT_PAGE

    def click_compare_button(self):
        self.find(self.COMPARE_BUTTON).click()

    def click_comparison_list(self):
        self.find(self.COMPARISON_LIST_BUTTON).click()
