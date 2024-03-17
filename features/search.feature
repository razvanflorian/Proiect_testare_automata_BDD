Feature: Search

  Background: Open home page
    Given I am on the home page
    Then The URL of the Home Page is correct

  Scenario: Search works properly from home page
    When I click the "What s New" button
    And I click the Pants button


