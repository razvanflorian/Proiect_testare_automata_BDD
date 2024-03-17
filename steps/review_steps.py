from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given("I am on the produce page")
def step_impl(context):
    context.review_page.open_page5()

@then("The produce page url is correct")
def step_impl(context):
    context.review_page.verify_url_products_page()

@when("I click on the review button")
def step_impl(context):
    context.review_page.click_reviews_button()

@when("I click on the rating button")
def step_impl(context):
    context.review_page.click_rating()

@when("I enter a nickname button")
def step_impl(context):
    context.review_page.set_nickname("Traian")

@when("I enter a summary info")
def step_impl(context):
    context.review_page.set_summary("Foarte Fain")

@when("I enter a review info")
def step_impl(context):
    context.review_page.set_review("Ceva super fain. Im vine extraordinar")

@then("I click on the submit review button")
def step_impl(context):
    context.review_page.click_submit_button()
