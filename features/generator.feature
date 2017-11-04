Feature: Generator
  As a user
  I want to be able to automatically creates questions
  In order to easily populates my assessments

  Scenario: Successfully creating an arithmetic problem

    Given I am on the generator page
    Then I enter "0" as lower range and "60" as upper range
    When I click on the create button
    Then I see a list of generated problems

  Scenario: Trying to create an arithmetic problem without parameters

    Given I am on the generator page
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an arithmetic problem with invalid range

    Given I am on the generator page
    Then I enter "99999" as lower range and "-1" as upper range
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an arithmetic problem with too small range

    Given I am on the generator page
    Then I enter "0" as lower range and "1" as upper range
    When I click on the create button
    Then I see an error panel