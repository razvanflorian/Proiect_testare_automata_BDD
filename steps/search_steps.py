from behave import *

@given("I am on the home page")
def step_impl(context):
    context.search_page.open()

@Then("The URL of the Home Page is correct")
def step_impl(context):
    context.search_page.verify_url()

@When('I click the "What s New" button')
def step_impl(context):
    context.search_page.click_whats_new_button()

@When("I click the Pants button")
def step_impl(context):
    context.search_page.click_pants_button()

