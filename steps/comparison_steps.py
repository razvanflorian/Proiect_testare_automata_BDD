from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




@Given("I am on the product page")
def step_impl(context):
    context.comparison_page.open_product_page()

@Then("The product page url is correct")
def step_impl(context):
    context.comparison_page.verify_url_product()

@When("I click on the Add button")
def step_impl(context):
    context.comparison_page.click_compare_button()

@When("I click on the comparison list")
def step_impl(context):
    context.comparison_page.click_comparison_list()