Feature: Login

  Background:
    Given The user is on the login page
  Scenario: Employee logs in successfully
    When The employee enters the correct username
    When The employee enters the correct password
    When The employee clicks the login button
    Then The employee should be navigated to the employee page

  Scenario: Employee logs in unsuccessfully
    When The employee enters the incorrect username
    When The employee enters the correct password
    When The employee clicks the login button
    Then The user should see an invalid credentials alert

   Scenario: Manager logs in successfully
     When The manager enters the correct username
     When The manager enters the correct password
     When The manager clicks the login button
     Then The manager should be navigated to the manager page

   Scenario: Manager logs in unsuccessfully
     When The manager enters the correct username
     When The manager enters the incorrect username
     When The manager clicks the login button
     Then The user should see an invalid credentials alert
