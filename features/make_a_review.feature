Feature: Make a review
  Background: Open page list
    Given  I am on the produce page
    Then The produce page url is correct

    Scenario: write a review
      When I click on the review button
      And I click on the rating button
      And I enter a nickname button
      And I enter a summary info
      And I enter a review info
      Then I click on the submit review button