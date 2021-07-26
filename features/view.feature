Feature: View Reimbursements

  Scenario: Employee views reimbursements
    Given The employee is logged in
    When The employee clicks the view button
    Then Their reimbursements should be displayed

  Scenario: Manager views reimbursements
    Given The manager is logged in
    When The manager clicks the view button
    Then All pending reimbursements should be displayed

   Scenario: Manager views past reimbursements
     Given The manager is logged in
     When The manager clicks the view button
     When The manager clicks the past button
     Then All past reimbursements should be displayed