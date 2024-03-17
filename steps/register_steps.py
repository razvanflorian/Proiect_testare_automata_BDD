from behave import *

@given('I am on the register page')
def step_impl(context):
    context.register_page.open_register()

@then("The register page url is correct")
def step_impl(context):
    context.register_page.verify_url_register()

@When('I enter "Leo" in the first name input')
def step_impl(context):
    context.register_page.set_first_name("Leo")

@When('I enter "Messi" in the last name input')
def step_impl(context):
    context.register_page.set_last_name("Messi")

@When('I enter a random email address in the email input')
def step_impl(context):
    context.register_page.set_unique_email()

@When('I enter "Leomessithegoat0" in the password input')
def step_impl(context):
    context.register_page.set_password("Leomessithegoat0")

@When('I enter "Leomessithegoat0" in the password confirm input')
def step_impl(context):
    context.register_page.set_password_confirm("Leomessithegoat0")

@When('I click the register button')
def step_impl(context):
    context.register_page.click_create_account_button()

@Then('My account page is displayed')
def step_impl(context):
    context.register_page.verify_success_message_displayed()




# @Then("First name error is displayed")
# def step_impl(context):
#     context.register_page.verify_first_name_error_displyed()
#
# @Then("Last name error is displayed")
# def step_impl(context):
#     context.register_page.verify_last_name_error_displyed()
#
# @Then("Email error is displayed")
# def step_impl(context):
#     context.register_page.verify_email_error_displyed()
#
# @Then("Password error is displayed")
# def step_impl(context):
#     context.register_page.verify_password_error_displyed()
#
# @Then("Password confirm error is displayed")
# def step_impl(context):
#     context.register_page.verify_password_confirm_error_displyed()
#




