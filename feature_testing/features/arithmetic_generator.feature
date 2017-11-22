Feature: ArithmeticGenerator
  As a user
  I want to be able to automatically creates arithmetical polynomial questions
  In order to easily populates my assessments

  Scenario: Successfully creating an arithmetic problem
    Given I am a logged in professor
    Then I create the class "fuzzz", with students "Millui" "Cenlignes" and "Fatmodels" "Skinnycontrollers"
    Then I create the test "fizz" for skill "T4-U5-A1b"
    Then I click on generate the question
    Given I am on the generator page
    Then I select the arithmetic problem generator
    Then I enter "0" as lower range and "60" as upper range
    When I click on the create button
    Then I see a list of generated problems
    Then I choose a generated problem
    Then I click on going back to the test

  Scenario: Successfully creating an arithmetic problem with rational domain
    Given I am a logged in professor
    Then I create the class "fuzzz", with students "Millui" "Cenlignes" and "Fatmodels" "Skinnycontrollers"
    Then I create the test "fizz" for skill "T4-U5-A1b"
    Then I click on generate the question
    Given I am on the generator page
    Then I select the arithmetic problem generator
    Then I enter "0" as lower range and "60" as upper range
    Then I select the rational domain
    When I click on the create button
    Then I see a list of generated problems
    Then I choose a generated problem
    Then I click on going back to the test


  Scenario: Trying to create an arithmetic problem without parameters
    Given I am a logged in professor
    Then I create the class "fuzzz", with students "Millui" "Cenlignes" and "Fatmodels" "Skinnycontrollers"
    Then I create the test "fizz" for skill "T4-U5-A1b"
    Then I click on generate the question
    Given I am on the generator page
    Then I select the arithmetic problem generator
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an arithmetic problem with invalid range
    Given I am a logged in professor
    Then I create the class "fuzzz", with students "Millui" "Cenlignes" and "Fatmodels" "Skinnycontrollers"
    Then I create the test "fizz" for skill "T4-U5-A1b"
    Then I click on generate the question
    Given I am on the generator page
    Then I select the arithmetic problem generator
    Then I enter "99999" as lower range and "-1" as upper range
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an arithmetic problem with too small range
    Given I am a logged in professor
    Then I create the class "fuzzz", with students "Millui" "Cenlignes" and "Fatmodels" "Skinnycontrollers"
    Then I create the test "fizz" for skill "T4-U5-A1b"
    Then I click on generate the question
    Given I am on the generator page
    Then I select the arithmetic problem generator
    Then I enter "0" as lower range and "1" as upper range
    When I click on the create button
    Then I see an error panel