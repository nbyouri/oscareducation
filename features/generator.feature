Feature: Generator
  As a user
  I want to be able to automatically creates questions
  In order to easily populates my assessments

  Scenario: Successfully creating an arithmetic problem

    Given I am on the generator page
    Then I enter a lower range
    Then I enter an upper range
    When I click on the create button
    Then I see a list of generated problems