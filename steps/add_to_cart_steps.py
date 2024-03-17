from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given("I am on the base page")
def step_impl(context):
    context.add_to_cart_page.open()

@Then("The Home Page URL is correct")
def step_impl(context):
    context.search_page.verify_url()


@When('I enter "Bags for laptop " in the search field')
def step_impl(context):
    context.add_to_cart_page.set_input_search_field("Bags for laptop")

@When("I click on the search button")
def step_impl(context):
    context.add_to_cart_page.click_button_search()

@When("I click on the product")
def step_impl(context):
    context.add_to_cart_page.click_button_product()


@When("I click Add to cart")
def step_impl(context):
    context.add_to_cart_page.click_button_add()

@Then('I should see "You added Endeavor Daytrip Backpack to your shopping cart"')
def step_impl(context):
    context.add_to_cart_page.verify_login_added_message()
