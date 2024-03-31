Feature: Login Page
  @smoke @regression
  Scenario: Check that the URL is correct
    Given I am on the login page
    Then The URL of the Login Page is correct

  @regression
  Scenario: Log in with unregistered email
    Given I am on the login page
    When I enter an unregistered email
    And I enter a password
    And I click the sign up button
    Then I should see "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later"



  Scenario Outline: Invalid login with invalid credentials
    Given I am on the Magento login page
    When I enter "<email>" as email
    And I enter "<password>" as password
    And I click on the login button
    Then I should see "The account sign-in was incorrect or your account is disabled temporarily"

  Examples:
    | email             | password  |
    | Lolita3@yahoo.com | wrongness |
    | Lolita4@yahoo.com | 123456    |







