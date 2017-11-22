Feature: SimpleInterestGenerator
  As a user
  I want to be able to automatically creates simple interest questions
  In order to easily populates my assessments

  Scenario: Successfully creating an arithmetic problem
    Given I am a logged in professor
    Then I create the class "fuzzz", with students "Millui" "Cenlignes" and "Fatmodels" "Skinnycontrollers"
    Then I create the test "fizz" for skill "T4-U5-A1b"
    Then I click on generate the question
    Given I am on the generator page
    Then I select the simple interest problem generator
    Then I set the time placed to month
    Then I set the type of rate to month
    When I click on the create button
    Then I see a list of generated problems
    Then I choose a generated problem
    Then I click on going back to the test