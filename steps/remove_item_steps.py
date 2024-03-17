from behave import *

from selenium import webdriver


@given("I am on the home page1")
def step_impl(context):
    context.remove_item_page.open()


@then("The Home Page1 URL is correct")
def step_impl(context):
    context.remove_item_page.verify_url_home()


@then("I click on the product button")
def step_impl(context):
    context.remove_item_page.click_on_product()


@then("I click on the size")
def step_impl(context):
    context.remove_item_page.click_size()


@then("I click on the color")
def step_impl(context):
    context.remove_item_page.click_color()


@then("I click Add to Basket")
def step_impl(context):
    context.remove_item_page.click_add_cart()


@then("I click on the item cart")
def step_impl(context):
    context.remove_item_page.click_item_cart()


# @then("I click on View and Edit Cart")
# def step_impl(context):
#     context.remove_item_page.click_view_edit()


@then("I click on the Remove button")
def step_impl(context):
    context.remove_item_page.click_remove_item()
