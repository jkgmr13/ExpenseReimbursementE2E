Feature: Implement the ability to logout
  Scenario: The Employee logs out
    Given The employee is logged in
    When The employee clicks the logout button
    Then The employee should be redirected to the login page

    Scenario: The Manager logs out
      Given The manager is logged in
      When The manager clicks the logout button
      Then The manager should be redirected to the login page