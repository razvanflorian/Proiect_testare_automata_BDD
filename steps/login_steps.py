from behave import *

from selenium import webdriver


@given("I am on the login page")
def step_impl(context):
    context.login_page.open()


@then("The URL of the Login Page is correct")
def step_impl(context):
    context.login_page.verify_url()


@when("I enter an unregistered email")
def step_impl(context):
    context.login_page.set_email("serban12@yahoo.com")


@when("I enter a password")
def step_impl(context):
    context.login_page.set_password("12555")


@when("I click the sign up button")
def step_impl(context):
    context.login_page.click_sign_up_button()


@then(
    'I should see "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try '
    'again later"')
def step_impl(context):
    context.login_page.verify_login_error_message()


@given('I am on the Magento login page')
def step_impl(context):
    context.login_page.open_page()


@when('I enter "{text}" as email')
def step_impl(context, text):
    context.login_page.enter_email(text)


@when('I enter "{text}" as password')
def step_impl(context, text):
    context.login_page.enter_password(text)


@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I should see "The account sign-in was incorrect or your account is disabled temporarily"')
def step_impl(context):
    context.login_page.err_message()




