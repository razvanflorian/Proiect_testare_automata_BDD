from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
import time

class ReviewPage(BasePage):
    PRODUSE_PAGE = "https://magento.softwaretestingboard.com/breathe-easy-tank.html"
    REVIEWS_BUTTON = (By.ID, "tab-label-reviews-title")
    RATING_BUTTON = (By.XPATH, '//*[@id="Rating_1_label"]')
    INPUT_NICKNAME = (By.XPATH, '//*[@id="nickname_field"]')
    INPUT_SUMMARY = (By.XPATH, '//*[@id="summary_field"]')
    INPUT_REVIEW = (By.XPATH, '//*[@id="review_field"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="review-form"]/div/div/button')

    def open_page5(self):
        self.driver.get(self.PRODUSE_PAGE)

    def verify_url_products_page(self):
        assert self.driver.current_url == self.PRODUSE_PAGE

    def click_reviews_button(self):
        self.find(self.REVIEWS_BUTTON).click()

    def click_rating(self,):
        self.find(self.RATING_BUTTON).click()

    def set_nickname(self, text):
        self.find(self.INPUT_NICKNAME).send_keys(text)

    def set_summary(self, text):
        self.find(self.INPUT_SUMMARY).send_keys(text)

    def set_review(self, text):
        self.find(self.INPUT_REVIEW).send_keys(text)

    def click_submit_button(self):
        self.find(self.SUBMIT_BUTTON).click()
