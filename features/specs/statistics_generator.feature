Feature: StatisticsGenerator
  As a user
  I want to be able to automatically creates arithmetical polynomial questions
  In order to easily populates my assessments

  Scenario: Successfully creating an statistic problem
    Given I am logged with a fresh class, created a test and accessed question generator
    Then I select the statistic problem generator
    # Order seems important for those next two lines
    # I guess phantomjs is loosing his mind as the range fields are the same than default form, which is Arithmetic
    Then I enter "50" elements asked
    Then I enter "0" as lower range and "60" as upper range
    When I click on the create button
    Then I see a list of generated problems
    Then I choose a generated problem
    Then I click on going back to the test

  Scenario: Trying to create an statistic problem without parameters
    Given I am logged with a fresh class, created a test and accessed question generator
    Then I select the statistic problem generator
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an statistic problem with invalid range
    Given I am logged with a fresh class, created a test and accessed question generator
    Then I select the statistic problem generator
    Then I enter "50" elements asked
    Then I enter "99999" as lower range and "-1" as upper range
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an statistic problem with too small range
    Given I am logged with a fresh class, created a test and accessed question generator
    Then I select the statistic problem generator
    Then I enter "50" elements asked
    Then I enter "0" as lower range and "0" as upper range
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an statistic problem with negative amount of elements asked
    Given I am logged with a fresh class, created a test and accessed question generator
    Then I select the statistic problem generator
    Then I enter "-1000000" elements asked
    Then I enter "0" as lower range and "60" as upper range
    When I click on the create button
    Then I see an error panel