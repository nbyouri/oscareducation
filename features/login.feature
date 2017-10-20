Feature: Login

  Scenario: Login as a professor

    Given an existing non logged professor
    When I submit a valid login page
    Then I am redirected to the professor home page

  Scenario: Login as a student

    Given an existing non logged student
    When I submit a valid login page
    Then I am redirected to the student home page

  Scenario: Login with wrong password

    Given an existing non logged professor
    When I submit an invalid password but valid account
    Then I am redirected to the login fail page

  Scenario: Login with wrong username
    Given an existing non logged professor
    When I submit an invalid username
    Then I am redirected to the login fail page