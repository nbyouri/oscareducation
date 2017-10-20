Feature: Login

  Scenario: Login as a professor

    Given an anonymous professor
    When I submit a valid login page
    Then I am redirected to the professor home page

  Scenario: Login as a student

    Given an anonymous student
    When I submit a valid login page
    Then I am redirected to the student home page

  Scenario: Login as non-registered user

    Given an anonymous professor
    When I submit an invalid login page
    Then I am redirected to the login fail page