Feature: Remove Page

  Background: Open home page1
    Given I am on the home page1
    Then The Home Page1 URL is correct


  Scenario: ADD an item to cart
      And I click on the product button
      And I click on the size
      And I click on the color
      And I click Add to Basket
      And I click on the item cart
#      And I click on View and Edit Cart
      Then I click on the Remove button
