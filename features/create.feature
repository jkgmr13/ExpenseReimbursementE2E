Feature: The employee creates a new reimbursement request
  Scenario: The employee successfully creates a new reimbursement request via input fields
    Given The employee is logged in
    Given The employee has clicked the create button
    When The employee enters the amount
    When The employee enters the reason
    When The employee clicks the submit button
    Then A new request should be added to the view page
  Scenario: The employee fails to create a new reimbursement request
        Given The employee is logged in
        Given The employee has clicked the create button
        When The employee enters the amount
        When The employee clicks the submit button
        Then An alert should indicate required fields

