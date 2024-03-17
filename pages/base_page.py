from selenium import webdriver
from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
class BasePage(Browser):

     INPUT_SEARCH = (By.ID, "search")
     def is_url_correct(self, text):
         self.driver.current_url ==text

     def find(self, locator):
        return self.driver.find_element(*locator)

     def type(self, locator, text):
        self.find(locator).send_keys(text)

     def set_search_term(self, text):
         self.type(self.INPUT_SEARCH, text)

