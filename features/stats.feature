Feature: The manager accessing the reimbursement stats
  Background: The manager is logged in
    Given The manager is logged in

  Scenario: The manager clicks the stat button
    When The manager clicks the stat button
    Then Tables containing data should be displayed