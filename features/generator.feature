Feature: Generator
  As a user
  I want to be able to automatically creates questions
  In order to easily populates my assessments

  Scenario: Successfully creating an arithmetic problem
    Given The db is populated
    Given I am an existing non logged professor
    Then I log in
    Then I go on class creation page
    Then I create a class "foobar"
    Then I create two students, "Jean" "Khule" and "Bill" "Boquet" for my class
    Then I access the class test page
    Then I click on add a test
    Then I click on add a test online
    Then I select the skill "T4-U5-A1b"
    Then I add that competence
    Then I add a name to that test
    Then I create the test
    Then I click on generate the question
    Given I am on the generator page
    Then I enter "0" as lower range and "60" as upper range
    When I click on the create button
    Then I see a list of generated problems

  Scenario: Trying to create an arithmetic problem without parameters
    Given The db is populated
    Given I am an existing non logged professor
    Then I log in
    Then I go on class creation page
    Then I create a class "foobar"
    Then I create two students, "Jean" "Khule" and "Bill" "Boquet" for my class
    Then I access the class test page
    Then I click on add a test
    Then I click on add a test online
    Then I select the skill "T4-U5-A1b"
    Then I add that competence
    Then I add a name to that test
    Then I create the test
    Then I click on generate the question
    Given I am on the generator page
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an arithmetic problem with invalid range
    Given The db is populated
    Given I am an existing non logged professor
    Then I log in
    Then I go on class creation page
    Then I create a class "foobar"
    Then I create two students, "Jean" "Khule" and "Bill" "Boquet" for my class
    Then I access the class test page
    Then I click on add a test
    Then I click on add a test online
    Then I select the skill "T4-U5-A1b"
    Then I add that competence
    Then I add a name to that test
    Then I create the test
    Then I click on generate the question
    Given I am on the generator page
    Then I enter "99999" as lower range and "-1" as upper range
    When I click on the create button
    Then I see an error panel

  Scenario: Trying to create an arithmetic problem with too small range
    Given The db is populated
    Given I am an existing non logged professor
    Then I log in
    Then I go on class creation page
    Then I create a class "foobar"
    Then I create two students, "Jean" "Khule" and "Bill" "Boquet" for my class
    Then I access the class test page
    Then I click on add a test
    Then I click on add a test online
    Then I select the skill "T4-U5-A1b"
    Then I add that competence
    Then I add a name to that test
    Then I create the test
    Then I click on generate the question
    Given I am on the generator page
    Then I enter "0" as lower range and "1" as upper range
    When I click on the create button
    Then I see an error panel