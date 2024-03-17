Feature: Add to cart

  Background: Open home page
    Given I am on the base page
    Then The Home Page URL is correct

    Scenario: Add to cart
      When I enter "Bags for laptop " in the search field
      And I click on the search button
      And I click on the product
      And I click Add to cart
      Then I should see "You added Endeavor Daytrip Backpack to your shopping cart"


