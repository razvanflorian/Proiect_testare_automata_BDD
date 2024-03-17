Feature: Registration page

  Background: Open register page
    Given I am on the register page
    Then The register page url is correct


  Scenario: Register new account with valid data
    When I enter "Leo" in the first name input
    And I enter "Messi" in the last name input
    And I enter a random email address in the email input
    And I enter "Leomessithegoat0" in the password input
    And I enter "Leomessithegoat0" in the password confirm input
    And I click the register button
    Then My account page is displayed


#   Scenario: Register without completing mandatory fields
#     When I click the register button
#     Then First name error is displayed
#     Then Last name error is displayed
#     Then Email error is displayed
#     Then Password error is displayed
#     Then Password confirm error is displayed



